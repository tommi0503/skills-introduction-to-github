import { theme } from '../theme'

export function PageDots({ count, active, className }: { count: number; active: number; className?: string }) {
  return (
    <div className={className}>
      <div className="flex justify-center gap-[11px]">
        {Array.from({ length: count }, (_, i) => (
          <span
            key={i}
            className="h-[6px] w-[6px] rounded-full"
            style={{ background: i === active ? theme.greenIcon : '#8a8a8a' }}
          />
        ))}
      </div>
    </div>
  )
}
