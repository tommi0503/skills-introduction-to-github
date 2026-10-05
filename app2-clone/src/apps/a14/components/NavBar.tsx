import { Zap } from 'lucide-react'
import { cn } from '../../../ui'
import type { NavTab } from '../data'
import { nord } from '../theme'

export interface NavBarProps {
  tabs: NavTab[]
  activeKey: string
  /** Status dots per tab key. */
  dots?: Record<string, NavTab['dot']>
  top: number
  className?: string
}

/** Four-icon bottom bar; the active icon sits in a soft grey pill. */
export function NavBar({ tabs, activeKey, dots = {}, top, className }: NavBarProps) {
  return (
    <nav className={cn('absolute inset-x-0 bottom-0 border-t border-[#ececee]', className)} style={{ top }}>
      <div className="flex px-[2px] pt-[10px]">
        {tabs.map(({ key, icon: Icon, bolt }) => {
          const dot = dots[key]
          return (
            <div key={key} className="flex flex-1 justify-center">
              <div
                className={cn('relative flex h-[31px] w-[54px] items-center justify-center rounded-[15px]', key === activeKey && 'bg-[#efeff0]')}
              >
                <Icon size={21} strokeWidth={key === activeKey ? 2.4 : 1.6} className="text-[#2a2a2c]" />
                {bolt && <Zap size={9} strokeWidth={2} fill="#2a2a2c" className="absolute text-[#2a2a2c]" />}
                {dot && (
                  <span
                    className="absolute top-[3px] right-[13px] h-[7px] w-[7px] rounded-full"
                    style={{ background: dot === 'green' ? nord.dot : nord.badge }}
                  />
                )}
              </div>
            </div>
          )
        })}
      </div>
    </nav>
  )
}
