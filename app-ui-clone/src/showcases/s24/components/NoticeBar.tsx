import { ChevronRight, Megaphone } from 'lucide-react'
import { HomeIndicator, cn } from '../../../ui'
import type { Notice } from '../data'
import { theme } from '../theme'

/** Bottom notice strip with rounded top and home indicator. */
export function NoticeBar({ notice, className }: { notice: Notice; className?: string }) {
  return (
    <div
      className={cn('absolute inset-x-0 bottom-0 z-30 h-[88px] rounded-t-[20px] bg-white font-pretendard', className)}
      style={{ boxShadow: '0 -1px 0 #ececef, 0 -4px 12px rgba(0,0,0,0.03)' }}
    >
      <div className="flex h-[52px] items-center pr-[21px] pl-[27px]">
        <Megaphone size={15} strokeWidth={1.8} color={theme.navy} />
        <span className="ml-[13px] text-[13.2px] tracking-[-0.2px]" style={{ color: theme.ink }}>
          {notice.text}
          <b className="font-bold" style={{ color: theme.navy }}>
            {notice.bold}
          </b>
        </span>
        <ChevronRight size={14} strokeWidth={1.5} color="#a0a4b0" className="ml-auto" />
      </div>
      <HomeIndicator width={138} bottom={9} />
    </div>
  )
}
