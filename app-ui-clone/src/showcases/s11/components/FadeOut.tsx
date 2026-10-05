import { cn } from '../../../ui'

/** Bottom fade that blurs and washes out the content scrolling underneath. */
export function FadeOut({ top, color, className }: { top: number; color: string; className?: string }) {
  const mask = 'linear-gradient(180deg, transparent 0%, #000 35%)'
  return (
    <div className={cn('pointer-events-none absolute inset-x-0 bottom-0', className)} style={{ top }}>
      <div
        className="absolute inset-0 backdrop-blur-[6px]"
        style={{ maskImage: mask, WebkitMaskImage: mask }}
      />
      <div
        className="absolute inset-0"
        style={{ background: `linear-gradient(180deg, transparent 0%, ${color}80 40%, ${color}f0 70%, ${color} 85%)` }}
      />
    </div>
  )
}
