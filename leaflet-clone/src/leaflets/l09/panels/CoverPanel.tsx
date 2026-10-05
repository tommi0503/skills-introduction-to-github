import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import { StackTitle } from '../components/StackTitle'
import { coverPanel as d } from '../data'

export function CoverPanel() {
  return (
    <Panel>
      <Placed x={28} y={48} className="text-[31px] leading-[40px] text-[#2b2b2b]">
        {d.lead}
      </Placed>
      <Placed x={419} y={52}>
        <StackTitle text={d.heading} wordGap={0} />
      </Placed>
      <Placed x={28} y={356}>
        <Lines lines={d.org} className="text-[15.5px] leading-[25px] text-[#333]" />
      </Placed>
      <Placed x={27} y={420} width={424} height={570}>
        <ImagePlaceholder className="h-full w-full" label="temple roof photo" />
      </Placed>
    </Panel>
  )
}
