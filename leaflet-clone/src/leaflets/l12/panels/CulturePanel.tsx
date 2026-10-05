import { Panel, Placed } from '../../../ui'
import { SightItem } from '../components/SightItem'
import { culture as d } from '../data'

export function CulturePanel() {
  return (
    <Panel>
      <Placed x={62} y={58} className="flex items-baseline gap-[10px] text-[#232323]">
        <span className="inline-block w-[88px] origin-left scale-x-[1.42] font-archivo-black text-[44px] leading-[46px]">{d.number}</span>
        <span className="text-[26.5px] leading-[30px] tracking-[1px] font-medium">{d.title}</span>
      </Placed>
      <Placed x={51} y={136} className="flex flex-col gap-[31px]">
        {d.sights.map((s) => (
          <SightItem key={s.name} sight={s} />
        ))}
      </Placed>
    </Panel>
  )
}
