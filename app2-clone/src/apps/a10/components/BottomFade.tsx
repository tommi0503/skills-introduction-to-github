import { cn } from '../../../ui'

/** White fade that dissolves scrolling content under the floating bars. */
export function BottomFade({ className }: { className?: string }) {
  return (
    <div className={cn('pointer-events-none absolute inset-x-0 bottom-0 bg-gradient-to-b from-white/0 via-white/85 to-white', className)} />
  )
}
