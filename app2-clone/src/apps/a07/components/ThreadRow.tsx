import type { ChatThread } from '../data'
import { BotAvatar } from './BotAvatar'
import { TagChip } from './TagChip'

export function ThreadRow({ thread }: { thread: ChatThread }) {
  return (
    <div className="flex h-[79px] items-start gap-[13px] pr-[24px] pl-[21px]">
      <BotAvatar shape={thread.shape} online={thread.online} className="mt-[5px]" />
      <div className="min-w-0 flex-1 pt-[1px]">
        <div className="flex items-center gap-[8px]">
          <span className="min-w-0 shrink truncate text-[16px] leading-[22px] font-[450] tracking-[0.15px] text-[#111]">{thread.title}</span>
          {thread.tag && <TagChip label={thread.tag} className="max-w-[106px] shrink-0" />}
          <span className="ml-auto shrink-0 pl-[6px] text-[12.5px] text-[#bdbdbd]">{thread.time}</span>
        </div>
        {thread.preview && <p className="mt-[3px] truncate text-[14px] leading-[19px] tracking-[0.2px] text-[#8a8a8a]">{thread.preview}</p>}
      </div>
    </div>
  )
}
