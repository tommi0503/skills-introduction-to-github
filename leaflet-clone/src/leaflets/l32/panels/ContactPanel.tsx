import { KeyValueList, Panel, Placed } from '../../../ui'
import { BrandMark } from '../../shared-3233/components/BrandMark'
import { SectionHeading } from '../../shared-3233/components/SectionHeading'
import { hutech } from '../../shared-3233/theme'
import { brand, contact, copyright, website } from '../data'

const heading = 'text-[19px] leading-[22px]'

/** Middle outside panel (front cover of the back): logo lock-up, contact list, website + QR, copyright. */
export function ContactPanel() {
  return (
    <Panel background={hutech.navy} className="font-noto-sans" style={{ color: hutech.onNavy }}>
      <Placed x={5} y={110} width={480} className="flex flex-col items-center">
        <BrandMark size={80} />
        <p className="m-0 mt-[17px] text-[32px] font-bold leading-[40px]">{brand.name}</p>
        <p className="m-0 mt-[1px] text-[16px] leading-[20px]" style={{ color: hutech.onNavySoft }}>
          {brand.latin}
        </p>
      </Placed>

      <Placed x={52} y={359} width={386}>
        <SectionHeading title={contact.title} color={hutech.accent} titleClassName={heading} gap={13} />
        <KeyValueList
          items={contact.rows.map((r) => ({ key: r.label, label: r.label, value: r.value }))}
          labelWidth={79}
          className="mt-[13px] text-[16px] leading-[33px]"
          labelClassName="font-bold"
          valueClassName="whitespace-pre-line"
        />
      </Placed>

      <Placed x={52} y={583} width={386}>
        <SectionHeading title={website.title} color={hutech.accent} titleClassName={heading} gap={13} />
        <p className="m-0 mt-[20px] text-[17px] leading-[24px]">{website.url}</p>
        <div
          className="mt-[13px] flex h-[119px] w-[118px] items-center justify-center whitespace-pre-line text-center text-[15px] leading-[20px]"
          style={{ background: hutech.paper, color: hutech.inkSoft }}
        >
          {website.qrLabel}
        </div>
        <p className="m-0 mt-[8px] w-[118px] text-center text-[15px] leading-[20px]" style={{ color: hutech.onNavySoft }}>
          {website.qrCaption}
        </p>
      </Placed>

      <Placed x={5} y={946} width={480} className="text-center text-[16.4px] leading-[24px]">
        {copyright}
      </Placed>
    </Panel>
  )
}
