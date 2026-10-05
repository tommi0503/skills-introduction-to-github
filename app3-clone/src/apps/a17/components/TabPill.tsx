import { ImagePlaceholder, cn } from '../../../ui'
import type { Tab } from '../data'

export function TabPill({ tabs, active }: { tabs: Tab[]; active: string }) {
  return (
    <div
      className="absolute top-[764px] left-[20px] flex h-[61px] w-[347px] items-center rounded-full bg-white/85 px-[2px] backdrop-blur"
      style={{ boxShadow: '0 4px 20px rgba(0,0,0,0.10)' }}
    >
      {tabs.map((t) => {
        const Icon = t.icon
        return (
          <div
            key={t.key}
            className={cn(
              'flex h-[57px] flex-1 flex-col items-center justify-center gap-[3px] rounded-full text-[#111]',
              t.key === active && 'bg-[#efefef]',
            )}
          >
            {Icon ? (
              <Icon size={22} strokeWidth={1.9} />
            ) : (
              <ImagePlaceholder className="h-[22px] w-[22px] rounded-full" tone="#3d7cf2" label="AI logo" />
            )}
            <span className="text-[10.5px] leading-none font-bold">{t.label}</span>
          </div>
        )
      })}
    </div>
  )
}
