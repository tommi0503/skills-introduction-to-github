import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme } from './theme'
import { cover, stats, insight, impact } from './data'
import { IconDot, Logo, Meta, StatCard } from './components'

function Cover() {
  return (
    <Slide background={theme.dark} className="font-spacemono">
      <Abs x={54} y={52}><Logo /></Abs>
      <Abs x={54} y={138} className="whitespace-nowrap text-[112px] leading-[124px]" style={{ color: theme.lime }}>
        <div>{cover.title[0]}</div><div>{cover.title[1]}</div><div className="text-right">{cover.title[2]}</div>
      </Abs>
      <Abs x={875} y={166} className="font-dm text-[24px] leading-[30px] text-white">{cover.presented.map((l) => <div key={l}>{l}</div>)}</Abs>
      <Abs x={1070} y={160} className="text-[56px] leading-none text-white">(→)</Abs>
      {cover.footer.map(([k, v, x]) => (
        <Abs key={k} x={x} y={602} className="font-dm text-[24px] leading-[32px]">
          <div style={{ color: theme.lime }}>{k}</div><div className="text-white">{v}</div>
        </Abs>
      ))}
    </Slide>
  )
}

function Stats() {
  return (
    <Slide background="#fff" className="font-grotesk">
      <Meta page="002" />
      <ImagePlaceholder className="absolute" style={{ left: 0, top: 121, width: 173, height: 422 }} />
      {stats.map((s) => (
        <div key={s.value}>
          <Abs x={s.value === '432' ? 205 : 160} y={s.vy - 110} w={s.value === '432' ? 470 : 515} className="flex justify-end whitespace-nowrap text-[205px] font-bold leading-[220px]" style={{ color: theme.ink }}>
            <span>{s.value}</span><span style={{ color: theme.lime }}>+</span>
          </Abs>
          <StatCard {...s} />
        </div>
      ))}
      <Abs x={713} y={634} className="font-dm text-[17px]" style={{ color: theme.ink }}>December 2027</Abs>
      <Abs x={913} y={634} w={302} className="text-right font-dm text-[17px]" style={{ color: theme.ink }}>Source : Internal Management</Abs>
    </Slide>
  )
}

function Insight() {
  return (
    <Slide background={theme.cream} className="font-dm">
      <Meta page="004" />
      <Abs x={0} y={0} w={1280} h={560} className="bg-white" />
      <Abs x={359} y={30} className="text-[120px] font-bold leading-none" style={{ color: theme.lime }}>“</Abs>
      <Abs x={54} y={48} className="text-[40px] leading-[56px]" style={{ color: theme.ink }}>{insight.quote.map((l) => <div key={l}>{l}</div>)}</Abs>
      <ImagePlaceholder className="absolute rounded-full" style={{ left: 54, top: 372, width: 44, height: 44 }} />
      <Abs x={112} y={380} className="text-[22px]" style={{ color: theme.ink }}>{insight.author}</Abs>
      <Abs x={715} y={100} className="font-spacemono text-[135px] font-bold leading-none" style={{ color: theme.ink }}>{insight.big}</Abs>
      <ImagePlaceholder className="absolute" style={{ left: 0, top: 400, width: 1280, height: 220 }} />
      <Abs x={0} y={621} w={1280} h={2} style={{ background: theme.dark }} />
      {insight.months.map(([m, x]) => <Abs key={m} x={x - 60} y={642} w={120} className="text-center text-[22px]" style={{ color: theme.ink }}>{m}</Abs>)}
    </Slide>
  )
}

function Impact() {
  return (
    <Slide background={theme.cream} className="font-dm">
      <Abs x={0} y={0} w={1280} h={513} style={{ background: theme.lime }} />
      <Meta page="009" />
      {[524, 969].map((x) => <Abs key={x} x={x} y={0} w={1} h={513} style={{ background: theme.dark, opacity: 0.5 }} />)}
      <Abs x={54} y={72} className="whitespace-nowrap font-spacemono text-[160px] leading-[157px]" style={{ color: theme.ink }}>
        <div>{impact.title[0]}</div><div className="text-right" style={{ width: 1161 }}>{impact.title[1]}</div>
      </Abs>
      <Abs x={1015} y={136} w={200} className="text-right text-[24px]" style={{ color: theme.ink }}>{impact.year}</Abs>
      <Abs x={181} y={278} className="text-center text-[23px] leading-[32px]" style={{ color: theme.ink }}>{impact.tag.map((l) => <div key={l}>{l}</div>)}</Abs>
      {impact.cols.map((c) => (
        <div key={c.x}>
          <IconDot kind={c.icon} x={c.x} y={496} />
          <Abs x={c.x} y={572} className="text-[24px] leading-[33px]" style={{ color: theme.ink }}>{c.text.map((l) => <div key={l}>{l}</div>)}</Abs>
        </div>
      ))}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '25', title: 'Splashlink agency', slides: [Cover, Stats, Insight, Impact] }
export default deck
