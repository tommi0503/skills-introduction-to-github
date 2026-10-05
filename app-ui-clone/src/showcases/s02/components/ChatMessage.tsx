import { cn } from '../../../ui'
import type { ChatEntry } from '../data'

interface ChatMessageProps {
  entry: ChatEntry
  width: number
}

/** Message bubble resting on a grey tray that carries the timestamp. */
export function ChatMessage({ entry, width }: ChatMessageProps) {
  const isUser = entry.from === 'user'
  return (
    <div className="rounded-[16px] bg-[#f1f1f1]" style={{ width }}>
      <div
        className={cn(
          'rounded-[16px] px-[14px] py-[11px] text-[14px] leading-[19.5px] tracking-[-0.1px]',
          isUser ? 'bg-white text-[#1d1d1d] shadow-[0_2px_6px_rgba(0,0,0,0.04)]' : 'bg-[#1f1f1f] text-white',
        )}
      >
        {entry.lines.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <div className="px-[14px] pt-[4px] pb-[5px] text-[12.5px] text-[#9a9a9a]">{entry.time}</div>
    </div>
  )
}
