import type { CSSProperties } from 'react'

/** Text with explicit line breaks so wrapping matches the reference exactly. */
export function Lines({ lines, className, style }: { lines: readonly string[]; className?: string; style?: CSSProperties }) {
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
