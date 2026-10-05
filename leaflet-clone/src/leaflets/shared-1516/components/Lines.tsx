import { cn } from '../../../ui'

export interface LinesProps {
  lines: string[]
  className?: string
}

/** Pre-broken multi-line text block. */
export function Lines({ lines, className }: LinesProps) {
  return (
    <div className={cn(className)}>
      {lines.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  )
}
