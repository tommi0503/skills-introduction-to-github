import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { PanelFrame, SerifHeading } from '../components'
import { content } from '../data'
import { theme } from '../theme'

/** Inside-middle (navy): 선착장 오시는 길 map, QR and 예약 문의. */
export function DirectionsPanel() {
  const { directions, qrCaption, contact } = content
  return (
    <Panel background={theme.navy} style={{ color: theme.onNavy }}>
      <PanelFrame color={theme.frameOnNavy} />
      <SerifHeading y={66} className="text-[26px] leading-[40px] tracking-[0.12em]">
        {directions.heading}
      </SerifHeading>
      <ImagePlaceholder label="map line art" className="absolute" style={{ left: 110, top: 140, width: 260, height: 186 }} />
      <TextLines
        className="absolute inset-x-0 text-center font-noto-sans text-[17px]"
        style={{ top: 344 }}
        lines={[directions.address]}
        lineClassName="leading-[28px]"
      />
      <TextLines
        className="absolute inset-x-0 text-center font-noto-sans text-[17px]"
        style={{ top: 398 }}
        lines={directions.transit}
        lineClassName="leading-[30px]"
      />
      <ImagePlaceholder label="QR code" className="absolute" style={{ left: 173, top: 548, width: 134, height: 134 }} />
      <Placed x={0} y={703} width={480} className="text-center font-noto-sans text-[19px] font-bold leading-[28px]">
        {qrCaption.join(' ')}
      </Placed>
      <SerifHeading y={802} className="text-[24px] leading-[40px]">
        {contact.heading}
      </SerifHeading>
      <TextLines className="absolute inset-x-0 text-center font-noto-sans text-[17px]" style={{ top: 853 }} lines={contact.lines} lineClassName="leading-[30px]" />
    </Panel>
  )
}
