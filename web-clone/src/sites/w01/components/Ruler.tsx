import { theme } from '../theme'

/** Full-bleed 16px "measuring tape" divider between sections. */
export function Ruler() {
  return (
    <div
      className="relative h-4 w-full"
      style={{
        borderTop: `1px solid ${theme.rule}`,
        borderBottom: `1px solid ${theme.rule}`,
        backgroundColor: theme.page,
        backgroundImage: `linear-gradient(to bottom, transparent 6px, ${theme.tickBand} 6px, ${theme.tickBand} 8px, transparent 8px), repeating-linear-gradient(to right, ${theme.tick} 0 1px, transparent 1px 8px)`,
      }}
    />
  )
}
