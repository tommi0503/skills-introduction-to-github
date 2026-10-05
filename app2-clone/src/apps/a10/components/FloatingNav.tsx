import { Search, type LucideIcon } from 'lucide-react'
import { cn, TabBar, type TabItem } from '../../../ui'
import { CircleButton } from './CircleButton'

export interface FloatingNavProps {
  items: TabItem[]
  activeKey?: string
  className?: string
  /** width of the tab capsule */
  width: number
  searchIcon?: LucideIcon
  searchSize?: number
  searchClassName?: string
}

/** Frosted tab capsule with the detached search button. */
export function FloatingNav({ items, activeKey, className, width, searchIcon = Search, searchSize = 58, searchClassName }: FloatingNavProps) {
  return (
    <div className={cn('absolute flex items-center justify-between', className)}>
      <div className="relative" style={{ width }}>
        <TabBar
          items={items}
          activeKey={activeKey}
          className="h-[57px] rounded-full bg-white/80 p-[4px] shadow-[0_4px_20px_rgba(0,0,0,0.10)] backdrop-blur-md"
          renderItem={(item, active) => {
            const Icon = item.icon
            return (
              <div
                className={cn(
                  'flex h-full flex-1 flex-col items-center justify-center rounded-full',
                  active ? 'bg-[#ececee] text-[#3b82f6]' : 'text-black',
                )}
              >
                {item.node ?? (Icon && <Icon size={25} strokeWidth={2.3} />)}
                <span className="mt-[2px] text-[10px] leading-[12px] font-semibold">{item.label}</span>
              </div>
            )
          }}
        />
      </div>
      <CircleButton icon={searchIcon} size={searchSize} iconSize={24} strokeWidth={2.2} className={cn('relative bg-white/85', searchClassName)} />
    </div>
  )
}
