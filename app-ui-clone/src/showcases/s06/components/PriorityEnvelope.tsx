import { Sparkles } from 'lucide-react'
import { theme } from '../theme'

export interface PriorityEnvelopeProps {
  label: string
  count: string
  countLabel: string
}

/**
 * Envelope hero made of plain gradient shapes: a white pocket, the blue letter
 * with its flap fold, and a frosted band carrying the counter.
 */
export function PriorityEnvelope({ label, count, countLabel }: PriorityEnvelopeProps) {
  return (
    <div className="relative h-[260px] w-[340px]">
      <div className="absolute inset-x-0 top-0 h-[160px] rounded-[40px] bg-white shadow-[0_6px_18px_rgba(0,0,0,0.07)]" />
      <div className="absolute left-[25px] top-[20px] h-[150px] w-[292px] overflow-hidden rounded-[24px]" style={{ background: theme.envelope }}>
        <div
          className="absolute inset-0"
          style={{ background: 'rgba(30,80,140,0.10)', clipPath: 'polygon(0 22%, 50% 92%, 100% 22%, 100% 100%, 0 100%)' }}
        />
        <p className="absolute inset-x-0 top-[22px] text-center text-[14px] text-white">{label}</p>
        <span className="absolute left-[121px] top-[50px] flex h-[50px] w-[49px] items-center justify-center rounded-[12px] bg-white">
          <Sparkles size={18} strokeWidth={1.7} color={theme.blue} />
        </span>
      </div>
      <div
        className="absolute left-[20px] top-[140px] h-[105px] w-[300px] rounded-[30px] blur-[9px]"
        style={{ background: 'linear-gradient(90deg, #8cc8dc 0%, #78b4e2 50%, #6aa2ec 100%)' }}
      />
      <div className="absolute inset-x-0 top-[180px] flex items-center justify-center gap-[13px] text-white">
        <span className="text-[42px] leading-none font-semibold tracking-[-1px]">{count}</span>
        <span className="text-[18px] font-medium">{countLabel}</span>
      </div>
    </div>
  )
}
