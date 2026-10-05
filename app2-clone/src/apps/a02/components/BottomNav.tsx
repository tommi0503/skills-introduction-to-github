import { Briefcase, House, MessageCircle, Search, type LucideIcon } from 'lucide-react'
import { TabBar } from '../../../ui'
import { navItems, profileInitials, type NavKey } from '../data'

const icons: Partial<Record<NavKey, LucideIcon>> = {
  home: House,
  chats: MessageCircle,
  trips: Briefcase,
  explore: Search,
}

function ProfileBadge() {
  return (
    <span className="flex h-[22px] w-[22px] items-center justify-center rounded-full bg-[#dfe9f7] text-[7.5px] font-bold text-[#4b5b78]">
      {profileInitials}
    </span>
  )
}

/** Five-tab bottom navigation; the active tab is solid black and filled. */
export function BottomNav({ active, top }: { active: NavKey; top: number }) {
  return (
    <TabBar
      items={navItems}
      activeKey={active}
      className="absolute inset-x-0 px-[1px]"
      renderItem={(item, on) => {
        const Icon = icons[item.key as NavKey]
        return (
          <div
            className="flex flex-1 flex-col items-center gap-[4px]"
            style={{ position: "relative", top: top + 2, color: on ? '#000' : '#9b9b9f' }}
          >
            <span className="flex h-[24px] items-center">
              {Icon ? <Icon size={23} strokeWidth={on ? 2 : 1.5} fill={on ? '#000' : 'none'} /> : <ProfileBadge />}
            </span>
            <span className="text-[10.5px] leading-none" style={{ fontWeight: on ? 600 : 400 }}>
              {item.label}
            </span>
          </div>
        )
      }}
    />
  )
}
