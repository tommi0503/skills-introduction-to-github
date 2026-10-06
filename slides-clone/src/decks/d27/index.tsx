import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { Check } from 'lucide-react'
import { theme } from './theme'
import { cover, intro, curation, menu, flow, welfare, benefit } from './data'
import { ArrowDot, Brand, Circle, Footer, Label, Lines, Menu } from './components'

const F = 'font-pretendard'

function Cover() {
  return (
    <Slide className={F}>
      <ImagePlaceholder className="absolute" tone={theme.cover} style={{ left: 0, top: 0, width: 1280, height: 658 }} />
      <ImagePlaceholder className="absolute rounded-[48px]" style={{ left: 908, top: 270, width: 293, height: 288 }} />
      <Abs x={51} y={52} className="text-[15px] text-white/90">{cover.sub}</Abs>
      <Abs x={51} y={80} className="text-[40px] font-bold leading-[56px] text-white"><Lines lines={cover.title} /></Abs>
      <Abs x={51} y={560} className="text-[14px] leading-[24px] text-white/90"><Lines lines={cover.contact} /></Abs>
      <Abs x={51} y={676}><Brand /></Abs>
      <Abs x={929} y={677} w={300} className="text-right text-[14px] font-semibold">{cover.url}</Abs>
    </Slide>
  )
}

function Intro() {
  const c = intro.chart
  return (
    <Slide className={F}>
      <Label>{intro.label}</Label>
      <Abs x={113} y={197} className="text-[32px] font-medium leading-[52px]">
        <div>{intro.lead[0]}</div><div><b style={{ color: theme.blueText }}>{intro.accent}</b>{intro.tail}</div><div>{intro.last}</div>
      </Abs>
      <Abs x={697} y={95} className="text-[13px] font-bold">{c.title}</Abs>
      {c.bars.map((b, i) => (
        <Abs key={i} x={b.x} y={400 - b.h} w={44} h={b.h} style={{ background: i === 3 ? 'linear-gradient(#2b59e0,#8a4be0)' : '#e5e7eb' }} />
      ))}
      <Abs x={698} y={400} w={480} h={1} className="bg-[#ddd]" />
      <Abs x={698} y={265} w={117} h={41} className="flex items-center justify-center rounded-md bg-[#e5e7eb] text-[22px] font-bold text-white">{c.from}</Abs>
      <Abs x={1048} y={96} w={140} h={47} className="flex items-center justify-center rounded-md text-[24px] font-bold text-white" style={{ background: theme.blue }}>{c.to}</Abs>
      <Abs x={730} y={410} className="text-[10px] text-[#999]">{c.years[0]}</Abs><Abs x={1100} y={410} className="text-[10px] text-[#999]">{c.years[1]}</Abs>
      <Abs x={0} y={475} w={1280} h={166} style={{ background: theme.band }} />
      {intro.stats.map(([k, v], i) => (
        <Abs key={k} x={[279, 611, 972][i] - 150} y={512} w={300} className="text-center">
          <div className="text-[15px] font-semibold">{k}</div>
          <div className="mt-2 text-[38px] font-bold" style={{ color: theme.blue }}>{v}<span className="text-[20px]">이상</span></div>
        </Abs>
      ))}
      {[440, 780].map((x) => <Abs key={x} x={x} y={520} w={1} h={90} className="bg-[#d5e0f2]" />)}
      <Footer />
    </Slide>
  )
}

function Curation() {
  return (
    <Slide className={F}>
      <Label>{curation.label}</Label>
      <Abs x={84} y={120} className="text-[19px] leading-[32px]"><div>{curation.lines[0]}</div><div className="font-bold">{curation.lines[1]}</div></Abs>
      <Abs x={934} y={122} w={275} h={75} className="flex items-center justify-center rounded-lg text-center text-[12px] leading-[19px] text-white" style={{ background: theme.blue }}><Lines lines={curation.callout} /></Abs>
      <Abs x={1070} y={197} w={2} h={426} style={{ background: theme.line }} />
      <Abs x={286 * 0} y={220} w={1280} h={403} className="overflow-hidden">
        <div className="absolute rounded-full" style={{ left: 1072 - 400, top: 403 - 400, width: 800, height: 800, background: '#eef4fd', boxShadow: 'inset 0 0 0 2px #d3e2f8' }} />
        <div className="absolute rounded-full" style={{ left: 1072 - 155, top: 403 - 155, width: 310, height: 310, background: '#fff', boxShadow: 'inset 0 0 0 2px #7aa7ee' }} />
      </Abs>
      <ImagePlaceholder className="absolute" style={{ left: 0, top: 379, width: 560, height: 129 }} />
      <ImagePlaceholder className="absolute" style={{ left: 1150, top: 379, width: 130, height: 129 }} />
      <Abs x={560} y={370} className="text-[26px] font-semibold" style={{ color: theme.blue }}>AIR KLASS</Abs>
      <Abs x={900} y={445} className="text-[12px] leading-[17px] text-[#333]"><Lines lines={curation.b2c} /></Abs>
      <Abs x={1010} y={535}><Brand size={20} /></Abs>
      <Abs x={0} y={623} w={1280} h={2} style={{ background: theme.line }} />
      {[429, 674, 915, 1228].map((x) => <Abs key={x} x={x - 4} y={619} w={9} h={9} className="rounded-full" style={{ background: theme.blue }} />)}
      <Footer />
    </Slide>
  )
}

