import { Panel, Placed } from '../../../ui'
import { ProgramItem } from '../components/ProgramItem'
import { StackTitle } from '../components/StackTitle'
import { programPanel as d } from '../data'

export function ProgramPanel() {
  return (
    <Panel>
      <Placed x={30} y={50} width={330} className="flex flex-col gap-[29px]">
        {d.items.map((item) => (
          <ProgramItem key={item.title} item={item} />
        ))}
      </Placed>
      <Placed x={416} y={52}>
        <StackTitle text={d.heading} wordGap={15} />
      </Placed>
    </Panel>
  )
}
