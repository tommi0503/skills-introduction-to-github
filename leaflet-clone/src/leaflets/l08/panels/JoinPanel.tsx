import { Panel, Placed } from '../../../ui'
import { Shapes } from '../../shared-0812'
import { ActivityItem } from '../components/ActivityItem'
import { RoundCard } from '../components/RoundCard'
import { SectionHeading } from '../components/SectionHeading'
import { joinPanel as d } from '../data'

export function JoinPanel() {
  return (
    <Panel>
      <Placed x={0} y={162} width={480}>
        <SectionHeading
          title={d.title}
          body={[d.subtitle]}
          titleClassName="text-[30px] leading-[40px]"
          bodyClassName="mt-[6px] text-[15px] leading-[20px] tracking-[-0.3px]"
        />
      </Placed>
      <RoundCard x={46} y={292} width={386} height={343} className="flex flex-col items-center pt-[50px]">
        {d.activities.map((a) => (
          <ActivityItem key={a.title} item={a} className="mb-[47px]" />
        ))}
      </RoundCard>
      <RoundCard x={46} y={657} width={386} height={169} className="pt-[34px]">
        <ActivityItem item={d.firstTime} />
      </RoundCard>
      <Shapes items={d.art} />
    </Panel>
  )
}
