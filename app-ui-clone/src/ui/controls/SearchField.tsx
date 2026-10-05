import type { ReactNode } from 'react'
import { Search, type LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface SearchFieldProps {
  placeholder?: string
  value?: string
  icon?: LucideIcon | null
  iconSize?: number
  iconStrokeWidth?: number
  trailing?: ReactNode
  className?: string
  textClassName?: string
}

/** Static search input (visual). */
export function SearchField({
  placeholder,
  value,
  icon: Icon = Search,
  iconSize = 18,
  iconStrokeWidth = 2,
  trailing,
  className,
  textClassName,
}: SearchFieldProps) {
  return (
    <div className={cn('flex items-center gap-2', className)}>
      {Icon && <Icon size={iconSize} strokeWidth={iconStrokeWidth} className="shrink-0" />}
      <span className={cn('min-w-0 flex-1 truncate', textClassName)}>{value ?? placeholder}</span>
      {trailing}
    </div>
  )
}
