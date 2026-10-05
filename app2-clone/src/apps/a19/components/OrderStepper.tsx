import { Check } from 'lucide-react'
import type { Step } from '../data'
import { fi } from '../theme'

/** Horizontal order-progress stepper (dots joined by lines, two-line captions). */
export function OrderStepper({ steps, spacing = 130, className }: { steps: Step[]; spacing?: number; className?: string }) {
  return (
    <div className={className} style={{ width: spacing * (steps.length - 1) + 80, height: 70 }}>
      {steps.slice(1).map((_, i) => (
        <span
          key={i}
          className="absolute top-[9px] h-[1.5px] bg-[#8d8d8d]"
          style={{ left: 40 + i * spacing + 13, width: spacing - 26 }}
        />
      ))}
      {steps.map((s, i) => (
        <div key={i} className="absolute top-0 flex w-[80px] flex-col items-center" style={{ left: i * spacing }}>
          {s.done ? (
            <span className="flex h-[19px] w-[19px] items-center justify-center rounded-full" style={{ background: fi.green }}>
              <Check size={12} strokeWidth={3.4} className="text-white" />
            </span>
          ) : (
            <span className="h-[19px] w-[19px] rounded-full border-[2px] border-[#222]" />
          )}
          <div className="mt-[10px] text-center text-[11.5px] font-medium leading-[17px] text-[#222]">
            {s.label.map((l) => (
              <div key={l}>{l}</div>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}
