import { ImagePlaceholder, cn } from '../../../ui'
import type { NavTab } from '../data'
import { theme } from '../theme'

export function BottomNav({ tabs, active }: { tabs: NavTab[]; active: string }) {
  return (
    <nav
      className="absolute inset-x-0 bottom-0 flex h-[87px] items-start rounded-t-[20px] bg-white px-[0px] pt-[11px]"
      style={{ boxShadow: '0 -2px 10px rgba(0,0,0,0.07)' }}
    >
      {tabs.map((t) => {
        const on = t.key === active
        const Icon = t.icon
        return (
          <div key={t.key} className="relative flex flex-1 flex-col items-center gap-[4px]">
            {Icon ? (
              <Icon size={22} strokeWidth={1.6} color="#c5c5c9" fill={t.key === 'like' || t.key === 'my' ? '#c5c5c9' : 'none'} />
            ) : (
              <ImagePlaceholder tone="#111" label="ZIGZAG home mark" className="h-[22px] w-[22px] rounded-[4px]" />
            )}
            {t.dot && <span className="absolute top-[-2px] right-[24px] h-[5px] w-[5px] rounded-full" style={{ background: theme.pink }} />}
            <span className={cn('text-[10.5px]', on ? 'font-semibold text-[#111]' : 'text-[#bdbdc1]')}>{t.label}</span>
          </div>
        )
      })}
    </nav>
  )
}
