#!/usr/bin/env python3
"""Download and verify the exact ten public ZIPs at an immutable Git commit.

Run only after pushing the requested commit:
    python tools/verify_published.py FULL_COMMIT_SHA --root SOURCE_ROOT

Uses public GitHub HTTPS through the configured egress proxy and CA trust,
without a GitHub token, .netrc, cookies, or directly injected auth headers.
A failure produces a failed report
and a nonzero exit status; no successful download is inferred from a push.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import ssl
import sys
import tempfile
from urllib.parse import quote, urlsplit
from urllib.request import (
    HTTPRedirectHandler, HTTPSHandler, ProxyHandler, Request, build_opener,
)

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'tommi0503/skills-introduction-to-github'
PUBLISHED_FOLDER = 'rhetis-part07-elements-v2/deliverables'
COLLECTIONS = ('vectorbox', 'seedmark', 'crossrail', 'meridian-deck', 'onboard-docket')
ARCHIVES = tuple(name for k in COLLECTIONS for name in (f'{k}.zip', f'{k}-review.zip'))
CHUNK_BYTES = 1024 * 1024


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha_file(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(CHUNK_BYTES), b''):
            h.update(chunk)
    return h.hexdigest()


def full_commit(value):
    if not re.fullmatch(r'[0-9a-fA-F]{40}', value):
        raise argparse.ArgumentTypeError('Pass the full 40-character Git commit SHA, not a branch or abbreviated SHA.')
    return value.lower()


def read_checksums(path):
    records = {}
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r'([0-9a-fA-F]{64})  ([^\r\n]+)', line)
        if not match:
            raise ValueError(f'Invalid SHA256SUMS line {number}')
        digest, name = match.groups()
        if name not in ARCHIVES or name in records or PurePosixPath(name).name != name:
            raise ValueError(f'Unexpected or duplicate archive name: {name}')
        records[name] = digest.lower()
    if set(records) != set(ARCHIVES) or len(records) != 10:
        raise ValueError('SHA256SUMS must identify exactly the ten requested collection/review ZIPs.')
    return records


class PublicRedirects(HTTPRedirectHandler):
    """Allow only HTTPS GitHub content redirects, never credentials in a URL."""
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urlsplit(newurl)
        host = (parsed.hostname or '').lower()
        if (parsed.scheme != 'https' or parsed.username is not None or parsed.password is not None
                or not (host == 'githubusercontent.com' or host.endswith('.githubusercontent.com'))):
            raise ValueError(f'Unexpected public download redirect host/scheme: {parsed.scheme}://{host}')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def load_package(root):
    path = root / 'tools' / 'package.py'
    spec = importlib.util.spec_from_file_location('rhetis_publication_package', path)
    if spec is None or spec.loader is None:
        raise ValueError(f'Cannot load package verifier: {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not callable(getattr(module, 'verify_zip', None)):
        raise ValueError('package.py does not expose verify_zip')
    return module, sha_file(path)


def write_report(root, report):
    destination = root / 'publication-verification.json'
    temporary = destination.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(destination)


def check_png_sizes(dimensions):
    for name, size in dimensions.items():
        parts = PurePosixPath(name).parts
        if len(size) != 2 or min(size) <= 0:
            raise ValueError(f'Invalid PNG dimensions: {name}: {size}')
        if any(folder in parts for folder in ('reassembled', 'foundation-sheets')) and size != [1280, 720]:
            raise ValueError(f'Expected a 1280x720 page PNG: {name}: {size}')
        if 'compare-reassembled' in parts and size != [3840, 720]:
            raise ValueError(f'Expected a 3840x720 comparison PNG: {name}: {size}')


def run(commit, root):
    report = {
        'schema': 'rhetis.publication-verification/1', 'status': 'in-progress',
        'startedAtUTC': now(), 'repository': REPOSITORY, 'commitSHA': commit,
        'sourceRoot': str(root), 'publishedFolder': PUBLISHED_FOLDER,
        'networkAuthentication': 'public GitHub, configured egress proxy; no GitHub token/cookies/netrc',
        'expectedArchiveNames': list(ARCHIVES), 'archives': [], 'errors': [],
    }
    write_report(root, report)
    try:
        sums = root / 'deliverables' / 'SHA256SUMS'
        expected = read_checksums(sums)
        report['checksumsFile'] = str(sums)
        report['checksumsFileSHA256'] = sha_file(sums)
        package, package_sha = load_package(root)
        report['packageVerifierSHA256'] = package_sha
        local = {}
        # Check all local originals before making any network request.
        for name in ARCHIVES:
            path = root / 'deliverables' / name
            if not path.is_file() or path.is_symlink():
                raise ValueError(f'Local original ZIP missing or symlinked: {name}')
            digest = sha_file(path)
            if digest != expected[name]:
                raise ValueError(f'Local ZIP does not match SHA256SUMS: {name}')
            local[name] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest}
        directory = Path(tempfile.mkdtemp(prefix=f'rhetis-publication-{commit[:12]}-', dir='/tmp'))
        report['downloadDirectory'] = str(directory)
        # urllib does not consult .netrc. Preserve the runtime egress proxy and
        # configured CA trust; never read/print credentials or inject GitHub auth.
        opener = build_opener(ProxyHandler(), PublicRedirects(), HTTPSHandler(context=ssl.create_default_context()))
        for name in ARCHIVES:
            url = f'https://raw.githubusercontent.com/{REPOSITORY}/{commit}/{PUBLISHED_FOLDER}/{quote(name, safe="")}'
            target = directory / name
            partial = target.with_suffix('.zip.part')
            item = {'name': name, 'url': url, 'localOriginal': local[name],
                    'expectedSHA256': expected[name], 'downloadPath': str(target), 'status': 'downloading'}
            report['archives'].append(item)
            try:
                request = Request(url, headers={'Accept': 'application/octet-stream', 'Accept-Encoding': 'identity',
                                                'User-Agent': 'Rhetis-publication-verifier/1'})
                digest = hashlib.sha256()
                received = 0
                with opener.open(request, timeout=45) as response, partial.open('wb') as stream:
                    item['httpStatus'] = response.status
                    item['finalURL'] = response.geturl()
                    item['contentLength'] = response.headers.get('Content-Length')
                    item['contentType'] = response.headers.get('Content-Type')
                    if response.status != 200:
                        raise ValueError(f'Expected HTTP 200, received {response.status}')
                    while True:
                        chunk = response.read(CHUNK_BYTES)
                        if not chunk:
                            break
                        received += len(chunk)
                        if received > local[name]['bytes']:
                            raise ValueError('HTTP body exceeds the exact local ZIP byte count')
                        stream.write(chunk)
                        digest.update(chunk)
                item['downloadedBytes'] = received
                item['downloadedSHA256'] = digest.hexdigest()
                item['byteCountMatches'] = received == local[name]['bytes']
                item['sha256Matches'] = digest.hexdigest() == expected[name]
                if not item['byteCountMatches'] or not item['sha256Matches']:
                    raise ValueError('Downloaded bytes/SHA256 do not match the local original')
                partial.replace(target)
                checked = package.verify_zip(target)
                expected_root = name[:-4]
                if checked['topFolder'] != expected_root:
                    raise ValueError(f'Unexpected top folder: {checked["topFolder"]}; expected {expected_root}')
                if checked['bytes'] != received or checked['sha256'] != expected[name]:
                    raise ValueError('Package verifier bytes/SHA256 differ from the downloaded archive')
                if name.endswith('-review.zip'):
                    manifest = expected_root + '/verification/package-manifest.json'
                    if not any(row['path'] == manifest for row in checked['files']):
                        raise ValueError('Review ZIP lacks its embedded package manifest')
                check_png_sizes(checked['pngDimensions'])
                item['zipVerification'] = {
                    'crc': checked['crc'], 'safePaths': 'passed', 'topFolder': checked['topFolder'],
                    'entryCount': checked['entryCount'], 'pngCRC': 'passed',
                    'pngCount': len(checked['pngDimensions']), 'pngDimensions': checked['pngDimensions'],
                    'embeddedReviewManifest': 'passed' if name.endswith('-review.zip') else 'not-applicable',
                }
                item['status'] = 'verified'
                print(f'{name}: HTTP 200, exact bytes/SHA256, ZIP CRC/path/PNG passed', flush=True)
            except Exception as error:
                item['status'] = 'failed'
                item['error'] = f'{type(error).__name__}: {error}'
                if partial.exists():
                    item['partialDownloadPath'] = str(partial)
                    item['partialBytes'] = partial.stat().st_size
                report['errors'].append({'archive': name, 'error': item['error']})
                print(f'{name}: FAILED: {item["error"]}', file=sys.stderr, flush=True)
            write_report(root, report)
        if len(report['archives']) != 10 or any(row['status'] != 'verified' for row in report['archives']):
            report['status'] = 'failed'
        else:
            report['status'] = 'verified'
    except Exception as error:
        report['status'] = 'failed'
        report['errors'].append({'stage': 'preflight', 'error': f'{type(error).__name__}: {error}'})
        print(f'Publication verification FAILED: {error}', file=sys.stderr, flush=True)
    report['completedAtUTC'] = now()
    report['verifiedArchiveCount'] = sum(row['status'] == 'verified' for row in report['archives'])
    write_report(root, report)
    print(str(root / 'publication-verification.json'), flush=True)
    return 0 if report['status'] == 'verified' else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('commit_sha', type=full_commit, help='Full immutable 40-character Git commit SHA')
    parser.add_argument('--root', type=Path, default=ROOT, help='Source ROOT containing tools/package.py and deliverables/SHA256SUMS')
    args = parser.parse_args()
    return run(args.commit_sha, args.root.resolve())


if __name__ == '__main__':
    raise SystemExit(main())
