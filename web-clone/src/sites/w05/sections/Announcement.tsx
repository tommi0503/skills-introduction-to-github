import { ArrowRight } from 'lucide-react'
import { announcement } from '../data'
import { theme } from '../theme'

export function Announcement() {
  return (
    <div className="flex h-[62px] items-center justify-center gap-[24px] text-[16px] leading-[23.2px]">
      <span style={{ color: theme.ink }}>{announcement.text}</span>
      <span className="flex items-center gap-[4px]" style={{ color: theme.cyan }}>
        {announcement.cta}
        <ArrowRight size={14} strokeWidth={2} />
      </span>
    </div>
  )
}
