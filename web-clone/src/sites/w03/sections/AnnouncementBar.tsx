import { X } from 'lucide-react'
import { announcement } from '../data'

export function AnnouncementBar() {
  return (
    <div className="relative flex h-[34px] items-center justify-center text-[14px] leading-[18.2px] text-[#0f0e0d]">
      <span className="tracking-[-0.12px]">{announcement.text}</span>
      <span className="ml-[10px] font-medium">{announcement.cta}</span>
      <X className="absolute right-[32px] top-[9px] size-4" strokeWidth={1.75} />
    </div>
  )
}
