import { ChipGroup } from '../../../ui'
import { ContinueButton } from '../components/ContinueButton'
import { FlowHeader } from '../components/FlowHeader'
import { MonthCalendar } from '../components/MonthCalendar'
import { dates, durations, months, steps, weekdays } from '../data'

/** Step 2 — pick the travel dates. */
export function DatesScreen() {
  const [august, september] = months
  return (
    <div className="relative h-full w-full">
      <div className="absolute inset-x-[24.4px] top-[57.5px]">
        <FlowHeader step={2} total={steps.total} />
      </div>
      <div className="absolute left-[24.4px] top-[151px]">
        <div className="text-[13.5px] leading-[20px] text-[#8e8e8e]">{dates.eyebrow}</div>
        <div className="mt-[6px] text-[22px] leading-[28px] font-semibold tracking-[-0.3px]">{dates.title}</div>
      </div>
      <ChipGroup
        items={durations}
        activeKey="1w"
        gap={4}
        className="absolute inset-x-[24.4px] top-[225.5px]"
        chipClassName="h-[35px] flex-1 rounded-full text-[12.5px]"
        activeClassName="bg-[#1f1f1f] text-white"
        inactiveClassName="border border-[#ebebeb] bg-white text-[#8e8e8e]"
      />
      <div className="absolute inset-x-[24.4px] top-[284px]">
        <MonthCalendar month={august} weekdays={weekdays} />
      </div>
      <div className="absolute inset-x-[24.4px] top-[603.4px]">
        <MonthCalendar month={september} weekdays={weekdays} fadeFromRow={1} />
      </div>
      <div
        className="pointer-events-none absolute inset-x-0 bottom-0 h-[90px]"
        style={{ background: 'linear-gradient(to bottom, rgba(250,250,250,0), rgba(250,250,250,0.92) 35%, #fafafa)' }}
      />
      <div className="absolute left-[93.75px] top-[715.7px]">
        <ContinueButton label={dates.cta} />
      </div>
    </div>
  )
}
