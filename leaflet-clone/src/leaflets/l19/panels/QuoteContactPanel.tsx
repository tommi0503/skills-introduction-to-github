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
      <Placed x={89} y={135} width={314} height={311} className="rounded-[22px]" style={{ background: palette.card, color: palette.ink }}>
        <span className={`${fonts.quote} absolute left-0 right-0 text-center text-[150px] font-black leading-none`} style={{ top: 39 }}>
          ”
        </span>
        <LineStack lines={quote.lines} className="absolute left-0 right-0 top-[130px] text-center text-[34.5px] font-bold leading-[43px]" />
      </Placed>
      <Placed x={97} y={728} className="flex items-center gap-[3px]">
        <ArrowBadge size={56} background={palette.inkSoft} color={palette.paper} />
        <Headline size={59} color={palette.inkSoft}>
          {contact.title}
        </Headline>
      </Placed>
      <Placed x={0} y={835} width={480} style={{ color: palette.inkSoft }}>
        <LineStack lines={contact.lines} className={`${fonts.contact} text-center text-[20.3px] font-medium leading-[35.5px] tracking-[1.5px]`} />
      </Placed>
    </Panel>
  )
}
