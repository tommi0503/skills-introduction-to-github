import { ImagePlaceholder, type DeckDefinition } from '../../ui'
import { Frame, Logo, Nav, T } from './components'
import { about, hero, solution } from './data'
import { theme } from './theme'

const Ph = ({ x, y, w, h, r = 0, tone }: { x: number; y: number; w: number; h: number; r?: number; tone?: string }) => (
  <ImagePlaceholder tone={tone} className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: r }} />
)

function Hero() {
  return (
    <Frame k={3.35} bg={theme.dark}>
      <Ph x={0} y={0} w={382} h={213} tone="#171917" />
      <Logo x={5} y={7} color="#fff" />
      <Nav y={9} color="#fff" xs={[108, 0]} page={{ x: 233, t: 'Marketing Deck' }} />
      <T x={340} y={9} className="text-[4px] text-white">©2025</T>
      <T x={16} y={108} className="flex h-[13px] w-[85px] items-center gap-1 rounded-full bg-[#2b2d2b] pl-1 text-[5px] text-white">
        <span className="h-[7px] w-[7px] rounded-full" style={{ background: theme.lime }} />{hero.pill}
      </T>
      <T x={16} y={128} className="text-[24px] font-medium leading-[27px] tracking-[-0.4px] text-white">{hero.title.map((l) => <div key={l}>{l}</div>)}</T>
      <T x={16} y={192} className="text-[4px] text-[#aaa]">{hero.footer}</T>
    </Frame>
  )
}
function Solution() {
  return (
    <Frame k={3.35} bg="#fff">
      <Logo x={5} y={7} color="#000" />
      <Nav y={9} color="#000" xs={[104, 0]} page={{ x: 239, t: 'Solution' }} />
      <T x={13} y={33} className="whitespace-nowrap text-[13.5px] font-medium leading-[19px] tracking-[-0.3px]">{solution.lines.map((l) => <div key={l}>{l}</div>)}</T>
      <T x={13} y={122} className="text-[4px]">{solution.caption}</T>
      <Ph x={13} y={134} w={107} h={61} r={3} />
      <T x={20} y={186} className="rounded-[3px] px-2 py-[2px] text-[4px] font-medium" style={{ background: theme.lime }}>{solution.badge}</T>
      <T x={146} y={112} className="whitespace-nowrap text-[76px] font-medium leading-none tracking-[-3px]">{solution.stat}</T>
    </Frame>
  )
}
function About() {
  const { lines, columns, filled, total } = about
  return (
    <Frame k={2.41} bg={theme.dark}>
      <Logo x={16} y={9} color="#fff" />
      <Nav y={11} color="#fff" xs={[270, 0]} page={{ x: 342, t: 'About Us' }} />
      <T x={502} y={11} className="text-[4px] text-white">02</T>
      <Ph x={16} y={55} w={160} h={226} r={3} tone="#252725" />
      <T x={205} y={54} className="whitespace-nowrap text-[10.5px] font-medium leading-[15px] text-white">{lines.map((l) => <div key={l}>{l}</div>)}</T>
      <div className="absolute rounded-full" style={{ left: 205, top: 162, width: 303, height: 45, background: theme.card }} />
      {Array.from({ length: total }, (_, i) => (
        <div key={i} className="absolute rounded-full" style={{ left: 212 + i * 24.4, top: 169, width: 17, height: 31, background: i < filled ? theme.lime : theme.grey }} />
      ))}
      <div className="absolute" style={{ left: 205, top: 224, width: 303, height: 0.6, background: '#333' }} />
      {columns.map((c, i) => (
        <T key={c.title} x={205 + i * 109} y={244} w={100}>
          <div className="text-[5.5px] text-white">{c.title}</div>
          <div className="mt-[5px] text-[4.8px] leading-[7px]" style={{ color: theme.muted }}>{c.body}</div>
        </T>
      ))}
    </Frame>
  )
}
function Dashboard() {
  return (
    <Frame k={2.41} bg={theme.dark}>
      <Ph x={0} y={0} w={531} h={299} tone="#1f2220" />
      <Logo x={16} y={9} color="#fff" />
      <Nav y={11} color="#fff" xs={[62, 0]} />
      <Ph x={41} y={47} w={200} h={260} r={26} tone="#2c2f2c" />
    </Frame>
  )
}
const deck: DeckDefinition = { id: '06', title: 'Stroom', slides: [Hero, Solution, About, Dashboard] }
export default deck
