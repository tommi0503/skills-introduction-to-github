import { Tag } from 'lucide-react'
import { palette as c } from '../theme'

export function FeeToast({ label, className }: { label: string; className?: string }) {
  return (
    <div className={className}>
      <div
        className="flex h-[44px] items-center gap-[8px] rounded-[14px] bg-white pr-[16px] pl-[13px] text-[14.3px] font-medium"
        style={{ color: c.text, boxShadow: '0 4px 14px rgba(0,0,0,0.13)' }}
      >
        <Tag size={18} fill={c.brand} color={c.brand} strokeWidth={1.5} className="-rotate-12" />
        {label}
      </div>
    </div>
  )
}
