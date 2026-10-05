import { ChevronRight, type LucideIcon } from 'lucide-react'

export interface ActionMenuProps {
  groups: { key: string; icon: LucideIcon; label: string }[][]
  buy: string
  sell: string
  top: number
}

/** Frosted trade action sheet: grouped rows with chevrons, then Buy / Sell buttons. */
export function ActionMenu({ groups, buy, sell, top }: ActionMenuProps) {
  return (
    <div
      className="absolute rounded-[22px] bg-white/88 shadow-[0_6px_30px_rgba(0,0,0,0.10)] backdrop-blur-xl"
      style={{ left: 20, right: 20, top, background: 'rgba(250,250,250,0.9)' }}
    >
      <div className="px-[16px] pt-[7px]">
        {groups.map((g, gi) => (
          <div key={gi} className="border-b border-[#e2e2e4] pb-[10px]" style={{ paddingTop: gi ? 9 : 0 }}>
            {g.map(({ key, icon: Icon, label }) => (
              <div key={key} className="flex h-[40px] items-center gap-[15px] pl-[17px] pr-[6px] text-[16.5px]">
                <Icon size={17} strokeWidth={2.2} fill={key === 'send' ? '#111' : 'none'} />
                <span className="flex-1">{label}</span>
                <ChevronRight size={17} strokeWidth={2} />
              </div>
            ))}
          </div>
        ))}
      </div>
      <div className="flex flex-col gap-[11px] px-[17px] pt-[20px] pb-[20px]">
        <div className="flex h-[41px] items-center justify-center rounded-full bg-[#0c0c0c] text-[14.5px] font-medium text-white">{buy}</div>
        <div className="flex h-[41px] items-center justify-center rounded-full bg-[#e9e9eb] text-[14.5px] font-medium">{sell}</div>
      </div>
    </div>
  )
}
