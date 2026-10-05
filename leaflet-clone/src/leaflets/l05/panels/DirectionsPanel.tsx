import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { SectionHeading } from '../components'
import { content } from '../data'
import { theme } from '../theme'

const X = 55

/** Inside-middle: 선착장 오시는 길 (photo is drawn by the sheet overlay). */
export function DirectionsPanel() {
  const { directions } = content
  return (
    <Panel style={{ color: theme.ink }}>
      <SectionHeading x={X} y={603} className="font-normal">
        {directions.heading}
      </SectionHeading>
      <ImagePlaceholder label="pier map line art" className="absolute" style={{ left: X, top: 660, width: 224, height: 174 }} />
      <Placed x={197} y={661} className="font-noto-sans text-[15px] font-bold leading-[24px]">
        {directions.pier}
      </Placed>
      <TextLines
        className="absolute font-noto-sans text-[16px]"
        style={{ left: X, top: 864, color: theme.muted }}
        lines={[directions.address]}
        lineClassName="leading-[28px]"
      />
      <TextLines
        className="absolute font-noto-sans text-[16px]"
        style={{ left: X, top: 914, color: theme.muted }}
        lines={directions.transit}
        lineClassName="leading-[27px]"
      />
    </Panel>
  )
}
