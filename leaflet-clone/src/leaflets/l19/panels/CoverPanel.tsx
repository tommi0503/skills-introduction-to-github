import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { Headline } from '../components/Headline'
import { cover } from '../data'
import { fonts, palette } from '../theme'

/** Right panel (front cover): headline, tagline, team photo, website. */
export function CoverPanel() {
  return (
    <Panel background={palette.charcoalDeep}>
      <Placed x={33} y={98}>
        <Headline size={106} lineHeight={110} color={palette.onDark}>
          {cover.title.map((line) => (
            <span key={line} className="block">
              {line}
            </span>
          ))}
        </Headline>
      </Placed>
      <Placed x={33} y={340} className={`${fonts.body} text-[15.5px]`} style={{ color: palette.onDarkSoft }}>
        {cover.tagline}
      </Placed>
      <ImagePlaceholder label="team photo" className="absolute" style={{ left: 0, top: 515, width: 480, height: 313 }} tone={palette.photoTone} />
      <Placed x={0} y={916} width={480} className={`${fonts.url} text-center text-[17px]`} style={{ color: palette.onDarkSoft }}>
        {cover.website}
      </Placed>
    </Panel>
  )
}
