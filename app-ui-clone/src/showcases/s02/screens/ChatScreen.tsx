import { ChevronLeft, EllipsisVertical, Paperclip } from 'lucide-react'
import { Avatar } from '../../../ui'
import { AiOrb } from '../components/AiOrb'
import { ChatMessage } from '../components/ChatMessage'
import { CircleButton } from '../components/CircleButton'
import { PillInput } from '../components/PillInput'
import { TripCardStack } from '../components/TripCardStack'
import { TypingRow } from '../components/TypingRow'
import { chat, messages, trip } from '../data'

/** Layout of each message row: tray width, top and where the sender avatar sits. */
const rows = {
  user: { top: 173, left: 62.5, width: 251.5 },
  ai: { top: 286.6, left: 61, width: 284 },
} as const

/** Assistant conversation with a generated trip card. */
export function ChatScreen() {
  return (
    <div className="relative h-full w-full">
      <div className="absolute inset-x-[24.4px] top-[57.5px] flex items-center justify-between">
        <CircleButton icon={ChevronLeft} iconSize={18} />
        <div className="flex items-center gap-[8px]">
          <AiOrb size={18.5} />
          <span className="text-[16.5px] font-semibold tracking-[-0.2px]">{chat.title}</span>
        </div>
        <CircleButton icon={EllipsisVertical} iconSize={18} />
      </div>
      <div className="absolute inset-x-[24.4px] top-[126px] flex items-center">
        <span className="h-px flex-1 bg-[#ececec]" />
        <span className="rounded-full bg-[#efefef] px-[14px] py-[4px] text-[12.5px] text-[#9a9a9a]">{chat.dayLabel}</span>
        <span className="h-px flex-1 bg-[#ececec]" />
      </div>
      {messages.map((m) => {
        const r = rows[m.from]
        return (
          <div key={m.id} className="absolute" style={{ top: r.top, left: r.left }}>
            <ChatMessage entry={m} width={r.width} />
          </div>
        )
      })}
      <div className="absolute top-[173.5px] left-[322.5px]">
        <Avatar size={29} />
      </div>
      <div className="absolute top-[285.5px] left-[24.5px]">
        <AiOrb size={29} />
      </div>
      <div className="absolute top-[413px] left-[60px]">
        <TripCardStack {...trip} />
      </div>
      <div className="absolute top-[643.5px] left-[24.5px]">
        <TypingRow label={chat.typing} />
      </div>
      <div className="absolute inset-x-[24.4px] top-[717px]">
        <PillInput leading={<Paperclip size={18} strokeWidth={1.6} className="text-[#3a3a3a]" />} leadingWidth={48} placeholder={chat.composer} />
      </div>
    </div>
  )
}
