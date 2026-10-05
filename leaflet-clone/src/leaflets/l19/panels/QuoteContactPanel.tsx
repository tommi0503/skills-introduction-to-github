import { Panel, Placed } from '../../../ui'
import { ArrowBadge } from '../components/ArrowBadge'
import { Headline } from '../components/Headline'
import { LineStack } from '../components/LineStack'
import { contact, quote } from '../data'
import { fonts, palette } from '../theme'

/** Middle panel: quote card and contact details on light grey. */
export function QuoteContactPanel() {
  return (
    <Panel background={palette.paper}>
      <Placed x={89} y={135} width={314} height={311} className="flex flex-col items-center rounded-[22px]" style={{ background: palette.card }}>
        <span className="mt-[14px] font-archivo-black text-[140px] leading-[140px]" style={{ color: palette.ink, height: 70 }}>
          ”
        </span>
        <LineStack lines={quote.lines} className="mt-[1px] text-center text-[29px] font-bold leading-[43px]" lineClassName="" />
      </Placed>
      <Placed x={97} y={728} className="flex items-center gap-[5px]">
        <ArrowBadge size={56} background={palette.inkSoft} color={palette.paper} />
        <Headline size={64} color={palette.inkSoft}>
          {contact.title}
        </Headline>
      </Placed>
      <Placed x={0} y={835} width={480} style={{ color: palette.inkSoft }}>
        <LineStack lines={contact.lines} className={`${fonts.contact} text-center text-[17.5px] font-semibold leading-[35.5px] tracking-[1.2px]`} />
      </Placed>
    </Panel>
  )
}
