import { Plus } from 'lucide-react'
import { ImagePlaceholder, TabBar } from '../../../ui'
import type { NavItem } from '../data'
import { Floating } from './Floating'

export interface BottomNavProps {
  items: NavItem[]
  activeKey: string
}

/** Floating nav pill + separate "+" button. */
export function BottomNav({ items, activeKey }: BottomNavProps) {
  return (
    <div className="absolute left-[91px] top-[767px] flex items-center gap-[6px]">
      <Floating className="h-[55px] w-[207px] px-[14px]">
        <TabBar
          items={items.map((i) => ({ key: i.key, icon: i.icon }))}
          activeKey={activeKey}
          className="w-full justify-between"
          renderItem={(item, active) => {
            const Icon = item.icon
            return Icon ? (
              <Icon size={24} strokeWidth={active ? 1.9 : 1.5} color={active ? '#111' : '#a9abaf'} />
            ) : (
              <ImagePlaceholder label="profile" tone="#c8cbcf" className="h-[30px] w-[21px] rounded-full" />
            )
          }}
        />
      </Floating>
      <Floating className="h-[54px] w-[54px]">
        <Plus size={26} strokeWidth={1.3} color="#b6b8bc" />
      </Floating>
    </div>
  )
}
