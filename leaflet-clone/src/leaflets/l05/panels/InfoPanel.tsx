import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { FareTable } from '../../shared-0407/components/FareTable'
import { TextLines } from '../../shared-0407/components/TextLines'
import { SectionHeading } from '../components'
import { content } from '../data'
import { theme } from '../theme'

const X = 50

/** Inside-left navy panel: 이용 안내, 예약 문의, QR and the fare table. */
export function InfoPanel() {
  const { guide, contact, qrCaption, fares } = content
  return (
    <Panel background={theme.navy} style={{ color: theme.onNavy }}>
      <div className="absolute inset-x-0" style={{ top: 46, height: 2, background: theme.rule, opacity: 0.85 }} />
      <SectionHeading x={X} y={82}>
        {guide.heading}
      </SectionHeading>
      <TextLines
        className="absolute font-noto-sans text-[14px] font-light"
        style={{ left: X + 5, top: 145 }}
        lines={guide.steps.map((s, i) => `${i + 1}. ${s}`)}
        lineClassName="leading-[25px]"
      />
      <SectionHeading x={X} y={282}>
        {contact.heading}
      </SectionHeading>
      <TextLines
        className="absolute font-noto-sans text-[15px] font-light"
        style={{ left: X, top: 338 }}
        lines={contact.lines}
        lineClassName="leading-[29px]"
      />
      <ImagePlaceholder label="QR code" className="absolute" style={{ left: X, top: 480, width: 78, height: 78 }} />
      <TextLines
        className="absolute font-noto-sans text-[15px] font-bold"
        style={{ left: 147, top: 475 }}
        lines={qrCaption}
        lineClassName="leading-[26px]"
      />
      <SectionHeading x={X} y={712}>
        {fares.heading}
      </SectionHeading>
      <Placed x={28} y={782} width={409}>
        <FareTable
          rows={fares.rows}
          columns={fares.columns}
          inlineType
          widths={[124, 91, 87, 107]}
          className="font-noto-sans text-[14px]"
          headCellClassName="h-[40px] font-bold border-l-2 first:border-l-0 border-white/90"
          rowClassName="border-t-2 border-white/90"
          cellClassName="h-[45px] font-light border-l-2 first:border-l-0 border-white/90"
        />
      </Placed>
    </Panel>
  )
}
