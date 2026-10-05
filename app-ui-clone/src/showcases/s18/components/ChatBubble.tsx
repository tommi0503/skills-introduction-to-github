import { Avatar } from '../../../ui'
import { theme } from '../theme'
import { BotGlyph } from './BotGlyph'

export interface ChatBubbleProps {
  from: 'user' | 'bot'
  lines: string[]
}

/** One chat line: grey bubble with the speaker's avatar on its side. */
export function ChatBubble({ from, lines }: ChatBubbleProps) {
  const bubble = (
    <div className="rounded-full px-[19px] py-[9.5px] text-[13.1px] leading-[17.5px]" style={{ background: theme.soft, color: '#4a4a4a' }}>
      {lines.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  )
  if (from === 'user')
    return (
      <div className="flex items-center justify-end gap-[10px]">
        {bubble}
        <Avatar size={45} tone="#d9c4f3" />
      </div>
    )
  return (
    <div className="flex items-center">
      <span className="flex h-[45px] w-[45px] items-center justify-center rounded-full" style={{ background: theme.botSoft }}>
        <BotGlyph size={22} color={theme.bot} />
      </span>
      <span className="h-[1.5px] w-[10px]" style={{ background: theme.botSoft }} />
      {bubble}
    </div>
  )
}
