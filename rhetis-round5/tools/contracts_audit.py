"""Round5 supersedes the historical closed-class/full56 audit. See source-contract-audit."""
import argparse,json
from audit import run,ROOT
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('--partial',action='store_true');v=a.parse_args();r=run(v.collection,v.partial);p=ROOT/'integration-contracts';p.mkdir(exist_ok=True);(p/(v.collection+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2))