function Flow() {
  return (
    <Slide background={theme.soft} className={F}>
      <Label>{flow.label}</Label>
      <Menu items={menu} active={0} y={118} />
      {flow.boxes.map(([h, t], i) => (
        <Abs key={h} x={[318, 627, 936][i]} y={157} w={293} h={94} className="rounded-xl border border-[#b7cdf3] bg-white text-center shadow-sm">
          <div className="mt-3 text-[14px] font-bold" style={{ color: theme.blue }}>{h}</div>
          <Lines lines={t} className="mt-2 text-[14px] leading-[20px]" />
        </Abs>
      ))}
      <ArrowDot x={620} y={204} /><ArrowDot x={928} y={204} />
      <ImagePlaceholder className="absolute rounded-md" style={{ left: 567, top: 340, width: 414, height: 286 }} />
      <Abs x={567} y={450} w={414} className="text-center text-[17px] font-bold">{flow.site}</Abs>
      <Circle x={480} y={484} r={116} lines={flow.left} /><Circle x={1069} y={484} r={116} lines={flow.right} />
      <Footer />
    </Slide>
  )
}

function Welfare() {
  return (
    <Slide background={theme.soft} className={F}>
      <Label>{welfare.label}</Label>
      <Menu items={menu} active={2} y={118} />
      <Abs x={320} y={118} className="text-[17px] leading-[30px]"><Lines lines={welfare.desc} /></Abs>
      {welfare.cards.map((c, i) => (
        <Abs key={c.t} x={[320, 629, 938][i]} y={215} w={291} h={253} className="rounded-2xl border border-[#b7cdf3] bg-white text-center">
          <ImagePlaceholder className="mx-auto mt-5 h-[80px] w-[130px]" />
          <div className="mt-4 text-[16px] font-bold" style={{ color: theme.blue }}>{c.t}</div>
          <Lines lines={c.d} className="mt-3 text-[13px] leading-[21px] text-[#555]" />
        </Abs>
      ))}
      <Abs x={320} y={505} w={909} className="border-t border-dashed border-[#b7cdf3]" />
      {welfare.steps.map((s, i) => (
        <Abs key={i} x={[320, 629, 938][i]} y={543} w={291} h={114} className="flex flex-col items-center justify-center rounded-xl text-center text-[15px] font-bold leading-[24px] text-white" style={{ background: theme.blue }}>
          <Check size={18} /><Lines lines={s} />
        </Abs>
      ))}
      <ArrowDot x={620} y={600} white /><ArrowDot x={925} y={600} white />
      <Footer />
    </Slide>
  )
}

function Benefit() {
  return (
    <Slide background={theme.soft} className={F}>
      <Label>{benefit.label}</Label>
      <Abs x={0} y={100} w={1334} className="text-center text-[24px] font-bold leading-[36px]">
        <div>{benefit.title[0]}</div><div style={{ color: theme.blueText }}>{benefit.accent}</div><div>{benefit.last}</div>
      </Abs>
      {benefit.cards.map((c, i) => (
        <Abs key={c.n} x={52 + i * 239.3} y={257} w={216} h={372} className="rounded-xl bg-white shadow-[0_2px_14px_rgba(40,80,160,0.12)]">
          <div className="mx-4 mt-4 flex h-[88px] flex-col items-center justify-center gap-2 rounded-md" style={{ background: theme.band }}>
            <span className="flex size-[22px] items-center justify-center rounded-full text-[12px] font-bold text-white" style={{ background: theme.blue }}>{c.n}</span>
            <span className="text-[15px] font-bold" style={{ color: theme.blueText }}>{c.t}</span>
          </div>
          {c.rows.map(([k, v]) => (
            <div key={k} className="mt-5 text-center">
              <div className="text-[14px] font-bold">{k}</div>
              <Lines lines={v} className="mt-1 text-[13px] leading-[18px] text-[#555]" />
            </div>
          ))}
        </Abs>
      ))}
      <Footer />
    </Slide>
  )
}

const deck: DeckDefinition = { id: '27', title: '에어클래스 비즈니스', slides: [Cover, Intro, Curation, Flow, Welfare, Benefit] }
export default deck
