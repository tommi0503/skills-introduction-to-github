import { ImagePlaceholder, TabBar, cn } from '../../../ui'
import { navEntries } from '../data'
import { palette } from '../theme'

/** White pill navigation: black home bubble, brand orb in the centre. */
export function BottomNav({ activeKey = 'home' }: { activeKey?: string }) {
  return (
    <TabBar
      className="h-[67px] w-[317px] justify-between rounded-full bg-white pl-[3px] pr-[18px]"
      items={navEntries.map((e) => ({ key: e.key, icon: e.icon }))}
      activeKey={activeKey}
      renderItem={(item, active) => {
        const entry = navEntries.find((e) => e.key === item.key)!
        if (entry.orb) return <ImagePlaceholder label="Gradient orb" className="h-[56px] w-[56px] rounded-full" />
        const Icon = item.icon!
        return (
          <span
            className={cn(
              'flex items-center justify-center rounded-full',
              active ? 'h-[56px] w-[56px] bg-[#121617] text-white' : 'h-[40px] w-[40px]',
            )}
            style={!active ? { color: entry.accent ? palette.navAccent : palette.ink } : undefined}
          >
            <Icon size={active ? 21 : 24} strokeWidth={active ? 2.4 : 1.8} fill={active ? 'currentColor' : 'none'} />
          </span>
        )
      }}
    />
  )
}
