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
      <div className="absolute left-[25px] top-[20px] h-[124px] w-[292px] overflow-hidden rounded-t-[24px]" style={{ background: theme.envelope }}>
        <div
          className="absolute inset-0"
          style={{ background: 'rgba(30,80,140,0.10)', clipPath: 'polygon(0 26%, 50% 100%, 100% 26%, 100% 100%, 0 100%)' }}
        />
        <p className="absolute inset-x-0 top-[18px] text-center text-[14.5px] text-white">{label}</p>
        <span className="absolute left-[121px] top-[50px] flex h-[50px] w-[49px] items-center justify-center rounded-[12px] bg-white">
          <Sparkles size={18} strokeWidth={1.7} color={theme.blue} />
        </span>
      </div>
      <div
        className="absolute left-0 top-[144px] h-[110px] w-[340px]"
        style={{
          background: 'linear-gradient(90deg, rgba(150,206,224,0.95) 0%, rgba(120,180,226,0.95) 50%, rgba(104,160,236,0.95) 100%)',
          WebkitMaskImage:
            'linear-gradient(90deg, transparent 2%, #000 16%, #000 86%, transparent 100%), linear-gradient(180deg, #000 70%, transparent 100%)',
          WebkitMaskComposite: 'source-in',
          maskComposite: 'intersect',
        }}
      />
      <div className="absolute inset-x-0 top-[169px] flex items-center justify-center gap-[13px] pl-[8px] text-white">
        <span className="text-[42px] leading-none font-semibold tracking-[-1px]">{count}</span>
        <span className="text-[18px] font-medium">{countLabel}</span>
      </div>
    </div>
  )
}
