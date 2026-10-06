import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme as t } from './theme'
import { stats, countries, therapy, company, app, points } from './data'
import { Circle, Desc, Header, Lines, Title } from './components'

const F = 'font-pretendard'
const BG = t.bg

function Cover() {
  return (
    <Slide background="#fff" className={F}>
      <ImagePlaceholder className="absolute" tone="#e0818b" style={{ left: 0, top: 0, width: 1280, height: 656 }} />
      <ImagePlaceholder className="absolute rounded-full" tone="#f0a9b0" style={{ left: 579, top: 192, width: 126, height: 126 }} />
      <Abs x={0} y={338} w={1280} className="text-center text-[62px] font-light leading-none text-white">약손명가</Abs>
      <Abs x={0} y={430} w={1280} className="text-center text-[40px] font-light leading-none text-white">헬스케어</Abs>
      <Abs x={51} y={678} className="text-[14px] font-bold">약손명가 헬스케어 회사소개서</Abs>
      <Abs x={929} y={679} w={300} className="text-right text-[13px]" style={{ color: t.coral }}>www.yaksonhouse.com</Abs>
    </Slide>
  )
}

function Data() {
  return (
    <Slide background={BG} className={F}>
      <Header page="PAGE 03" />
      <ImagePlaceholder className="absolute" style={{ left: 1030, top: 130, width: 220, height: 220 }} />
      <Abs x={84} y={156} className="text-[14px]" style={{ color: t.coral }}>KOREA NOLTOTAL TERAHPY COMPANY</Abs>
      <Title y={198}>데이터로 확인하는 빛채</Title>
      <Desc y={262} lines={['1979년부터 45년간 약 41만명 이상의 고객들을 접하고', '높은 재구매율을 보여주고 있습니다.']} />
      {stats.map(([a, b, v], i) => (
        <Abs key={a} x={84 + i * 220.5} y={387} w={208} h={208} className="text-white" style={{ background: t.coral }}>
          <div className="px-4 pt-4 text-[15px] font-semibold">{a}</div>
          <div className="px-4 pt-1 text-[14px] text-white/70">{b}</div>
          <div className="absolute inset-x-4 top-[70px] h-px bg-white/30" />
          <div className="absolute bottom-3 right-4 text-[48px] font-medium leading-none">{v}</div>
        </Abs>
      ))}
      <Abs x={987} y={477} w={210} h={118} className="border bg-white p-3 text-center" style={{ borderColor: t.line }}>
        <div className="text-[13px] font-bold">해외 6개 국가 진출</div>
        <div className="mt-2 flex flex-wrap justify-center gap-1">{countries.map((c) => <span key={c} className="rounded-sm px-1.5 text-[14px]" style={{ background: t.pinkSoft, color: t.coral }}>{c}</span>)}</div>
      </Abs>
    </Slide>
  )
}

function Therapy() {
  return (
    <Slide background={BG} className={F}>
      <Header page="PAGE 04" />
      <Title y={138}>{therapy.title}</Title>
      <Desc y={192} lines={therapy.desc} />
      <Abs x={84} y={274} className="text-[13px]" style={{ color: t.coral }}>{therapy.note}</Abs>
      <ImagePlaceholder className="absolute rounded-tr-[110px]" style={{ left: 0, top: 360, width: 670, height: 360 }} />
      {[859, 1096].map((x) => <Abs key={x} x={x - 70} y={190} w={140} h={270} className="rounded-full" style={{ background: t.pinkSoft, opacity: 0.6 }} />)}
      {therapy.top.map(([en, k, x]) => (
        <Circle key={k} x={x} y={227} r={72} className="bg-white shadow-[0_2px_12px_rgba(220,110,124,0.2)]"><div className="text-[9px]" style={{ color: t.coral }}>{en}</div><div className="text-[16px] font-bold">{k}</div></Circle>
      ))}
      {therapy.bottom.map(([k, x]) => <Circle key={k} x={x} y={414} r={72} className="bg-white text-[16px] font-bold" style={{ color: t.coral, boxShadow: `inset 0 0 0 1px ${t.line}` }}>{k}</Circle>)}
      <Abs x={968} y={308} className="text-[22px]" style={{ color: t.line }}>+</Abs>
      {therapy.tags.map(([x, w, l]) => <Abs key={l} x={x} y={576} w={w} h={42} className="flex items-center justify-center text-[14px] font-semibold text-white" style={{ background: t.coral }}>{l}</Abs>)}
    </Slide>
  )
}

