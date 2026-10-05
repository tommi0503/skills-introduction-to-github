import { cn } from '../../../ui'
import type { DockTab } from '../data'
import { gn } from '../theme'

/** Floating capsule tab bar with a grey pill behind the active tab. */
export function Dock({ tabs, active, activeWidth = 98, className }: { tabs: DockTab[]; active: string; activeWidth?: number; className?: string }) {
  return (
    <nav className={cn('flex items-center rounded-full bg-white p-[2px] shadow-[0_2px_16px_rgba(0,0,0,0.09)]', className)}>
      {tabs.map((t) => {
        const on = t.key === active
        const Icon = t.icon
        return (
          <div key={t.key} className={cn('flex h-[56px] flex-col items-center justify-center gap-[4px] pt-[2px] rounded-full', on ? 'shrink-0 bg-[#ececec]' : 'flex-1')} style={on ? { width: activeWidth } : undefined}>
            <Icon size={21} strokeWidth={1.6} fill={on ? gn.folderFront : 'none'} stroke={on ? gn.folderBack : '#222'} />
            <span className="text-[9.5px] font-semibold text-[#222]">{t.label}</span>
          </div>
        )
      })}
    </nav>
  )
}
