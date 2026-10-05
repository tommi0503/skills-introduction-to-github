import { cn } from '../../../ui'
import { theme } from '../theme'

/** Orange square + uppercase mono label. */
export function Eyebrow({ label, className, color = '#fff' }: { label: string; className?: string; color?: string }) {
  return (
    <div className={cn('absolute flex items-center gap-[8px]', theme.font.mono, className)}>
      <span className="h-[7px] w-[7px]" style={{ background: theme.color.orange }} />
      <span className="text-[11px] font-medium uppercase leading-[14px]" style={{ color }}>
        {label}
      </span>
    </div>
  )
}
