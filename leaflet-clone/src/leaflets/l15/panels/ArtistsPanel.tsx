import { Panel, PANEL, Placed } from '../../../ui'
import { ArtistCard } from '../../shared-1516/components/ArtistCard'
import { EyebrowHeading } from '../../shared-1516/components/EyebrowHeading'
import { Lines } from '../../shared-1516/components/Lines'
import { concertTheme as t } from '../../shared-1516/theme'
import { artists as d } from '../data'

/** Inside-flap panel introducing the performers. */
export function ArtistsPanel() {
  return (
    <Panel background={t.paper} style={{ color: t.body }}>
      <Placed x={57} y={55}>
        <EyebrowHeading eyebrow={d.eyebrow} title={d.title} eyebrowColor="#5a4a4a" titleColor={t.heading} />
      </Placed>
      {d.list.map((a) => (
        <ArtistCard key={a.name} artist={a} panelWidth={PANEL.width} inset={a.side === 'left' ? 25 : 18} height={192} photoSize={157} />
      ))}
      <Placed x={57} y={892}>
        <Lines lines={d.closing} className={`${t.font.display} text-[23px] leading-[30px] tracking-[0.07em] text-[#3d3535]`} />
      </Placed>
    </Panel>
  )
}
