import { ArrowRight } from 'lucide-react'
import { theme } from '../theme'

/** Section heading with a trailing "View all →" link. */
export function SectionTitle({ title, action = 'View all' }: { title: string; action?: string }) {
  return (
    <div className="flex items-center justify-between">
      <span className="font-poppins text-[17px] leading-[22px] font-semibold" style={{ color: theme.ink }}>
        {title}
      </span>
      <span className="flex items-center gap-[6px] font-poppins text-[13px]" style={{ color: '#7d7d7d' }}>
        {action}
        <ArrowRight size={15} strokeWidth={2} />
      </span>
    </div>
  )
}
