import { ImagePlaceholder, Panel, Pill, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import { contact as d } from '../data'

export function ContactPanel() {
  return (
    <Panel>
      <Placed x={60} y={55} width={370} height={660}>
        <ImagePlaceholder className="h-full w-full" label="coastal path photo" />
      </Placed>
      <Placed x={0} y={757} width={480} className="flex flex-col items-center">
        <Pill className="h-[35px] rounded-none bg-[#232323] px-[8px] text-[20px] font-bold text-white">{d.label}</Pill>
        <Lines lines={d.lines} className="mt-[11px] text-center font-dm text-[20px] leading-[35.5px] tracking-[2px] text-[#3a3a3a]" />
      </Placed>
    </Panel>
  )
}
