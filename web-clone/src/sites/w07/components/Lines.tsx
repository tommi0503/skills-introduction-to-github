import type { CSSProperties } from 'react'

/** Renders text lines with explicit breaks, matching the reference line wrapping. */
export function Lines({ lines, style, className }: { lines: readonly string[]; style?: CSSProperties; className?: string }) {
  return (
    <div className={className} style={style}>
      {lines.map((l) => (
        <div key={l} className="whitespace-nowrap">
          {l}
        </div>
      ))}
    </div>
  )
}
