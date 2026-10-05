import { Send } from 'lucide-react'
import { TabBar } from '../../../ui'
import type { NavItem } from '../data'

export interface FloatingNavProps {
  items: NavItem[]
  activeKey: string
  /** Label shown inside the expanded active pill. */
  activeLabel: string
}

/** Black floating capsule nav with an expanded white active pill, plus a detached send button. */
export function FloatingNav({ items, activeKey, activeLabel }: FloatingNavProps) {
  return (
    <div className="absolute top-[759px] left-[19px] flex gap-[8px]">
      <TabBar
        items={items}
        activeKey={activeKey}
        className="h-[61px] w-[283px] rounded-full bg-black px-[5px] text-white"
        renderItem={(item, active) => {
          const Icon = item.icon!
          return active ? (
            <span className="flex h-[51px] w-[112px] shrink-0 items-center justify-center gap-[7px] rounded-full bg-white text-[14px] text-black">
              <Icon size={20} strokeWidth={1.6} />
              {activeLabel}
            </span>
          ) : (
            <span className="flex flex-1 justify-center">
              <Icon size={20} strokeWidth={1.6} />
            </span>
          )
        }}
      />
      <span className="flex h-[61px] w-[61px] items-center justify-center rounded-full bg-black text-white">
        <Send size={20} strokeWidth={1.6} />
      </span>
    </div>
  )
}
