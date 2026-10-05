import type { CSSProperties, ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { Check, ChevronLeft, Minus, Plus } from 'lucide-react'
import { cn } from '../../../ui'
import { cu } from '../theme'

/* Small, single-purpose building blocks shared by the CU screens. */

export interface NavBarProps {
  title?: string
  actions?: LucideIcon[]
  className?: string
}

/** Back chevron + bold title on the left, outline icons on the right. */
export function NavBar({ title, actions = [], className }: NavBarProps) {
  return (
    <div className={cn('absolute inset-x-0 flex h-[30px] items-center pr-[18px] pl-[14px]', className)} style={{ top: 73 }}>
      <ChevronLeft size={26} strokeWidth={1.6} className="text-[#222]" />
      {title && <span className="ml-[6px] text-[17.5px] font-bold text-[#1a1a1a]">{title}</span>}
      <div className="ml-auto flex items-center gap-[18px]">
        {actions.map((Icon, i) => (
          <Icon key={i} size={25} strokeWidth={1.5} className="text-[#222]" />
        ))}
      </div>
    </div>
  )
}

export function CtaButton({ children, className, style }: { children: ReactNode; className?: string; style?: CSSProperties }) {
  return (
    <div
      className={cn('flex h-[59px] items-center justify-center rounded-full text-[19px] font-semibold text-white', className)}
      style={{ background: cu.green, ...style }}
    >
      {children}
    </div>
  )
}

export function CheckDot({ size = 20 }: { size?: number }) {
  return (
    <span className="flex shrink-0 items-center justify-center rounded-full text-white" style={{ width: size, height: size, background: cu.check }}>
      <Check size={size * 0.7} strokeWidth={3} />
    </span>
  )
}

export function Stepper({ value }: { value: number }) {
  return (
    <div className="flex h-[28px] w-[77px] items-center justify-between rounded-full border border-[#e2e2e2] bg-white px-[10px] text-[#222]">
      <Minus size={13} strokeWidth={2.6} />
      <span className="text-[15px] font-semibold">{value}</span>
      <Plus size={13} strokeWidth={2.6} />
    </div>
  )
}

export function Toggle({ on = true }: { on?: boolean }) {
  return (
    <span className="relative inline-block h-[19.5px] w-[35.5px] rounded-full" style={{ background: on ? cu.toggle : '#ddd' }}>
      <span className="absolute top-[2px] h-[15.5px] w-[15.5px] rounded-full bg-white" style={{ left: on ? 18 : 2 }} />
    </span>
  )
}
