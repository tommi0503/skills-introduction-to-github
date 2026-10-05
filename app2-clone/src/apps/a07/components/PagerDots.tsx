import { cn } from '../../../ui'

export function PagerDots({ count, active, className }: { count: number; active: number; className?: string }) {
  return (
    <div className={cn('flex items-center justify-center gap-[6px]', className)}>
      {Array.from({ length: count }, (_, i) => (
        <span key={i} className="h-[5px] w-[5px] rounded-full" style={{ background: i === active ? '#666' : '#e3e3e3' }} />
      ))}
    </div>
  )
}
