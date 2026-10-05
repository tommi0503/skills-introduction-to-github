import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import { cover as d } from '../data'

export function CoverPanel() {
  return (
    <Panel>
      <Placed x={31} y={73}>
        <Lines lines={d.title} className="font-archivo-black text-[67px] leading-[67px] origin-left scale-x-[1.2] text-[#1e1e1e]" />
      </Placed>
      <Placed x={0} y={226} width={480}>
        <Divider color="#1e1e1e" thickness={4} />
      </Placed>
      <Placed x={0} y={246} width={480} className="text-center text-[25px] leading-[30px] tracking-[1px] font-semibold text-[#232323]">
        {d.subtitle}
      </Placed>
      <Placed x={0} y={297} width={480} height={721}>
        <ImagePlaceholder className="h-full w-full" label="island sea photo" />
      </Placed>
    </Panel>
  )
}
