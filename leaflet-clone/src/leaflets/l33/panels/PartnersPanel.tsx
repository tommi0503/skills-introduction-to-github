import { Panel, Placed } from '../../../ui'
import { LogoGrid } from '../../shared-3233/components/LogoGrid'
import { SectionHeading } from '../../shared-3233/components/SectionHeading'
import { hutech, hutechType } from '../../shared-3233/theme'
import { partners } from '../data'

const heading = 'text-[19.5px] leading-[28px]'

/** Inside right panel: PARTNERS title, success story, partner logo grid and contact callout. */
export function PartnersPanel() {
  return (
    <Panel background={hutech.paper} className="font-noto-sans" style={{ color: hutech.ink }}>
      <Placed x={34} y={64}>
        <h2 className={`m-0 text-[43px] leading-[60px] ${hutechType.display}`} style={{ color: hutech.accent }}>
          {partners.title}
        </h2>
        <p className="m-0 mt-[4px] text-[29.5px] leading-[40px]" style={{ color: hutech.inkSoft }}>
          {partners.subtitle}
        </p>
        <p className="m-0 mt-[24px] whitespace-pre-line text-[20px] font-bold leading-[30px]">{partners.lead}</p>
      </Placed>

      <Placed x={33} y={292} width={400}>
        <SectionHeading title={partners.caseStudy.title} color={hutech.accent} titleClassName={heading} gap={9} />
        <p className="m-0 mt-[16px] whitespace-pre-line text-[16.5px] leading-[26px] tracking-[-0.02em]" style={{ color: hutech.inkSoft }}>
          {partners.caseStudy.body}
        </p>
      </Placed>

      <Placed x={33} y={473} width={400}>
        <SectionHeading title={partners.logos.title} color={hutech.accent} titleClassName={heading} gap={9} />
        <LogoGrid
          count={partners.logos.count}
          columns={partners.logos.columns}
          logoWidth={85}
          logoHeight={28}
          columnGap={63}
          rowGap={27}
          className="mt-[33px] pl-[2px]"
        />
      </Placed>

      <Placed
        x={31}
        y={808}
        width={399}
        height={152}
        className="rounded-[8px] pl-[26px] pt-[24px] whitespace-pre-line text-[17px] leading-[26px]"
        style={{ background: hutech.calloutBg, color: hutech.inkSoft }}
      >
        {partners.callout}
      </Placed>
    </Panel>
  )
}
