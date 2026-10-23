from pathlib import Path
C=Path('/workspace/output/nightchamfer');p=Path('/workspace/work/nightchamfer/reassemble.py');t=p.read_text();t=t.replace("'<span class=\"from\">협력사</span><span class=\"to\">미리컴퍼니</span>'", "'<span class=\"from\"><b>협력사</b><small>사용자 접점·도메인</small></span><span class=\"to\"><b>미리컴퍼니</b><small>기타 인프라 지원</small></span>'")
# Response headings belong to the column head, rather than repeating inside every response cell.
t=t.replace("('정확도 검증','출처 표기·검증 단계·사용자 피드백 루프로 보완'),('수익성 확보','사용량 과금·경량 모델 병행으로 마진 확보'),('보안 인증','데이터 격리·미학습 정책·보안 인증으로 신뢰 확보')", "('','출처 표기·검증 단계·사용자 피드백 루프로 보완'),('','사용량 과금·경량 모델 병행으로 마진 확보'),('','데이터 격리·미학습 정책·보안 인증으로 신뢰 확보')")
p.write_text(t)
s='[data-el="nightchamfer-versus"]';p=C/'elements/versus/element.css';p.write_text(p.read_text()+f'''
@container (min-width:1000px) and (min-height:420px){{
{s}>.side{{position:absolute;left:188px;top:46px;width:446px;height:398px;padding:0;border:var(--stroke) solid var(--n-4);background:var(--n-1);border-radius:var(--radius);display:block}}
{s}>.side.on{{left:673px;width:calc(100% - 673px);border-color:var(--a1-4);background:var(--n-1)}}
{s}>.side>.name{{position:absolute;left:50%;top:34px;transform:translateX(-50%);width:155px;height:49px;display:flex;align-items:center;justify-content:center;padding:0;background:none;border:var(--stroke) solid var(--n-4);border-radius:999px;font-size:var(--type-22);line-height:var(--label-line);color:var(--ink)}}
{s}>.side.on>.name{{border-color:var(--a1-4);color:var(--ink)}}
{s}>.side>.list{{position:absolute;inset:0;padding:0;display:block;container-type:normal}}
{s}>.side:first-child>.list::before{{content:"";position:absolute;left:-188px;top:81px;width:163px;height:317px;border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1)}}
{s} .list>.item{{position:absolute;left:31px;right:31px;top:113px;height:102px;padding:0;min-height:0;border:0;border-radius:0;background:none;display:flex;align-items:flex-start;justify-content:center}}
{s} .list>.item:nth-child(2){{top:215px}}{s} .list>.item:nth-child(3){{top:317px;height:70px}}
{s} .list>.item+.item{{border-top:1px dotted var(--n-4)}}
{s} .list>.item>.name{{position:absolute;left:-219px;top:0;width:163px;min-height:0;height:54px;display:flex;align-items:center;justify-content:center;flex:none;padding:0;background:none;color:var(--ink);font-size:var(--type-22);line-height:var(--label-line);font-weight:var(--name-weight)}}
{s} .side.on .list>.item>.name:empty{{display:none}}
{s} .list>.item>.note{{padding-top:7px;margin:0;font-size:var(--type-18);line-height:var(--lead-line);text-align:center;color:var(--n-7);flex:none;max-width:100%}}
{s}>.vs{{position:absolute;left:632px;top:254px;width:56px;height:60px;color:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);font-size:var(--type-48)}}
{s}>.vs::before{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--a1-4),var(--a1));clip-path:polygon(0 25%,66% 25%,66% 0,100% 50%,66% 100%,66% 75%,0 75%)}}
}}
''')
s='[data-el="nightchamfer-delta"]';p=C/'elements/delta/element.css';p.write_text(p.read_text()+f'''
@container (min-width:900px) and (min-height:280px){{
{s}>.from,{s}>.to{{position:absolute;left:105px;top:34px;width:258px;height:258px;max-width:none;max-height:none;aspect-ratio:1;border:26px solid var(--n-3);border-radius:50%;background:linear-gradient(120deg,var(--ink),var(--a1-9));color:var(--page);font-size:var(--type-32);font-weight:var(--name-weight);display:flex;align-items:center;justify-content:center}}
{s}>.to{{left:740px;border-color:var(--a1-2-muted);background:linear-gradient(135deg,var(--a1-5),var(--a1-4));color:var(--ink)}}
{s}>.from>small,{s}>.to>small{{position:absolute;left:337px;top:2px;width:220px;font-size:var(--type-20);font-weight:var(--body-weight);line-height:var(--body-line);color:var(--n-7);text-align:left}}
{s}>.to>small{{left:-278px;top:179px}}
{s}::before{{content:"";position:absolute;left:413px;top:91px;width:274px;height:78px;background:linear-gradient(90deg,var(--a2),color-mix(in srgb,var(--page) 0%,var(--ink) .001%));clip-path:polygon(0 50%,14.6% 0,14.6% 28%,100% 28%,100% 72%,14.6% 72%,14.6% 100%)}}
{s}::after{{content:"";position:absolute;left:413px;top:157px;width:274px;height:78px;background:linear-gradient(90deg,color-mix(in srgb,var(--page) 0%,var(--ink) .001%),var(--a1-9));clip-path:polygon(0 28%,85.4% 28%,85.4% 0,100% 50%,85.4% 100%,85.4% 72%,0 72%)}}
}}
''')
p=C/'elements/callout/element.css';s='[data-el="nightchamfer-callout"]';p.write_text(p.read_text()+f'\n{s}:has(>p>b:nth-of-type(2))::before{{inset:9px 15px 15px 3px}}{s}:has(>p>b:nth-of-type(2))>p{{font-weight:var(--body-weight)}}{s}:has(>p>b:nth-of-type(2))>p>b{{color:var(--ink)}}\n')