function Company() {
  return (
    <Slide background={BG} className={F}>
      <Header page="PAGE 05" />
      <Title y={138}>{company.title}</Title>
      <Desc y={192} lines={company.desc} />
      <Circle x={640} y={248} r={91} className="bg-white shadow-[0_2px_16px_rgba(220,110,124,0.2)]"><ImagePlaceholder className="size-[56px] rounded-full" tone={t.logoTone} /><div className="mt-1 text-[16px] font-bold" style={{ color: t.coral }}>약손명가</div><div className="text-[14px]">헬스케어</div></Circle>
      {company.cols.map((c) => (
        <div key={c.head}>
          <Abs x={c.x} y={455} w={343} h={40} className="flex items-center justify-center text-[14px] font-semibold text-white" style={{ background: t.coral }}>{c.head}</Abs>
          {c.subs.map((s, i) => (
            <Abs key={s} x={c.x + i * (343 / c.subs.length) + 2} y={511} w={343 / c.subs.length - 4} h={40} className="flex items-center justify-center text-[14px]" style={{ background: t.pinkSoft, color: t.coral }}>{s}</Abs>
          ))}
          {c.descs.map((d, i) => <Abs key={i} x={c.x + i * (343 / c.descs.length) + 6} y={570} className="text-[14px] leading-[15px] text-[#555]"><Lines lines={d} /></Abs>)}
        </div>
      ))}
    </Slide>
  )
}

function App() {
  return (
    <Slide background={BG} className={F}>
      <Header left="약손명가 헬스케어" page="PAGE 16" />
      <Title center y={96}>{app.title}</Title>
      <Desc center y={157} lines={app.desc} />
      {app.shops.map((s, i) => (
        <Abs key={s} x={84} y={350 + i * 86} w={337} h={77} className="flex items-center gap-4 bg-white px-4 shadow-sm">
          <ImagePlaceholder className="h-[22px] w-[60px]" /><span className="text-[14px] font-semibold">{s}</span>
        </Abs>
      ))}
      <ImagePlaceholder className="absolute rounded-t-[40px]" style={{ left: 509, top: 266, width: 262, height: 454 }} />
      <Abs x={790} y={455} w={72} h={44} style={{ background: t.pinkSoft, clipPath: 'polygon(0 20%,60% 20%,60% 0,100% 50%,60% 100%,60% 80%,0 80%)' }} />
      <Circle x={1027} y={476} r={140} className="text-white" style={{ background: t.coral }}>
        <ImagePlaceholder className="size-[44px] rounded-full" tone={t.logoTone} /><div className="mt-2 text-[24px] leading-[28px]">약손명가<br />헬스케어</div>
      </Circle>
      <Abs x={893} y={535} w={267} h={38} className="flex items-center justify-center rounded-full bg-white text-[15px] font-semibold" style={{ color: t.coral }}>{app.pill}</Abs>
    </Slide>
  )
}

function Points() {
  return (
    <Slide background={BG} className={F}>
      <Header left="약손명가 헬스케어" page="PAGE 17" />
      <Title y={138}>{points.title}</Title>
      <Circle x={157} y={421} r={73} className="text-[16px] font-semibold leading-[22px] text-white" style={{ background: t.coral }}>APP<br />가입 고객</Circle>
      <Abs x={365} y={308} className="text-[13px]" style={{ color: t.coral }}>B2C</Abs><Abs x={365} y={510} className="text-[13px]" style={{ color: t.coral }}>B2B</Abs>
      {points.mids.map((m) => (
        <div key={m.y}>
          <Circle x={554} y={m.y} r={75} className="bg-white text-[14px] leading-[20px]" style={{ color: t.coral, boxShadow: `inset 0 0 0 1px ${t.coral}` }}><Lines lines={m.t} /></Circle>
          {m.above && <Abs x={444} y={m.y - 120} w={220} className="text-center text-[14px] leading-[16px] text-[#555]"><Lines lines={m.above} /></Abs>}
          {m.below && <Abs x={444} y={m.y + 85} w={220} className="text-center text-[14px] leading-[16px] text-[#555]"><Lines lines={m.below} /></Abs>}
        </div>
      ))}
      <Abs x={862} y={178} w={158} h={481} className="rounded-full border" style={{ background: '#fceef0', borderColor: t.line }} />
      <Abs x={862} y={147} w={158} className="text-center text-[13px]" style={{ color: t.coral }}>POINT 사용처</Abs>
      {points.uses.map(([a, b, c], i) => (
        <div key={a}>
          <Circle x={941} y={[257, 418, 581][i]} r={64} className="bg-[#f9dde0] text-[15px] font-bold leading-[20px]"><div>{a}</div><div>{b}</div></Circle>
          <Abs x={1039} y={[238, 400, 563][i]} w={190} className="text-[14px] leading-[16px] text-[#555]">{c}</Abs>
        </div>
      ))}
      <Abs x={84} y={640} className="text-[14px] text-[#666]">{points.note}</Abs>
    </Slide>
  )
}

const deck: DeckDefinition = { id: '29', title: '약손명가 헬스케어', slides: [Cover, Data, Therapy, Company, App, Points] }
export default deck
