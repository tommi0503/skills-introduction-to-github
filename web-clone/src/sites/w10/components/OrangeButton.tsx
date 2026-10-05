import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Glossy orange CTA with mono uppercase label. */
export function OrangeButton({ label, className, style }: { label: string; className?: string; style?: CSSProperties }) {
  return (
    <span
      className={cn('absolute flex items-center justify-center rounded-[8px] text-[10.5px] uppercase tracking-[0.06em]', theme.font.mono, className)}
      style={{
        background: theme.color.orange,
        color: 'rgba(255,255,255,0.95)',
        boxShadow: 'inset 0 1px 0 rgba(255,255,255,0.35), 0 4px 10px rgba(0,0,0,0.35)',
        ...style,
      }}
    >
      {label}
    </span>
  )
}
