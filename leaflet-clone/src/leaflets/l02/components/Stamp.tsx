import { cn } from '../../../ui'

interface StampProps {
  lines: [string, string] | string[]
  size: number
  color: string
  className?: string
}

/** Round rubber-stamp style badge: outer ring, dotted inner ring, two words. */
export function Stamp({ lines, size, color, className }: StampProps) {
  return (
    <div
      className={cn('flex items-center justify-center rounded-full', className)}
      style={{ width: size, height: size, border: `2px solid ${color}`, color }}
    >
      <div
        className="flex flex-col items-center justify-center rounded-full font-poppins leading-none"
        style={{ width: size - 16, height: size - 16, border: `1.5px dotted ${color}` }}
      >
        <span className="text-[12.5px] font-bold tracking-[0.04em]">{lines[0]}</span>
        <span className="mt-[4px] text-[11px] tracking-[0.04em]">{lines[1]}</span>
      </div>
    </div>
  )
}
