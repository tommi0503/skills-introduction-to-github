import { House } from 'lucide-react'
import { TabBar, type TabItem } from '../../../ui'

interface FloatingNavProps {
  items: TabItem[]
  activeKey: string
}

/** Floating white capsule nav; the active tab expands into a black pill with its label. */
export function FloatingNav({ items, activeKey }: FloatingNavProps) {
  return (
    <TabBar
      items={items}
      activeKey={activeKey}
      className="h-[60px] w-[321px] rounded-full bg-white pl-[7px] shadow-[0_4px_20px_rgba(0,0,0,0.06)]"
      renderItem={(item, active) => {
        const Icon = item.icon ?? House
        return active ? (
          <div className="flex h-[47px] mr-[12px] w-[115px] items-center justify-center gap-[10px] rounded-full bg-[#222] text-white">
            <Icon size={20} strokeWidth={0} fill="#fff" />
            <span className="text-[15px] font-semibold">{item.label}</span>
          </div>
        ) : (
          <div className="flex w-[44px] items-center justify-center text-[#2a2a2a]">
            <Icon size={22} strokeWidth={1.5} />
          </div>
        )
      }}
    />
  )
}
