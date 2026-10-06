import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme as t } from './theme'
import { cover, diff, program, results, self, healing } from './data'
import { BigHeart, Head, Lines, Logo, Panel, PanelTitle, Tag } from './components'

const F = 'font-pretendard'

function Cover() {
  return (
    <Slide background={t.cover} className={F}>
      <Logo y={60} />
      <Abs x={62} y={60} className="text-[54px] font-bold leading-[74px]"><div>{cover.title}</div><div style={{ color: t.green }}>{cover.brand}</div></Abs>
      <Abs x={62} y={203} w={345} h={69} className="flex items-center justify-center rounded-xl text-[40px] font-bold text-white" style={{ background: t.green }}>{cover.badge}</Abs>
      <ImagePlaceholder className="absolute" style={{ left: 690, top: 313, width: 517, height: 336 }} />
      <Abs x={62} y={610} className="text-[16px] leading-[32px]"><Lines lines={cover.date} /></Abs>
    </Slide>
  )
}

function Diff() {
  return (
    <Slide className={F}>
      <Head crumb={diff.crumb} title={diff.title} />
      <Abs x={0} y={141} w={1280} h={167} style={{ background: t.beige }} />
      {[426, 852].map((x) => <Abs key={x} x={x} y={141} w={1} h={167} className="bg-white" />)}
      {diff.cols.map(([x, l], i) => (
        <Abs key={x} x={x - 200} y={176} w={400} className="text-center">
          <span className="mx-auto mb-3 flex size-[22px] items-center justify-center rounded-full text-[14px] font-bold text-white" style={{ background: t.green }}>{i + 1}</span>
          <Lines lines={l} className="text-[20px] font-medium leading-[34px]" />
        </Abs>
      ))}
      <Abs x={47} y={391} w={241} h={236} className="flex flex-col items-center justify-end rounded-[60px] pb-[34px] text-center text-white" style={{ background: t.mid }}>
        <div className="text-[30px] font-bold">{diff.blob[0]}</div>
        <Lines lines={diff.blob.slice(1)} className="mt-1 text-[13px] leading-[22px]" />
      </Abs>
      <ImagePlaceholder className="absolute" style={{ left: 124, top: 377, width: 95, height: 80 }} />
      {diff.roles.map(([a, b, y, d]) => (
        <div key={a}>
          <Abs x={431} y={y} w={185} h={105} className="flex flex-col items-center justify-center rounded-xl border-2 bg-white text-center font-bold" style={{ borderColor: t.green, color: t.green }}>
            <div className="text-[25px]">{a}</div><div className="text-[17px]">{b}</div>
          </Abs>
          <Abs x={621} y={y} w={314} h={105} className="flex items-center rounded-xl px-5 text-[14px] leading-[22px] text-[#555]" style={{ background: t.light }}><Lines lines={d} /></Abs>
        </div>
      ))}
      {diff.side.map(([a, b, x, y]) => <Abs key={a} x={x} y={y} className="text-[13px] leading-[19px] text-[#555]"><div>{a}</div><div>{b}</div></Abs>)}
      <Abs x={1111 - 121} y={508 - 121} w={242} h={242} className="flex flex-col items-center justify-center rounded-full px-6 text-center text-white" style={{ background: t.green }}>
        <div className="text-[23px] font-bold leading-[31px]">{diff.org[0]}<br />{diff.org[1]}</div>
        <Lines lines={diff.org.slice(2)} className="mt-2 text-[13px] leading-[19px]" />
      </Abs>
      <Abs x={995} y={352} className="text-[13px] text-[#555]">양육 코칭</Abs><Abs x={985} y={654} className="text-[13px] text-[#555]">프로그램 코칭</Abs>
    </Slide>
  )
}

function Program() {
  return (
    <Slide className={F}>
      <Head crumb={'Ⅲ. ' + '“내가 디자인하는 My Life Map”은?'} title={program.title} />
      <Abs x={55} y={264} w={276} h={276} className="flex flex-col items-center rounded-full pt-[100px] text-center text-white" style={{ background: t.green }}>
        <Lines lines={program.circle} className="text-[28px] font-bold leading-[38px]" />
      </Abs>
      <ImagePlaceholder className="absolute rounded-full" style={{ left: 138, top: 478, width: 114, height: 108 }} />
      {program.rows.map((r) => (
        <div key={r.y}>
          <Tag x={483} y={r.y - 6} solid={r.tag === '필수활동'}>{r.tag}</Tag>
          <Abs x={493} y={r.y} w={295} h={110} className="flex items-center gap-4 rounded-xl px-6" style={{ background: t.light }}>
            <ImagePlaceholder className="size-[44px] rounded-md" />
            <Lines lines={r.name} className="text-[24px] font-bold leading-[32px]" />
          </Abs>
          <Abs x={854} y={r.y + 22} className="text-[14px] leading-[23px] text-[#666]"><Lines lines={r.desc} /></Abs>
        </div>
      ))}
    </Slide>
  )
}

