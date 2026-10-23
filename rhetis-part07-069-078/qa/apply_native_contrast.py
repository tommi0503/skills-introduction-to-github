"""Resolve only snapshot-matched sibling-paint contrast, retaining all raw candidates."""
import json
from audit_css import BASE

proof_path = BASE / 'qa/crossrail-native-contrast.json'
proof = json.loads(proof_path.read_text())
for name in ['crossrail-contrast-audit.json', 'crossrail-contrast-min-audit.json']:
    path = BASE / 'qa' / name
    report = json.loads(path.read_text())
    for mode, result in report.items():
        measured = proof[mode]
        if measured['sourceSha256'] != result['sourceSha256']:
            raise SystemExit(f'Stale native paint proof: {name} {mode}')
        raw = result.get('rawCandidates', result['candidates'])
        result['rawCandidates'] = raw
        kept, verified = [], []
        for candidate in raw:
            matches = [r for r in measured['rows'] if
                       candidate['fixture'] == measured['fixture'] and
                       all(candidate[k] == r[k] for k in ['text', 'class', 'size'])]
            if len(matches) == 1 and matches[0].get('pass'):
                verified.append({'candidate': candidate, 'nativePaint': matches[0]})
            else:
                kept.append(candidate)
        for row in measured['rows']:
            if row.get('pass') is not False:
                continue
            if not any(x['fixture'] == measured['fixture'] and
                       all(x[k] == row[k] for k in ['text', 'class', 'size']) for x in kept):
                kept.append({k: row[k] for k in ['text', 'class', 'size', 'ratio', 'threshold']} |
                            {'fixture': measured['fixture'], 'source': 'native-painted-background'})
        result['candidates'] = kept
        result['nativeVerifiedPasses'] = verified
        result['nativePaintProof'] = str(proof_path.relative_to(BASE))
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(name, {mode: len(r['candidates']) for mode, r in report.items()})
