import { ue } from '../theme'

export function OrDivider({ label, className }: { label: string; className?: string }) {
  return (
    <div className={`flex items-center gap-[12px] ${className ?? ''}`}>
      <span className="h-px flex-1" style={{ background: '#bdbdbd' }} />
      <span className="text-[12.5px]" style={{ color: ue.muted }}>
        {label}
      </span>
      <span className="h-px flex-1" style={{ background: '#bdbdbd' }} />
    </div>
  )
}
