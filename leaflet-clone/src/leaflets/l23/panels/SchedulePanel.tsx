import { Panel, Placed } from '../../../ui'
import { BlobCard } from '../../shared-2223/components/BlobCard'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { TimelineItem } from '../components/TimelineItem'
import { schedulePanel as d } from '../data'

export function SchedulePanel() {
  return (
    <Panel>
      <BlobCard x={22} y={40} width={418} height={936} radius="62px 66px 56px 48px / 56px 86px 44px 44px" />
      <SectionTitle top={82} centerX={235} className="text-[34px] text-[#62a871]">
        {d.heading}
      </SectionTitle>
      <Placed x={143} y={168} width={3} height={694} className="bg-[#8cc297]" />
      <Placed x={52} y={153} className="flex flex-col gap-[41px]">
        {d.slots.map((s) => (
          <TimelineItem key={s.time} slot={s} />
        ))}
      </Placed>
    </Panel>
  )
}
