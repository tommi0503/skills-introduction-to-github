import { Bike, CalendarDays, CarFront, ChevronRight, Info, Search, Tag, UserRound } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { ChipRow } from '../components/ChipRow'
import { IconRow } from '../components/IconRow'
import { StatusRow } from '../components/StatusRow'
import { chips, home as d } from '../data'
import { fonts, lyft } from '../theme'

const navIcons = [
  { key: 'ride', icon: CarFront, active: true },
  { key: 'bike', icon: Bike },
  { key: 'plans', icon: CalendarDays },
  { key: 'account', icon: UserRound, dot: true },
]

function FloatingNav() {
  return (
    <nav className="absolute top-[762px] left-[65px] flex h-[53px] w-[259px] items-center justify-around rounded-full bg-white px-[8px] shadow-[0_2px_12px_rgba(0,0,0,0.14)]">
      {navIcons.map(({ key, icon: Icon, active, dot }) => (
        <span key={key} className="relative">
          <Icon
            size={24}
            strokeWidth={active ? 2 : 1.4}
            fill={active ? lyft.magenta : 'none'}
            className={active ? 'text-white' : 'text-[#3a333b]'}
            style={active ? { color: lyft.magenta } : undefined}
          />
          {dot && <span className="absolute -top-[1px] right-[-2px] h-[7px] w-[7px] rounded-full bg-[#d0213c]" />}
        </span>
      ))}
    </nav>
  )
}

export function Home() {
  return (
    <AppScreen className={fonts.body} style={{ color: lyft.ink }}>
      <StatusRow />
      <h1 className={cn(fonts.display, 'absolute top-[88px] left-[24px] text-[32px] leading-[40px] font-extrabold tracking-[-1.2px]')}>
        {d.greeting}
      </h1>
      <Tag size={15} strokeWidth={0} fill="#2f7a4c" className="absolute top-[135px] left-[24px] rotate-90" />
      <div className="absolute top-[133px] left-[47px] text-[15.5px] leading-[20.5px] text-[#4a444b]">
        {d.promo.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <Info size={16} strokeWidth={1.6} className="absolute top-[135px] left-[333px] text-[#4a444b]" />

      <div
        className="absolute top-[199px] left-[15px] flex h-[59px] w-[358px] items-center rounded-[12px] border-[2px] pl-[18px]"
        style={{ borderColor: lyft.border }}
      >
        <Search size={20} strokeWidth={3} style={{ color: lyft.magenta }} />
        <span className="ml-[18px] text-[15.5px] text-[#4f4a50]">{d.search}</span>
      </div>
      <ChipRow items={chips} height={38} className="top-[280px] left-[16px]" />

      <div className="absolute top-[328px] left-[24px] w-[340px]">
        {d.shortcuts.map(({ key, title, sub, icon: Icon }) => (
          <IconRow
            key={key}
            className="h-[64px]"
            textLeft={39}
            icon={<Icon size={21} strokeWidth={1.4} fill={lyft.magenta} className="text-white" />}
            title={title}
            sub={sub}
            titleClassName="text-[16px] leading-[20px]"
            subClassName="text-[14px] leading-[20px] text-[#4a444b]"
          />
        ))}
      </div>

      <div className="absolute top-[468px] left-[24px] text-[18px] font-semibold tracking-[-0.2px]">{d.earnTitle}</div>
      <div className="absolute top-[507px] left-[23px] w-[345px]">
        {d.rewards.map((r) => (
          <IconRow
            key={r.key}
            className={r.title.length > 1 ? 'h-[106px]' : 'h-[73px]'}
            textLeft={64}
            icon={<ImagePlaceholder label={r.key} className="h-[48px] w-[48px] rounded-full" />}
            title={r.title.map((l) => (
              <div key={l}>{l}</div>
            ))}
            sub={r.sub.map((l) => (
              <div key={l}>{l}</div>
            ))}
            trailing={<ChevronRight size={20} strokeWidth={1.6} className="text-[#3a333b]" />}
            titleClassName="text-[15.5px] leading-[20px] font-medium"
            subClassName="text-[13.5px] leading-[19px] text-[#6a656b]"
          />
        ))}
      </div>
      <div className="absolute top-[780px] left-[24px] text-[18px] font-semibold text-[#d5d3d6]">{d.peek}</div>
      <FloatingNav />
    </AppScreen>
  )
}
