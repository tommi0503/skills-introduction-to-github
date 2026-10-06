import { ImagePlaceholder, type DeckDefinition } from '../../ui'
import { Frame, InfoCard, Pill, T } from './components'
import { contacts, journey, market, roadmap } from './data'
import { theme } from './theme'

const Ph = ({ x, y, w, h, r = 3, tone }: { x: number; y: number; w: number; h: number; r?: number; tone?: string }) => (
  <ImagePlaceholder tone={tone} className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: r }} />
)
const cols = [6, 68, 136, 207, 274]

function Roadmap() {
  return (
    <Frame>
      <Ph x={0} y={0} w={346} h={194} r={0} tone={theme.orange} />
      <T x={10} y={10} className="text-[11px] font-medium text-white">Road map</T>
      {roadmap.map((c, i) => (
        <div key={c.date}>
          <Pill x={cols[i]} y={46} solid={i === 0}>{c.date}</Pill>
          <T x={cols[i]} y={64} className="text-[5.5px] text-white">MAU</T>
          <T x={cols[i]} y={72} className="text-[11px] font-medium text-white">{c.mau}</T>
          <T x={cols[i]} y={86} className="text-[5.5px] text-white">Users</T>
          <T x={cols[i]} y={95} className="text-[11px] font-medium text-white">{c.users}</T>
          <T x={cols[i]} y={116} w={1} h={5} style={{ background: '#fff' }} />
          <T x={cols[i]} y={125} w={64} className="text-[4.4px] leading-[6px] text-white">{c.items.map((l) => <div key={l}>{l}</div>)}</T>
        </div>
      ))}
      <T x={6} y={116} w={334} h={0.6} style={{ background: 'rgba(255,255,255,0.5)' }} />
    </Frame>
  )
}
function Journey() {
  return (
    <Frame>
      <T x={12} y={11} className="whitespace-nowrap text-[8.2px] font-semibold leading-[12.5px]">{journey.title.map((l) => <div key={l}>{l}</div>)}</T>
      <T x={12} y={42} className="whitespace-nowrap text-[4.8px] leading-[7px]">{journey.sub.map((l) => <div key={l}>{l}</div>)}</T>
      <svg className="absolute left-0 top-0" width={346} height={194} fill="none" stroke={theme.orange} strokeWidth={1.2}>
        <path d="M16 145 C45 140 50 105 80 100 C110 96 130 85 166 70 C200 58 225 40 250 26" />
      </svg>
      {journey.points.map((p) => (
        <div key={p.name}>
          <div className="absolute rounded-full bg-[#111]" style={{ left: p.x + 1, top: p.y + 10, width: 4, height: 4 }} />
          <T x={p.x} y={p.y} className="rounded-[2px] border border-gray-300 bg-white px-[3px] text-[3.8px]">{p.date}</T>
          <T x={p.x + 7} y={p.y + 7} className="text-[7px] font-semibold">{p.name}</T>
          <T x={p.x} y={p.y + 18} className="whitespace-nowrap text-[3.8px] leading-[5px]">{p.text.map((l) => <div key={l}>{l}</div>)}</T>
        </div>
      ))}
      {journey.cards.map((c) => <InfoCard key={c.title} {...c} />)}
    </Frame>
  )
}
function Market() {
  return (
    <Frame>
      <T x={10} y={10} className="text-[4.8px] font-medium">Market potential</T>
      {market.items.map((m, i) => (
        <div key={m.name}>
          <i className="absolute rounded-full" style={{ left: 10, top: 29 + i * 24, width: 6, height: 6, background: m.color }} />
          <T x={22} y={27 + i * 24} className="text-[5.5px] font-bold">{m.name}</T>
          <T x={22} y={36 + i * 24} className="text-[4px] text-gray-500">{m.value}</T>
        </div>
      ))}
      <T x={10} y={140} w={125} className="rounded-[3px] bg-[#eef2fb] p-[4px]">
        <div className="text-[9px] font-bold text-[#2f6df6]">2M+ 32B companies annually</div>
        <div className="text-[3.6px] text-gray-500">looking for clients and learning to sell through MVP platforms like Lovable</div>
      </T>
      <T x={10} y={186} className="text-[3.4px] text-gray-400">Source: Statista via JonDenies</T>
      <Ph x={145} y={4} w={194} h={187} r={5} tone="#3d9cf5" />
      {market.callouts.map((c) => (
        <T key={c.t} x={c.x} y={c.y} className="whitespace-nowrap rounded-[2px] px-[3px] py-[1px] text-[4.2px] font-semibold text-white" style={{ background: c.orange ? theme.orange : theme.blue }}>{c.t}</T>
      ))}
      <T x={163} y={181} className="text-[3.6px] text-white">2024</T>
      <T x={321} y={181} className="text-[3.6px] text-white">2030</T>
    </Frame>
  )
}
function Contacts() {
  const { raising, split, lines } = contacts
  return (
    <Frame bg="#fbfbfb">
      <T x={10} y={11} className="text-[9px] font-medium">Contacts</T>
      <Ph x={6} y={33} w={82} h={76} tone={theme.orange} />
      <T x={6} y={58} w={82} className="text-center text-white"><div className="text-[5px]">{raising.label}</div><div className="text-[15px] font-medium leading-[18px]">{raising.value}</div></T>
      {split.map((s) => (
        <T key={s.l} x={s.x} y={33} w={s.w} h={76} className="text-white" style={{ background: s.c }}>
          <div className="mt-[24px] text-center text-[9px] font-medium" style={{ color: s.w > 100 ? '#c2410c' : '#fff' }}>{s.v}</div>
          <div className="text-center text-[4px]" style={{ color: s.w > 100 ? '#c2410c' : '#fff' }}>{s.l}</div>
        </T>
      ))}
      <T x={6} y={113} w={164} h={76} className="rounded-[3px] p-[6px] text-white" style={{ background: theme.blue }}>
        <div className="text-[6.5px]">Contact</div>
        <div className="mt-[34px] text-[4.5px] leading-[6.5px]">{lines.map((l) => <div key={l}>{l}</div>)}</div>
      </T>
      <T x={174} y={113} w={167} h={76} className="rounded-[3px] bg-white shadow-[0_1px_5px_rgba(0,0,0,0.1)]" />
      <T x={182} y={152} w={80} className="text-[6.5px] font-semibold leading-[8px]">View the product<br />from the inside</T>
      <Ph x={277} y={122} w={59} h={59} r={2} />
    </Frame>
  )
}
const deck: DeckDefinition = { id: '08', title: 'SalesTrigger orange', slides: [Roadmap, Journey, Market, Contacts] }
export default deck
