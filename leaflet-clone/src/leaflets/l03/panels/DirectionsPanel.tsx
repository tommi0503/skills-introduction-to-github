import { ImagePlaceholder, Panel, Placed, VerticalText } from '../../../ui'
import { directions } from '../data'
import { blobs, theme } from '../theme'
import { LineBlock } from '../components/LineBlock'

/** Panel 2 — map, directions, SNS call-out. */
export function DirectionsPanel() {
  return (
    <Panel>
      <Placed x={24} y={96}>
        <VerticalText className="text-[31px] leading-[38px] tracking-[0.3em] text-white">{directions.title}</VerticalText>
      </Placed>
      <Placed x={98} y={97} width={316} height={254}>
        <ImagePlaceholder label="map illustration" className="h-full w-full" style={{ clipPath: blobs.mapPath }} />
      </Placed>
      <Placed x={89} y={338} className="flex flex-col gap-[42px]">
        {directions.blocks.map((b) => (
          <LineBlock key={b[0]} lines={b} className="text-[22.5px] leading-[34px] tracking-[0.01em] text-white" />
        ))}
      </Placed>
      <Placed x={0} y={683} width={466}>
        <LineBlock lines={directions.sns} className="text-center text-[28px] leading-[40px] text-white" />
      </Placed>
      <Placed x={51} y={812} width={362} height={91} className="flex items-center justify-center rounded-[50%]" style={{ background: theme.cream }}>
        <LineBlock lines={directions.account} className="text-center text-[24.5px] leading-[34px] text-[#1b1b1b]" />
      </Placed>
    </Panel>
  )
}