function Results() {
  const r = results
  return (
    <Slide background={t.band} className={F}>
      <Head crumb={r.crumb} title={r.title} white />
      {r.top.map(([a, b, n, u], i) => (
        <Abs key={a} x={[52, 347, 643, 942][i]} y={140} w={287} h={172} className="rounded-2xl bg-white">
          <div className="px-5 pt-5 text-[17px] font-semibold">{a}</div><div className="px-5 text-[12px] text-[#999]">{b}</div>
          <ImagePlaceholder className="absolute right-5 top-5 size-[40px] rounded-md" />
          <div className="absolute bottom-4 right-5 text-[48px] font-bold leading-none" style={{ color: t.green }}>{n}<span className="text-[22px]">{u}</span></div>
        </Abs>
      ))}
      <Abs x={52} y={322} w={287} h={170} className="rounded-2xl bg-white">
        <div className="px-5 pt-5 text-[17px] font-semibold">{r.total[0]}</div><div className="px-5 text-[13px] text-[#999]">{r.total[1]}</div>
        <div className="absolute bottom-4 right-5 text-[48px] font-bold leading-none" style={{ color: t.orange }}>{r.total[2]}<span className="text-[22px]">{r.total[3]}</span></div>
      </Abs>
      <Abs x={347} y={322} w={882} h={170} className="rounded-2xl bg-white" />
      {r.trio.map(([a, n, u, cx]) => (
        <Abs key={a} x={cx - 140} y={340} w={280} className="text-center">
          <div className="text-[17px] font-semibold">{a}</div>
          <div className="mt-[44px] text-[48px] font-bold leading-none" style={{ color: t.green }}>{n}<span className="text-[22px]">{u}</span></div>
        </Abs>
      ))}
      {[642, 935].map((x, i) => <Abs key={x} x={x - 8} y={392} className="text-[26px] text-[#aaa]">{i ? '=' : '+'}</Abs>)}
      <Abs x={645} y={500} w={584} h={171} className="rounded-2xl text-white" style={{ background: t.teal }}>
        <div className="px-6 pt-6 text-[17px] font-semibold">● {r.budget.label}</div>
        <div className="absolute bottom-5 right-6 text-[46px] font-bold leading-none">{r.budget.value}</div>
      </Abs>
      <ImagePlaceholder className="absolute" style={{ left: 607, top: 570, width: 70, height: 60 }} />
    </Slide>
  )
}

function SelfRun() {
  return (
    <Slide className={F}>
      <Head crumb={diff.crumb} title={<><span className="text-[#aaa]">3) </span>{self.title}</>} dim />
      <Panel x={55} w={569}>
        <PanelTitle lines={self.left} />
        <Abs x={48} y={175} w={159} h={159} className="flex items-center justify-center rounded-full bg-[#e6e6e6] text-center text-[18px] text-[#aaa]">{self.from}</Abs>
        <Abs x={314 - 55 - 79 + 55 - 55} y={175} w={159} h={159} className="flex items-center justify-center rounded-full text-center text-[19px] font-semibold text-white" style={{ background: t.green, left: 340 }}>{self.to}</Abs>
        {self.labels.map((l, i) => <Abs key={l} x={48} y={335 + i * 52} className="text-[17px] text-[#aaa]">{l}</Abs>)}
        {self.pills.map((l, i) => <Abs key={l} x={300} y={323 + i * 52} w={236} h={44} className="flex items-center justify-center rounded-lg border bg-white text-[17px]" style={{ borderColor: t.mid, color: t.sub }}>{l}</Abs>)}
      </Panel>
      <Panel x={656} w={572}>
        <PanelTitle lines={self.right} />
        {self.cells.map((c, i) => (
          <Abs key={i} x={31 + (i % 2) * 262} y={125 + Math.floor(i / 2) * 182} w={250} h={165} className="text-center">
            <ImagePlaceholder className="mx-auto h-[100px] w-[140px] rounded-md" />
            <Lines lines={c} className="mt-3 text-[14px] leading-[22px] text-[#666]" />
          </Abs>
        ))}
      </Panel>
    </Slide>
  )
}

function Healing() {
  const h = healing
  return (
    <Slide className={F}>
      <Head crumb={diff.crumb} title={<><span className="text-[#aaa]">3) </span>{h.title}</>} dim />
      <Panel x={52} w={573}>
        <PanelTitle lines={h.left} />
        <Lines lines={h.survey} className="mt-[40px] text-center text-[17px] leading-[31px] text-[#555]" />
      </Panel>
      <BigHeart x={122} y={400} size={280} fill={t.mid}><div className="text-[48px] font-bold">{h.big[0]}</div><div className="text-[18px]">{h.big[1]}</div></BigHeart>
      <BigHeart x={357} y={466} size={200} fill="#a5d9bd"><div className="text-[34px] font-bold">{h.small[0]}</div><div className="text-[16px]">{h.small[1]}</div></BigHeart>
      <Panel x={650} w={578}>
        <PanelTitle lines={h.right} />
        <Lines lines={h.body} className="mt-[40px] text-center text-[14px] leading-[26px] text-[#666]" />
        {h.chats.map((c, i) => (
          <Abs key={i} x={i ? 60 : 24} y={i ? 342 : 240} w={470} h={i ? 90 : 72} className="rounded-xl bg-white/80 px-6 py-3 text-[14px] leading-[23px] text-[#777]">{c}</Abs>
        ))}
        <ImagePlaceholder className="absolute size-[44px] rounded-full" style={{ left: 505, top: 232 }} />
        <ImagePlaceholder className="absolute size-[44px] rounded-full" style={{ left: 10, top: 390 }} />
      </Panel>
    </Slide>
  )
}

const deck: DeckDefinition = { id: '32', title: '초록우산 My Life Map', slides: [Cover, Diff, Program, Results, SelfRun, Healing] }
export default deck
