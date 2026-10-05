import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { cover } from '../data'
import { RuledHeading } from '../components/RuledHeading'

/** Panel 3 — front cover: campaign kicker, big title, illustration, organisation. */
export function CoverPanel() {
  return (
    <Panel>
      <Placed x={47} y={66} width={381}>
        <RuledHeading className="h-[48px] text-[21px] font-extrabold tracking-[0] text-[#1a1a1a]">{cover.kicker}</RuledHeading>
      </Placed>
      <Placed x={0} y={140} width={474} className="flex flex-col items-center">
        {cover.title.map((l) => (
          <span key={l} className="block text-[80px] font-medium leading-[88px] tracking-[-0.05em] text-[#111]">{l}</span>
        ))}
      </Placed>
      <Placed x={15} y={496} width={455} height={410}>
        <ImagePlaceholder label="children illustration" className="h-full w-full rounded-[40px]" />
      </Placed>
      <Placed x={0} y={946} width={474} className="text-center text-[22px] font-extrabold leading-none tracking-[0.2em] text-[#111]">
        {cover.org}
      </Placed>
    </Panel>
  )
}
