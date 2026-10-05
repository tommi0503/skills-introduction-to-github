import { cn } from '../../../ui'

/** Segmented progress line (completed segments dark). */
export function StepProgress({ steps, done, className }: { steps: number; done: number; className?: string }) {
  return (
    <div className={cn('flex gap-[4px]', className)}>
      {Array.from({ length: steps }, (_, i) => (
        <span key={i} className="h-[3px] flex-1" style={{ background: i < done ? '#222' : '#e2e2e2' }} />
      ))}
    </div>
  )
}
