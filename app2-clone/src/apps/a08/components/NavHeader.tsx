import type { ReactNode } from 'react'
import { ChevronLeft } from 'lucide-react'
import { cn } from '../../../ui'
import { HaloButton } from './Halo'

export interface NavHeaderProps {
  title: string
  subtitle?: ReactNode
  /** Centre the title block (Files Changed) vs. left after the back button. */
  centered?: boolean
  right?: ReactNode
  titleClassName?: string
  /** Horizontal inset of a centred title block. */
  titleInset?: number
  className?: string
}

/** Back button + two-line title + trailing controls. */
export function NavHeader({ title, subtitle, centered, right, titleClassName = 'text-[14.5px] leading-[18px] font-semibold', titleInset = 100, className }: NavHeaderProps) {
  return (
    <div className={cn('absolute inset-x-0 top-[58px] z-30 h-[44px]', className)}>
      <HaloButton icon={ChevronLeft} iconSize={24} className="absolute top-0 left-[15px]" />
      <div
        className={cn('absolute top-[7px] min-w-0', centered ? 'text-center' : 'right-[110px] left-[72px]')}
        style={centered ? { left: titleInset, right: titleInset } : undefined}
      >
        <div className={cn('truncate text-[#1f2328]', titleClassName)}>{title}</div>
        {subtitle && <div className="truncate text-[11px] leading-[14px] text-[#8c9098]">{subtitle}</div>}
      </div>
      {right && <div className="absolute top-0 right-[17px]">{right}</div>}
    </div>
  )
}
