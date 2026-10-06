import { Check } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Frame, Kicker, Ph, T } from './components'
import { compare, connector, impacts, layers, market, pains, value } from './data'
import { theme } from './theme'

const B = ({ children }: { children: string }) => <span style={{ color: theme.blue }}>{children}</span>

const Title = () => (
  <Frame>
    <Ph x={14} y={20} w={12} h={13} r={2} />
    <T x={30} y={19} className="text-[4px] font-semibold">cycode</T>
    <T x={30} y={26} className="text-[9.5px] font-bold" style={{ color: theme.navy }}>Complete ASPM</T>
    <Ph x={80} y={36} w={235} h={135} r={6} />
  </Frame>
)
const Impacts = () => (
  <Frame>
    <T x={13} y={22} className="text-[9px] font-medium leading-[11px]" style={{ color: theme.navy }}>The Impacts<br />have Created<br /><B>Ripple Effects.</B></T>
    {impacts.map(({ icon: I, pre, bold, post, y }) => (
      <div key={bold}>
        <T x={187} y={y - 6} w={12} h={12} className="flex items-center justify-center rounded-[3px] text-white" style={{ background: theme.blue }}><I size={7} /></T>
        <T x={204} y={y - 2} className="whitespace-nowrap text-[4.6px]">{pre}<b className="font-semibold" style={{ color: theme.blue }}>{bold}</b>{post}</T>
      </div>
    ))}
  </Frame>
)
const Compare = () => (
  <Frame>
    <Kicker>Competitive Landscape</Kicker>
    <T x={8} y={15} className="text-[7px] font-semibold" style={{ color: theme.navy }}>How Cycode Do It <B>Better?</B></T>
    <T x={98} y={47} w={88} h={9} className="flex items-center justify-center bg-[#d7dbe3] text-[3.6px] font-semibold">Alternative Vendors</T>
    <T x={189} y={47} w={100} h={9} className="flex items-center justify-center text-[3.6px] font-semibold text-white" style={{ background: theme.blue }}>Cycode&apos;s Advantage</T>
    {compare.rows.map((r) => (
      <div key={r.y}>
        <T x={8} y={r.y} w={90} h={48} className="rounded-[2px] bg-[#f3f6fb]" />
        <T x={14} y={r.y + 8} className="text-[3.8px] font-medium leading-[5px]">{r.label.map((l) => <div key={l}>{l}</div>)}</T>
        <Ph x={55} y={r.y + 6} w={40} h={30} r={2} />
        <T x={98} y={r.y} w={88} h={48} className="rounded-[2px] border border-[#d9dde6] bg-white" />
        <T x={189} y={r.y} w={100} h={48} className="rounded-[2px] bg-white" style={{ border: `1px solid ${theme.blue}` }}>
          {[0, 1, 2].map((i) => <div key={i} className="absolute flex items-center gap-1" style={{ left: 6, top: 8 + i * 12 }}><i className="h-[5px] w-[5px] rounded-[1px]" style={{ background: theme.blue }} /><i className="h-[2px] w-[50px] bg-[#d5def4]" /></div>)}
        </T>
      </div>
    ))}
  </Frame>
)
const Market = () => (
  <Frame>
    <Kicker>Competitive Landscape</Kicker>
    <T x={8} y={15} className="text-[5px]" style={{ color: theme.navy }}>An Ever-Expanding Market Opportunity</T>
    <T x={17} y={63} className="whitespace-nowrap text-[8.2px] font-semibold leading-[12px]" style={{ color: theme.navy }}>{market.quote.map((l) => <div key={l}>{l}</div>)}</T>
    {market.circles.map((c) => (
      <div key={c.v}>
        <div className="absolute rounded-full" style={{ left: c.cx - c.r, top: c.cy - c.r, width: c.r * 2, height: c.r * 2, background: c.c }} />
        <T x={c.cx - c.r} y={c.cy - c.t * 0.9} w={c.r * 2} className="text-center text-white"><div className="font-bold leading-none" style={{ fontSize: c.t }}>{c.v}</div><div className="mt-[2px] text-[3.4px] leading-[4px]">{c.l.map((l) => <div key={l}>{l}</div>)}</div></T>
      </div>
    ))}
    <T x={8} y={160} className="text-[3.6px] text-gray-500">Source: <b>Gartner</b></T>
  </Frame>
)
const Mission = () => (
  <Frame bg={theme.blue} bar={false} light>
    <Ph x={97} y={80} w={12} h={13} r={2} tone="#6f93f4" />
    <T x={113} y={78} className="text-[3.6px] text-white/80">Cycode&apos;s Mission</T>
    <T x={113} y={84} className="whitespace-nowrap text-[8.5px] font-medium text-white">Deliver safe code — faster.</T>
  </Frame>
)
const Layers = () => (
  <Frame>
    {layers.map((l, i) => (
      <div key={l}>
        <T x={22} y={33 + i * 26} className="text-[4px]">{l}</T>
        <Ph x={104} y={25 + i * 26} w={52} h={26} r={3} />
        <T x={176} y={28 + i * 26} w={104} h={22} className="rounded-[2px] border bg-[#f3f6fd]" style={{ borderColor: theme.line }} />
      </div>
    ))}
  </Frame>
)
const Connector = () => (
  <Frame>
    <T x={8} y={8} w={78} h={156} className="rounded-[3px] bg-[#f1f4fa]" />
    {connector.left.map((c) => (
      <T key={c.t} x={13} y={c.y} w={68} h={c.h} className="rounded-[2px] bg-white p-[3px] text-[3.4px] font-semibold">{c.t}<Ph x={0} y={0} w={0} h={0} /></T>
    ))}
    <T x={85} y={16} w={154} h={140} className="rounded-[3px] bg-[#eaf0fd]" />
    <Ph x={112} y={40} w={100} h={62} r={4} />
    <T x={92} y={124} w={140} className="text-center text-[3.6px] leading-[5px] text-gray-600">{connector.copy}</T>
    {connector.right.map(({ icon: I, ...c }) => (
      <T key={c.t} x={243} y={c.y} w={54} h={c.h} className="flex flex-col items-center justify-center gap-1 rounded-[2px] bg-[#f1f4fa] text-center text-[3.4px]">
        <span className="flex h-[9px] w-[9px] items-center justify-center rounded-[2px] text-white" style={{ background: theme.blue }}><I size={5} /></span>{c.t}
      </T>
    ))}
  </Frame>
)
const Maximize = () => (
  <Frame>
    <T x={15} y={14} className="text-[6.5px] font-semibold leading-[8px]" style={{ color: theme.navy }}>Maximizing Value<div className="text-[4.2px] font-normal">with Cycode&apos;s Complete ASPM</div></T>
    <Ph x={36} y={66} w={76} h={80} r={4} />
    {value.map((v) => (
      <div key={v.t}>
        <T x={164} y={v.y} w={9} h={9} className="flex items-center justify-center rounded-full bg-[#dbe6fd]" style={{ color: theme.blue }}><Check size={5} /></T>
        <T x={178} y={v.y - 1} w={115}><div className="text-[4.4px] font-semibold">{v.t}</div><div className="mt-[1px] text-[3.6px] leading-[5px] text-gray-500">{v.d}</div></T>
      </div>
    ))}
  </Frame>
)
const Racing = () => (
  <Frame>
    <T x={15} y={14} className="text-[7px] font-semibold" style={{ color: theme.navy }}>But Security is <B>Racing to Keep up</B></T>
    <T x={15} y={26} className="text-[4px] text-gray-500">Security Team Pain Points</T>
    <Ph x={0} y={58} w={315} h={116} r={0} tone="#eaf0fd" />
    {pains.map((p) => <T key={p.t} x={p.x} y={p.y} className="whitespace-nowrap text-[4.3px]" style={{ color: theme.navy }}>{p.t}</T>)}
  </Frame>
)
const deck: DeckDefinition = { id: '09', title: 'Cycode ASPM', slides: [Title, Impacts, Compare, Market, Mission, Layers, Connector, Maximize, Racing] }
export default deck
