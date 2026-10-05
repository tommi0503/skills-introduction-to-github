import type { ReactNode } from 'react'
import { theme } from '../theme'

/** Rounded brand-purple panel; content (copy + illustration placeholders) is injected. */
export function HeroCard({ top, height, radius = 19, children }: { top: number; height: number; radius?: number; children: ReactNode }) {
  return (
    <div
      className="absolute left-[13.6px] w-[362px] overflow-hidden"
      style={{ top, height, borderRadius: radius, background: theme.brand }}
    >
      {children}
    </div>
  )
}
