import { cn } from '../../../ui'
import { palette as c } from '../theme'

export function Divider({ className }: { className?: string }) {
  return <div className={cn('h-px', className)} style={{ background: c.line }} />
}
