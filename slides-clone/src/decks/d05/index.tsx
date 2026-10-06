import { ImagePlaceholder, type DeckDefinition } from '../../ui'
import { Cond, Frame, Header, T } from './components'
import { brand, build, founders, stats, whoWeAre } from './data'

const Ph = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => <ImagePlaceholder className="absolute" style={{ left: x, top: y, width: w, height: h }} />

function Title() {
  return (
    <Frame>
      <Header left={brand.left} num="01" right={brand.right} />
      <T x={234} y={96} className="font-archivo text-[34px] font-black leading-none" style={{ transform: 'translateX(-50%) scaleX(1.25)' }}>{brand.name}</T>
      <Cond x={34} y={132} w={400} s={0.63} size={36} lh={34} align="center">{brand.tagline}</Cond>
      <T x={234} y={182} className="font-archivo text-[4.5px] font-bold" style={{ transform: 'translateX(-50%)' }}>● {brand.url}</T>
      {[0, 1, 2, 3].map((i) => <Ph key={i} x={165 + i * 35} y={219} w={34} h={34} />)}
    </Frame>
  )
}
function Founders() {
  return (
    <Frame>
      <Header left="FOUNDERS" num="03" />
      <T x={150} y={30} w={270} className="font-archivo text-[11.5px] font-extrabold leading-[13px]" style={{ textAlign: 'right' }}>{founders.heading.map((l) => <div key={l}>{l}</div>)}</T>
      <Cond x={104} y={86} w={316} s={0.62} size={25} lh={21} align="right">{founders.sub.map((l) => <div key={l}>{l}</div>)}</Cond>
      {founders.people.map((p) => (
        <div key={p.name}>
          <Ph x={p.x} y={134} w={58} h={65} />
          <Cond x={p.x + 54} y={190} w={60} s={0.6} size={28} lh={26}>{p.name}</Cond>
          <T x={p.x - 5} y={212} className="font-archivo text-[3.6px] leading-[7px]">{p.role.map((l) => <div key={l}>{l}</div>)}</T>
        </div>
      ))}
    </Frame>
  )
}
function WhoWeAre() {
  return (
    <Frame>
      <Ph x={0} y={0} w={82} h={263} />
      <Header left="WHO WE ARE" num="02" />
      <Cond x={5} y={31} w={270} s={0.64} size={27} lh={22.5}>{whoWeAre.map((l) => <div key={l}>{l}</div>)}</Cond>
      {stats.map((s) => (
        <div key={s.value}>
          <Cond x={s.x} y={s.y} w={140} s={0.72} size={75} lh={75}>{s.value}</Cond>
          <T x={s.lx} y={s.ly} className="font-archivo text-[3.6px] font-semibold">{s.label}</T>
        </div>
      ))}
      <Ph x={268} y={0} w={74} h={64} /><Ph x={322} y={33} w={71} h={80} /><Ph x={355} y={181} w={102} h={82} />
    </Frame>
  )
}
function Build() {
  return (
    <Frame>
      <Header left="WHAT WE'VE BUILD" num="04" />
      <T x={5} y={46} className="font-archivo text-[9px] font-extrabold leading-[10px]" style={{ transform: 'scaleX(1.1)', transformOrigin: 'left' }}>{build.heading.map((l) => <div key={l}>{l}</div>)}</T>
      <Cond x={5} y={72} w={330} s={0.7} size={25} lh={20.5}>{build.copy.map((l) => <div key={l}>{l}</div>)}</Cond>
      {build.cards.map((c, i) => (
        <div key={c.title}>
          <Ph x={5 + i * 116} y={163} w={113} h={93} />
          <T x={13 + i * 116} y={171} className="font-archivo text-[6px] font-extrabold">{c.title}</T>
          <T x={13 + i * 116} y={244} className="font-archivo text-[3.6px] font-semibold">{c.text}</T>
        </div>
      ))}
    </Frame>
  )
}
const deck: DeckDefinition = { id: '05', title: 'Yard', slides: [Title, Founders, WhoWeAre, Build] }
export default deck
