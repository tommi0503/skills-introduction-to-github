import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { LabeledLine } from '../../shared-1718/components/LabeledLine'
import { fonts, outsidePalette as c } from '../../shared-1718/theme'
import { cover } from '../data'

/** Front cover: big festival title, tagline, date, illustration and venue line. */
export function CoverPanel() {
  return (
    <Panel background={c.periwinkle}>
      <div className={`${fonts.display} absolute flex flex-col items-center`} style={{ left: 0, right: 0, top: 62, color: c.yellow }}>
        {cover.title.map((line) => (
          <p key={line} className="m-0 text-[126px] leading-[124px]">
            {line}
          </p>
        ))}
      </div>
      <ImagePlaceholder label="sparkle" className="absolute" style={{ left: 395, top: 150, width: 42, height: 48 }} />
      <Placed x={0} y={469} width={480} className="text-center" style={{ color: c.onPeriwinkle }}>
        <p className="m-0 text-[21px] font-semibold leading-[30px]">{cover.tagline}</p>
        <p className="m-0 text-[16.5px] leading-[30px]" style={{ color: c.onPeriwinkleSoft }}>
          {cover.date}
        </p>
      </Placed>
      <ImagePlaceholder label="reading children illustration" className="absolute" style={{ left: 58, top: 655, width: 282, height: 270 }} />
      <Placed x={0} y={946} width={480} style={{ color: c.onPeriwinkleSoft }}>
        <LabeledLine items={cover.footer} gap={22} className="justify-center text-[14px]" labelClassName="font-bold" />
      </Placed>
    </Panel>
  )
}
