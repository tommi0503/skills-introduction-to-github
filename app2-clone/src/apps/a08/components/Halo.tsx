import type { ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { gh } from '../theme'

/** White floating surface with the soft iOS-26 style halo. */
export function Halo({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={cn('flex items-center bg-white', className)} style={{ boxShadow: gh.halo }}>
      {children}
    </div>
  )
}

export interface HaloButtonProps {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  className?: string
}

export function HaloButton({ icon: Icon, size = 44, iconSize = 21, strokeWidth = 2, className }: HaloButtonProps) {
  return (
    <Halo className={cn('justify-center rounded-full text-[#1f2328]', className)}>
      <span className="flex items-center justify-center" style={{ width: size, height: size }}>
        <Icon size={iconSize} strokeWidth={strokeWidth} />
      </span>
    </Halo>
  )
}

/** Several icons sharing one capsule (e.g. share + more). */
export function HaloGroup({ icons, className }: { icons: LucideIcon[]; className?: string }) {
  return (
    <Halo className={cn('h-[44px] justify-around rounded-full px-[8px] text-[#1f2328]', className)}>
      {icons.map((Icon, i) => (
        <Icon key={i} size={21} strokeWidth={1.9} />
      ))}
    </Halo>
  )
}
