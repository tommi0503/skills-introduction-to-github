import { ChevronRight, X } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface ProBannerProps {
  badge: string
  title: string
  text: string
  className?: string
}

export function ProBanner({ badge, title, text, className }: ProBannerProps) {
  return (
    <div className={cn('relative rounded-[12px] px-[15px] pt-[10px] text-white', className)} style={{ background: theme.purple, height: 56 }}>
      <div className="flex items-center text-[13px] leading-[18px] font-semibold">
        <span className="mr-[8px] rounded-[5px] bg-white/85 px-[5px] text-[11px] leading-[15px] font-bold" style={{ color: theme.purple }}>
          {badge}
        </span>
        {title}
        <ChevronRight size={15} strokeWidth={2.4} className="ml-[1px]" />
      </div>
      <p className="mt-[1px] text-[13px] leading-[18px] text-white/90">{text}</p>
      <X size={17} strokeWidth={2.6} className="absolute top-[10px] right-[11px]" />
    </div>
  )
}
