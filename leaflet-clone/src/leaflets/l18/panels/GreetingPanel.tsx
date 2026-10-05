import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { RoundedBox } from '../../shared-1718/components/RoundedBox'
import { insidePalette as c } from '../../shared-1718/theme'
import { JustifiedLines } from '../components/JustifiedLines'
import { ScheduleList } from '../components/ScheduleList'
import { greeting, schedule } from '../data'

/** Inner left panel: invitation letter on periwinkle, timetable card on cream. */
export function GreetingPanel() {
  return (
    <Panel>
      <Placed x={0} y={0} width={480} height={590} style={{ background: c.periwinkle }} />
      <Placed x={68} y={70} className="text-[20px] font-bold" style={{ color: c.onPeriwinkle }}>
        {greeting.title}
      </Placed>
      <ImagePlaceholder label="sparkles" className="absolute" style={{ left: 165, top: 45, width: 42, height: 56 }} />
      <Placed x={68} y={140} width={348} className="text-[16.8px] font-semibold leading-[29.5px]" style={{ color: c.ink }}>
        <JustifiedLines lines={greeting.lines} />
      </Placed>
      <RoundedBox x={25} y={612} width={427} height={376} radius={12} background={c.card}>
        <p className="absolute m-0 text-[21px] font-bold" style={{ left: 43, top: 35, color: c.accent }}>
          {schedule.title}
        </p>
        <ScheduleList
          items={schedule.items}
          color={c.accentMuted}
          ruleColor={c.rule}
          rowHeight={43}
          className="absolute text-[18.5px] font-medium"
          style={{ left: 43, top: 83, width: 332 }}
        />
      </RoundedBox>
      <ImagePlaceholder label="readers illustration" className="absolute" style={{ left: 230, top: 315, width: 215, height: 310 }} />
      <ImagePlaceholder label="squiggle" className="absolute" style={{ left: 375, top: 710, width: 46, height: 40 }} />
    </Panel>
  )
}
