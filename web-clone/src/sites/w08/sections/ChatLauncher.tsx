import { MessageSquareMore } from 'lucide-react'
import { theme } from '../theme'

/** Fixed support-chat bubble captured at the right edge of the viewport. */
export function ChatLauncher() {
  return (
    <span
      className="absolute flex items-center justify-center rounded-full"
      style={{ left: 1372, top: 832, width: 48, height: 48, background: theme.ink, color: theme.page }}
    >
      <MessageSquareMore size={24} strokeWidth={2} />
    </span>
  )
}
