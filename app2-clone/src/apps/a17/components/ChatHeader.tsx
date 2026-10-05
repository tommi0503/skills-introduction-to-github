import { Ellipsis, Ghost, MessageCirclePlus, TextAlignStart } from 'lucide-react'
import { cn } from '../../../ui'
import { floatShadow } from '../theme'
import { FloatButton } from './FloatButton'

export interface ChatHeaderProps {
  /** Empty chat shows the incognito ghost; an active chat shows new-chat + more. */
  variant: 'empty' | 'chat'
}

/** Floating header controls: menu on the left, contextual actions on the right. */
export function ChatHeader({ variant }: ChatHeaderProps) {
  return (
    <>
      <FloatButton icon={TextAlignStart} className="absolute top-[60px] left-[16px] z-30" />
      {variant === 'empty' ? (
        <FloatButton icon={Ghost} className="absolute top-[60px] right-[18px] z-30" iconSize={20} />
      ) : (
        <div
          className={cn(
            'absolute top-[59px] right-[18px] z-30 flex h-[43px] w-[98px] items-center justify-around rounded-full bg-[#fefefc] px-[6px] text-[#2b2b29]',
            floatShadow,
          )}
        >
          <MessageCirclePlus size={22} fill="currentColor" stroke="#fff" strokeWidth={2} />
          <Ellipsis size={20} strokeWidth={2} />
        </div>
      )}
    </>
  )
}
