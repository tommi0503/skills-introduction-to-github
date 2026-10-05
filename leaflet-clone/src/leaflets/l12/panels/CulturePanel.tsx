import { Panel, Placed } from '../../../ui'
import { SightItem } from '../components/SightItem'
import { culture as d } from '../data'

export function CulturePanel() {
  return (
    <Panel>
      <Placed x={62} y={58} className="flex items-baseline gap-[10px] text-[#232323]">
        <span className="font-archivo-black text-[46px] leading-[46px]">{d.number}</span>
        <span className="text-[25px] leading-[30px] font-semibold">{d.title}</span>
      </Placed>
      <Placed x={51} y={136} className="flex flex-col gap-[31px]">
        {d.sights.map((s) => (
          <SightItem key={s.name} sight={s} />
        ))}
      </Placed>
    </Panel>
  )
}
