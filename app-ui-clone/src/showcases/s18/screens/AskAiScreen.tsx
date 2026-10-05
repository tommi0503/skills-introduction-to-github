import { EllipsisVertical } from 'lucide-react'
import { ChatBubble } from '../components/ChatBubble'
import { ChatInput } from '../components/ChatInput'
import { MatchStack } from '../components/MatchStack'
import { TopBar } from '../components/TopBar'
import { askScreen as d } from '../data'

/** Vertical offset of each message in the thread (logical pt). */
const messageTops: Record<string, number> = { u1: 151, b1: 237, m: 324, u2: 630 }

export function AskAiScreen() {
  return (
    <div className="absolute inset-0">
      <TopBar title={d.title} action={EllipsisVertical} />
      {d.messages.map((m) => (
        <div
          key={m.key}
          className="absolute"
          style={{ top: messageTops[m.key], left: m.from === 'matches' ? 0 : 15, right: m.from === 'matches' ? 0 : 15 }}
        >
          {m.from === 'matches' ? <MatchStack {...d.match} pages={d.pages} /> : <ChatBubble from={m.from} lines={m.lines} />}
        </div>
      ))}
      <div className="absolute top-[743.5px] left-[15px]">
        <ChatInput placeholder={d.input} />
      </div>
    </div>
  )
}
