import type { LucideIcon } from 'lucide-react'
import { theme } from '../theme'

/** White circular action (call / chat) with optional lime notification dot. */
export function RoundAction({ icon: Icon, dot = false, size = 41 }: { icon: LucideIcon; dot?: boolean; size?: number }) {
  return (
    <div className="relative flex items-center justify-center rounded-full bg-white" style={{ width: size, height: size, color: theme.dark }}>
      <Icon size={18} strokeWidth={2.2} fill={theme.dark} />
      {dot && (
        <span className="absolute -top-[1px] -right-[1px] h-[12px] w-[12px] rounded-full" style={{ background: theme.lime, boxShadow: `0 0 0 2px ${theme.dark}` }} />
      )}
    </div>
  )
}
