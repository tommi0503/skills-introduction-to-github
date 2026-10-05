import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface ChatBubbleProps {
  from: 'user' | 'bot'
  children: ReactNode
  className?: string
  style?: CSSProperties
}

/** Small conversation bubble; user bubbles have the tail bottom-right, bot bubbles bottom-left. */
export function ChatBubble({ from, children, className, style }: ChatBubbleProps) {
  const user = from === 'user'
  return (
    <div
      className={cn('px-[14px] py-[8px] text-[10.5px] leading-[17.0625px] text-[#0a0a0a]', className)}
      style={{
        background: user ? 'rgba(10,10,10,0.08)' : 'rgba(10,10,10,0.04)',
        borderRadius: user ? '16px 16px 6px 16px' : '16px 16px 16px 6px',
        ...style,
      }}
    >
      {children}
    </div>
  )
}
