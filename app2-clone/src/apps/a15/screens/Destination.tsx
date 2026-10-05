import { Plus, X } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { ChipRow } from '../components/ChipRow'
import { IconRow } from '../components/IconRow'
import { PlacePin } from '../components/PlacePin'
import { StatusRow } from '../components/StatusRow'
import { chips, destination as d } from '../data'
import { fonts, lyft } from '../theme'

function RingDot({ color }: { color: string }) {
  return <span className="block h-[13px] w-[13px] rounded-full border-[3.5px]" style={{ borderColor: color }} />
}

function LocationBox() {
  return (
    <div className="absolute top-[176px] left-[15px] h-[113px] w-[358px] rounded-[12px] border-[2px]" style={{ borderColor: lyft.border }}>
      <div className="absolute top-[22px] left-[16px]">
        <RingDot color={lyft.purple} />
      </div>
      <div className="absolute top-[7px] left-[46px] text-[13px] leading-[18px] text-[#4a444b]">{d.startLabel}</div>
      <div className="absolute top-[26px] left-[46px] text-[16px] leading-[22px]">{d.start}</div>
      <div className="absolute inset-x-0 top-[54px] h-[1.5px]" style={{ background: lyft.border }} />
      <span className="absolute top-[40px] right-[8px] flex h-[31px] w-[31px] items-center justify-center rounded-full border border-[#8c868d] bg-white">
        <Plus size={20} strokeWidth={1.4} />
      </span>
      <div className="absolute top-[78px] left-[16px]">
        <RingDot color={lyft.magenta} />
      </div>
      <div className="absolute top-[73px] left-[46px] text-[16px] leading-[22px] text-[#76717a]">{d.destPlaceholder}</div>
    </div>
  )
}

export function Destination() {
  return (
    <AppScreen className={fonts.body} style={{ color: lyft.ink }}>
      <StatusRow />
      <X size={26} strokeWidth={1.4} className="absolute top-[73px] left-[13px]" />
      <div className="absolute inset-x-0 top-[74px] text-center text-[17px] font-semibold">{d.title}</div>
      <ChipRow items={chips} height={40} className="top-[127px] left-[15px]" />
      <LocationBox />

      <div className="absolute top-[295px] left-[15px] w-[340px]">
        {d.shortcuts.map(({ key, title, icon: Icon, filled }) => (
          <IconRow
            key={key}
            className="h-[56px]"
            textLeft={39}
            icon={
              filled ? (
                <Icon size={21} strokeWidth={1.4} fill={lyft.magenta} className="text-white" />
              ) : (
                <Icon size={24} strokeWidth={1.4} style={{ color: lyft.magenta }} />
              )
            }
            title={title}
            titleClassName="text-[16px] font-medium"
          />
        ))}
      </div>
      <div className="absolute top-[463px] left-[15px] w-[340px]">
        {d.places.map((p) => (
          <IconRow
            key={p.key}
            className="h-[64px]"
            textLeft={39}
            icon={
              <span className="ml-[3px] pt-[5px]">
                <PlacePin color={lyft.magenta} size={14} />
              </span>
            }
            title={p.title}
            sub={p.address}
            titleClassName="text-[15.5px] leading-[20px] font-medium"
            subClassName="text-[13.5px] leading-[20px] text-[#6a656b]"
          />
        ))}
      </div>
    </AppScreen>
  )
}
