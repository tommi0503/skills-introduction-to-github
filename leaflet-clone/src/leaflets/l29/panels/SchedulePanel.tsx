import { Panel, Placed } from '../../../ui'
import { LeafHeading } from '../../shared-2829/components/LeafHeading'
import { autumn } from '../../shared-2829/theme'
import { ScheduleTable } from '../components/ScheduleTable'
import { schedule } from '../data'

/** Panel 1 — performance timetable and contact. */
export function SchedulePanel() {
  return (
    <Panel>
      <Placed x={55} y={63}>
        <LeafHeading title={schedule.title} titleClassName="text-[24px]" />
      </Placed>
      <Placed x={50} y={135}>
        <ScheduleTable width={388} />
      </Placed>
      <Placed x={50} y={883} className="text-[13px] font-medium leading-[25px]" style={{ color: autumn.footer }}>
        {schedule.footer.map((l, i) => (
          <p key={i} className="m-0 whitespace-pre">
            {l}
          </p>
        ))}
      </Placed>
    </Panel>
  )
}
