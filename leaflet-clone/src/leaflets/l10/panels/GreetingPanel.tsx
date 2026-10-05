import { Panel, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import { greeting as d } from '../data'

export function GreetingPanel() {
  return (
    <Panel>
      <Placed x={72} y={174} className="text-[#2d3a6c]">
        <h2 className="m-0 font-myeongjo text-[25px] leading-[36px] font-extrabold">{d.title}</h2>
        <div className="mt-[19px] flex flex-col gap-[37px] font-myeongjo font-extrabold text-[21.5px] tracking-[1.2px] leading-[37px] text-[#55608a]">
          {d.paragraphs.map((p, i) => (
            <Lines key={i} lines={p} />
          ))}
        </div>
      </Placed>
    </Panel>
  )
}
