import { ImagePlaceholder } from '../../../ui'
import type { ScheduleItem } from '../data'
import { theme } from '../theme'

const LEFT = 67

export function TodayRow({ item }: { item: Extract<ScheduleItem, { kind: 'today' }> }) {
  return (
    <div className="relative h-[77px]">
      <span className="absolute left-[23px] top-[10px] w-[22px] text-center text-[9.5px] font-semibold" style={{ color: theme.blue }}>
        {item.weekday}
      </span>
      <span
        className="absolute left-[15px] top-[23px] flex size-[37px] items-center justify-center rounded-full text-[16px] text-white"
        style={{ background: theme.blue }}
      >
        {item.day}
      </span>
      <span className="absolute top-[18px] text-[13.5px]" style={{ left: LEFT, color: theme.sub }}>{item.text}</span>
      <span className="absolute left-[56px] top-[44px] size-[6px] rounded-full bg-[#202124]" />
      <span className="absolute left-[58px] right-[13px] top-[46.5px] h-[1.2px] bg-[#5f6368]" />
    </div>
  )
}

export function RangeRow({ label }: { label: string }) {
  return (
    <div className="flex h-[37.5px] items-center text-[11px] font-medium tracking-[0.3px]" style={{ paddingLeft: LEFT, color: theme.sub }}>
      {label}
    </div>
  )
}

export function MonthBanner({ label, tone }: { label: string; tone: 'june' | 'july' }) {
  return (
    <div className="relative my-[16px] h-[154px]">
      <ImagePlaceholder label={`${label} illustration`} tone={theme[tone]} className="absolute inset-0" />
      <span className="absolute top-[16px] font-dm text-[19.5px]" style={{ left: LEFT, color: theme.text }}>
        {label}
      </span>
    </div>
  )
}
