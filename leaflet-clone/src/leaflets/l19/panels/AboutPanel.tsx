import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { Headline } from '../components/Headline'
import { LineStack } from '../components/LineStack'
import { about } from '../data'
import { fonts, palette } from '../theme'

/** Left panel: team photo over a charcoal "About Us" block. */
export function AboutPanel() {
  return (
    <Panel background={palette.charcoal}>
      <ImagePlaceholder label="team photo" className="absolute" style={{ left: 0, top: 0, width: 480, height: 490 }} tone={palette.photoTone} />
      <Placed x={40} y={591}>
        <Headline size={57} color={palette.onDark}>
          {about.title}
        </Headline>
      </Placed>
      <Placed x={40} y={669} width={398} style={{ color: palette.onDarkSoft }}>
        <LineStack lines={about.lines} justify className={`${fonts.paragraph} text-[19.5px] font-medium leading-[34.5px]`} />
      </Placed>
    </Panel>
  )
}
