import { navTabs, type NavTab } from '../data'
import { theme } from '../theme'

function NavIcon({ tab, active }: { tab: NavTab; active: boolean }) {
  if (tab.avatarInitial) {
    return (
      <span className="flex h-[24px] w-[24px] items-center justify-center rounded-full bg-[#5f5f63] text-[12px] text-white">
        {tab.avatarInitial}
      </span>
    )
  }
  const Icon = tab.icon!
  return (
    <span className="relative">
      <Icon
        size={22}
        strokeWidth={active ? 2.3 : 1.6}
        className={active ? 'text-[#111]' : 'text-[#3a3a3e]'}
        fill={active ? 'currentColor' : 'none'}
      />
      {tab.badge !== undefined && (
        <span
          className="absolute -top-[7px] -right-[8px] flex h-[14px] min-w-[14px] items-center justify-center rounded-full text-[9px] font-medium text-white"
          style={{ background: theme.badge }}
        >
          {tab.badge}
        </span>
      )}
    </span>
  )
}

export function BottomNav({ active }: { active: string }) {
  return (
    <nav className="absolute inset-x-0 bottom-0 top-[760px] z-10 border-t bg-white" style={{ borderColor: theme.divider }}>
      <div className="grid grid-cols-5 px-[0px] pt-[19px]">
        {navTabs.map((t) => (
          <div key={t.id} className="flex justify-center">
            <NavIcon tab={t} active={t.id === active} />
          </div>
        ))}
      </div>
    </nav>
  )
}
