import { BellRing, Check, MessageSquareWarning, TriangleAlert, Earth } from 'lucide-react'
import type { ReactNode } from 'react'
import { why } from '../data'
import { theme } from '../theme'
import { SectionHeading } from '../components/Heading'
import { Corners } from '../components/Dashed'

const TOP = 2773

/** Dashed-border incident card floating in the "chaos" panel. */
function IncidentCard({ x, y, w, h, children }: { x: number; y: number; w: number; h: number; children: ReactNode }) {
  return (
    <div
      className="absolute overflow-hidden rounded-[6px] border border-dashed border-[#ececec] bg-[#fdfdfc] px-3 pt-[9px] text-[14px] leading-[16.1px] tracking-[-0.14px]"
      style={{ left: x - 120, top: y - 2972, width: w, height: h }}
    >
      {children}
    </div>
  )
}

function ChaosPanel() {
  const c = why.chaos
  return (
    <div className="relative h-full w-[600px] overflow-hidden">
      <span className="absolute left-[133px] top-[16px] flex h-9 items-center gap-1 rounded-[6px] border border-dashed border-[#f0f0f0] px-[10px] text-[14px] tracking-[-0.4px] text-[#727272]">
        <TriangleAlert className="size-5 text-[#ffcc00]" strokeWidth={1.5} />
        {c.status}
      </span>
      <h3 className="absolute inset-x-0 top-[49px] text-center text-[48px] font-medium leading-[48px] tracking-[-1.2px] text-[#262626]">
        {c.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h3>
      <p className="absolute left-[453px] top-[130px] text-[6px] leading-[7px] text-[#727272]/70">
        {c.whisper.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </p>
      <IncidentCard x={409} y={3336} w={192} h={60}>
        <BellRing className="size-5 text-[#ff4800]" strokeWidth={1.5} />
        <span className="mt-[4px] block text-[#727272]">{c.incidents}</span>
      </IncidentCard>
      <IncidentCard x={645} y={3300} w={120} h={92}>
        <MessageSquareWarning className="size-5 text-[#ff4800]" strokeWidth={1.5} />
        {c.leak.map((l, i) => (
          <span key={l} className={i ? 'block text-[#727272]' : 'mt-[3px] block text-[#262626]'}>
            {l}
          </span>
        ))}
      </IncidentCard>
      <IncidentCard x={257} y={3422} w={303} h={60}>
        <Earth className="size-5 text-[#ed1641]" strokeWidth={1.5} />
        <span className="mt-[4px] block text-[#262626]">{c.circuit}</span>
      </IncidentCard>
    </div>
  )
}

function ShipPanel() {
  const s = why.ship
  return (
    <div className="relative h-full w-[600px] text-white" style={{ background: theme.color.orange }}>
      <h3 className="absolute inset-x-0 top-[49px] text-center text-[48px] font-medium leading-[48px] tracking-[-1.2px]">
        {s.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h3>
      <div
        className="absolute inset-x-0 top-[278px] h-0 border-t-2 border-dotted border-white/40"
        aria-hidden
      />
      <span className="absolute left-[156px] top-[250px] flex h-[58px] w-[287px] items-center gap-[10px] rounded-[8px] border border-white/30 bg-[#ff6b33] pl-[17px] text-[16px]">
        <Check className="size-5" strokeWidth={2} />
        <span>
          {s.status[0]} <span className="mx-[2px]">{s.status[1]}</span> {s.status[2]}
        </span>
      </span>
    </div>
  )
}

export function WhyChoose() {
  return (
    <section className="relative h-[781px]">
      <SectionHeading title={why.title} body={why.body} size={56} gap={27} className="pt-[13px]" />
      <div className="absolute left-[120px] flex h-[500px] w-[1200px] border-y border-[#f0f0f0]" style={{ top: 2972 - TOP }}>
        <ChaosPanel />
        <ShipPanel />
      </div>
      <Corners x={120} y={2972 - TOP} w={1199} h={499} />
      <Corners x={720} y={2972 - TOP} w={0} h={499} />
    </section>
  )
}
