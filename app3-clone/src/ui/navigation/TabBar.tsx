import type { ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface TabItem {
  key: string
  icon?: LucideIcon
  label?: ReactNode
  /** Custom node in place of the icon (e.g. placeholder logo, FAB). */
  node?: ReactNode
}

export interface TabBarProps {
  items: TabItem[]
  activeKey?: string
  /** Render strategy for one tab — lets each app define its look without changing TabBar. */
  renderItem: (item: TabItem, active: boolean) => ReactNode
  className?: string
}

/** Layout-only bottom navigation; visuals come from renderItem (Open/Closed). */
export function TabBar({ items, activeKey, renderItem, className }: TabBarProps) {
  return (
    <nav className={cn('flex items-center', className)}>
      {items.map((item) => (
        <div key={item.key} className="contents">
          {renderItem(item, item.key === activeKey)}
        </div>
      ))}
    </nav>
  )
}

export interface DefaultTabProps {
  item: TabItem
  active: boolean
  activeClassName?: string
  inactiveClassName?: string
  className?: string
  iconSize?: number
  strokeWidth?: number
  labelClassName?: string
}

/** Common "icon above label" tab cell. */
export function IconLabelTab({
  item,
  active,
  activeClassName,
  inactiveClassName,
  className,
  iconSize = 22,
  strokeWidth = 1.8,
  labelClassName,
}: DefaultTabProps) {
  const Icon = item.icon
  return (
    <div
      className={cn('flex flex-1 flex-col items-center justify-center', className, active ? activeClassName : inactiveClassName)}
    >
      {item.node ?? (Icon && <Icon size={iconSize} strokeWidth={strokeWidth} />)}
      {item.label && <span className={labelClassName}>{item.label}</span>}
    </div>
  )
}
