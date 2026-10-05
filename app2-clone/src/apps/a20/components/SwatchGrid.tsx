import { Check } from 'lucide-react'
import { cn } from '../../../ui'

export interface SwatchGridProps {
  rows: string[][]
  /** "row-col" of the selected swatch */
  selected?: string
  pitchX?: number
  pitchY?: number
  size?: number
  className?: string
}

/** Colour picker grid; the special value "wheel" renders the custom-colour wheel. */
export function SwatchGrid({ rows, selected, pitchX = 37.7, pitchY = 37.7, size = 23, className }: SwatchGridProps) {
  return (
    <div className={cn('', className)}>
      {rows.map((row, r) =>
        row.map((c, i) => {
          const on = selected === `${r}-${i}`
          return (
            <span
              key={`${r}-${i}`}
              className="absolute flex items-center justify-center rounded-full"
              style={{
                left: i * pitchX,
                top: r * pitchY,
                width: size,
                height: size,
                transform: 'translate(-50%,-50%)',
                background: c === 'wheel' ? 'conic-gradient(#f55, #fd5, #5e5, #5df, #55f, #f5f, #f55)' : c,
                boxShadow: on ? '0 0 0 7px rgba(200,205,212,0.6)' : c === '#ffffff' ? 'inset 0 0 0 1px #e6e6e6' : undefined,
              }}
            >
              {c === 'wheel' && <span className="h-[14px] w-[14px] rounded-full bg-white/70 blur-[2px]" />}
              {on && <Check size={13} strokeWidth={2.6} className="text-white" />}
            </span>
          )
        }),
      )}
    </div>
  )
}
