import { cn } from '../../../ui'
import type { InboxItem } from '../data'
import { CircleButton } from './CircleButton'
import { ThreadAvatar } from './ThreadAvatar'

export function InboxRow({ item, className }: { item: InboxItem; className?: string }) {
  return (
    <div className={cn('flex h-[79px] items-center pr-[20px] pl-[18px]', className)}>
      <ThreadAvatar kind={item.avatar} />
      <div className="ml-[13px] flex min-w-0 flex-1 flex-col">
        <div className="flex items-baseline gap-[6px] whitespace-nowrap">
          {item.title ? (
            <span className="truncate text-[16px] leading-[22px] font-semibold text-[#111]">{item.title}</span>
          ) : (
            <span className="my-[2px] h-[18px] w-[140px] bg-[#ececec]" />
          )}
          {item.meta && <span className="shrink-0 text-[14px] text-[#8a8a8a]">{item.meta}</span>}
        </div>
        <span className="truncate text-[14px] leading-[22px] text-[#777]">{item.subtitle}</span>
      </div>
      {item.action && (
        <CircleButton icon={item.action} filled={item.actionFilled} inverse={item.actionInverse} iconSize={item.actionFilled || item.actionInverse ? 19 : 20} className="ml-[10px]" />
      )}
    </div>
  )
}
