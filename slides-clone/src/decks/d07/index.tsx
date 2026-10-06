import { Zap } from 'lucide-react'
import { ImagePlaceholder, type DeckDefinition } from '../../ui'
import { Chevron, Frame, T, Tag } from './components'
import { brand, funnel, hero, market, process } from './data'
import { theme } from './theme'

const Ph = ({ x, y, w, h, r = 2, tone }: { x: number; y: number; w: number; h: number; r?: number; tone?: string }) => (
  <ImagePlaceholder tone={tone} className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: r }} />
)

function Hero() {
  return (
    <Frame bg="#3b82f6">
      <Ph x={0} y={0} w={444} h={250} r={0} tone="#4c8cf7" />
      <T x={222} y={14} className="flex items-center gap-1 text-[8.5px] font-semibold text-white" style={{ transform: 'translateX(-50%)' }}><Zap size={9} />{brand}</T>
      <T x={222} y={55} className="whitespace-nowrap text-center text-[27px] font-semibold leading-[29px] text-white" style={{ transform: 'translateX(-50%)' }}>{hero.map((l) => <div key={l}>{l}</div>)}</T>
      <Ph x={55} y={150} w={140} h={90} tone="#cfe0fc" />
      <Ph x={165} y={158} w={150} h={90} tone="#cfe0fc" />
      <Ph x={290} y={165} w={150} h={85} tone="#cfe0fc" />
    </Frame>
  )
}
function Funnel() {
  return (
    <Frame bg="#fff">
      <T x={13} y={11} className="whitespace-nowrap text-[11.5px] font-bold">{funnel.title}</T>
      <T x={13} y={30} className="text-[6.5px]">{funnel.sub}</T>
      {funnel.rows.map((r, i) => (
        <div key={r.label}>
          <T x={13} y={68 + i * 35} w={82} h={26} className="flex items-center rounded-[3px] bg-[#eef2fb] px-2 text-[6px] font-medium">{r.label}</T>
          <T x={98} y={68 + i * 35} w={r.w} h={26} className="rounded-[3px]" style={{ background: theme.blue }} />
          {r.tag && <Tag x={101} y={70 + i * 35} bg="rgba(255,255,255,0.25)" color="#fff">{r.tag}</Tag>}
          <T x={102} y={(r.tag ? 79 : 74) + i * 35} className="text-[10px] font-semibold text-white">{r.pct}</T>
          {r.extra && (
            <>
              <T x={98 + r.w} y={68 + i * 35} w={60} h={26} style={{ background: 'repeating-linear-gradient(115deg,#2f6df6 0 4px,#fff 4px 6px)' }} />
              <T x={98 + r.w + 66} y={68 + i * 35 + 3} className="whitespace-nowrap text-[7px] font-semibold text-[#ee3b1c]">{r.extra[0]}</T>
              <T x={98 + r.w + 66} y={68 + i * 35 + 14} className="whitespace-nowrap text-[9px] font-semibold">{r.extra[1]}</T>
            </>
          )}
        </div>
      ))}
    </Frame>
  )
}
function Process() {
  return (
    <Frame bg={theme.page}>
      <T x={13} y={9} className="whitespace-nowrap text-[13px] font-bold leading-[17px]">{process.title.map((l) => <div key={l}>{l}</div>)}</T>
      <T x={349} y={36} className="flex items-center gap-[3px] whitespace-nowrap text-[6px]"><i className="h-[7px] w-[7px] rounded-[1.5px]" style={{ background: theme.blue }} />Time</T>
      <T x={384} y={36} className="flex items-center gap-[3px] whitespace-nowrap text-[6px]"><i className="h-[7px] w-[7px] rounded-[1.5px]" style={{ background: theme.orange }} />Conversion</T>
      <T x={431} y={8} className="text-[5px]">2</T>
      <T x={6} y={48} w={433} h={168} className="rounded-[4px] bg-white" />
      {process.cols.map((c, i) => (
        <div key={c.step}>
          {i > 0 && <T x={6 + i * 104 + 6} y={52} w={0.6} h={160} style={{ background: '#e5e9f2' }} />}
          <Tag x={13 + i * 104} y={61}>{c.tag}</Tag>
          {c.tag2 && <Tag x={66 + i * 104} y={61} color={theme.orange} bg="#fdece2">{c.tag2}</Tag>}
          <T x={13 + i * 104} y={76} w={92} className="text-[5.2px] leading-[7px]">{c.text}</T>
          <Chevron x={12 + i * 104} y={125} w={110} first={i === 0}>{c.step}</Chevron>
          <Ph x={14 + i * 104} y={188} w={88} h={22} />
        </div>
      ))}
    </Frame>
  )
}
function Market() {
  return (
    <Frame bg="#fff">
      <T x={13} y={10} className="whitespace-nowrap text-[13px] font-bold">{market.title}</T>
      {market.bars.map((b) => (
        <div key={b.value}>
          <T x={b.x} y={b.y} w={b.w} h={b.h} className="rounded-[5px]" style={{ background: b.color }} />
          <T x={b.x + 9} y={b.y + 8} className="text-[8px] font-semibold leading-[10px] text-white">{b.name.map((l) => <div key={l}>{l}</div>)}</T>
          <T x={b.x + 9} y={b.y + 52} className="whitespace-nowrap rounded-[2px] bg-white/25 px-1 text-[5px] font-medium text-white">{b.cagr}</T>
          <T x={b.x + 9} y={b.y + 66} className="whitespace-nowrap text-[9px] font-medium text-white">{b.value}</T>
        </div>
      ))}
      <T x={13} y={236} className="text-[4px] text-gray-500">{market.source}</T>
    </Frame>
  )
}
const deck: DeckDefinition = { id: '07', title: 'SalesTrigger', slides: [Hero, Funnel, Process, Market] }
export default deck
