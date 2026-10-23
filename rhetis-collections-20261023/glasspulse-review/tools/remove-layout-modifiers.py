from pathlib import Path
import hashlib,json,re
C=Path('/workspace/output/glasspulse');R=Path('/workspace/output/glasspulse-review');W=Path('/workspace/work/glasspulse')
files=list((R/'reassembled').glob('*.png'))+list((R/'compare-reassembled').glob('*.png'))+list((R/'library').glob('*/light.png'))+list((R/'library').glob('*/dark.png'))
(W/'modifier-before.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}))
p=C/'foundation/foundation.css';s=p.read_text();replacements={
'.slide .head.low:not(.center)':'.slide .head:not(.center):is(:has(+.body>.stack>[data-el$="-delta"]),:has(+.body>[data-el$="-venn"]))',
'.slide .head.mid:not(.center)':'.slide .head:not(.center):has(+.body>.group.two)',
'.slide .head.low.center':'.slide .head.center:has(+.body>.group>[data-el]>.parts>.kick):not(:has(+.body>.group>[data-el]>.parts>.fig))',
'.slide .stack.tight':'.slide .page:has(>.head)>.body>.stack:has(>[data-el$="-card"])',
'.slide .stack.compact':'.slide .page:has(>.head)>.body>.stack:has(>[data-el$="-delta"])',
'.slide .group.two.compact':'.slide .page:has(>.head)>.body>.group.two:has(>[data-el]>.parts>.fig)',
'.slide .head.high':'.slide .head:has(+.body>[data-el]>.parts>[data-el$="-metric"])'
}
for a,b in replacements.items():
 assert a in s,a;s=s.replace(a,b)
p.write_text(s)
p=W/'reassemble.py';s=p.read_text();s=re.sub(r'^P\[(?:9|12|18)\]=\(P\[\d+\]\[0\],P\[\d+\]\[1\],P\[\d+\]\[2\],P\[\d+\]\[3\]\.replace\(\'class="(?:stack|group two)"\',\'class="(?:stack tight|stack compact|group two compact)"\'\)\)\n','',s,flags=re.M)
s=s.replace('{"low" if n in [12,17] else "mid" if n==18 else "" if n==9 else "center low" if n==14 else "center high" if n==11 else "center"}', '{"" if n in [9,12,17,18] else "center"}')
p.write_text(s)
p=C/'foundation/description.md';s=p.read_text().split('Shared heading variants:')[0];s+='Heading position follows the following body structure. An inline heading above comparison rows or a Venn diagram receives the deeper heading seat; an inline heading above a two-column metric grid receives the medium seat. Centered headings above labeled narrative cards use additional top space, while market charts containing a metric overlay lift the heading without changing the body. A stack of proof cards uses an 18px gap; a stack of before/after comparisons uses three 112px rows and a 28px gap; a two-column metric grid uses two 213px rows. These rules read only the existing contract structure and add no markup classes.\n';p.write_text(s)
