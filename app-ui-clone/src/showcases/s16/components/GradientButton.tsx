import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { orangeGradient } from '../theme'

/** Orange gradient pill button with optional leading icon. */
export function GradientButton({ label, icon: Icon, className }: { label: string; icon?: LucideIcon; className?: string }) {
  return (
    <div className={cn('flex items-center justify-center gap-[8px] rounded-full text-white', className)} style={{ background: orangeGradient }}>
      {Icon && <Icon size={24} strokeWidth={1.6} />}
      {label}
    </div>
  )
}
