import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { DisplayLine } from '../../shared-1718/components/DisplayLine'
import { LabeledLine } from '../../shared-1718/components/LabeledLine'
import { fonts, outsidePalette as c } from '../../shared-1718/theme'
import { cover } from '../data'

/** Front cover: big festival title, tagline, date, illustration and venue line. */
export function CoverPanel() {
  return (
    <Panel background={c.periwinkle}>
      {cover.title.map((line) => (
        <DisplayLine key={line.text} line={line} color={c.yellow} className={fonts.display} />
      ))}
      <ImagePlaceholder label="sparkle" className="absolute" style={{ left: 395, top: 150, width: 42, height: 48 }} />
      <Placed x={0} y={472} width={480} className="text-center" style={{ color: c.onPeriwinkle }}>
        <p className="m-0 text-[22.5px] font-bold leading-[30px]">{cover.tagline}</p>
        <p className="m-0 text-[19px] leading-[34px]" style={{ color: c.onPeriwinkleSoft }}>
          {cover.date}
        </p>
      </Placed>
      <ImagePlaceholder label="reading children illustration" className="absolute" style={{ left: 58, top: 655, width: 282, height: 270 }} />
      <Placed x={0} y={946} width={480} style={{ color: c.onPeriwinkleSoft }}>
        <LabeledLine items={cover.footer} gap={16} className="justify-center text-[15.5px]" labelClassName="font-bold" />
      </Placed>
    </Panel>
  )
}
