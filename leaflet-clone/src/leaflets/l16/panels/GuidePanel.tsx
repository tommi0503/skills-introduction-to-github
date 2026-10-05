import { Panel, Placed } from '../../../ui'
import { EyebrowHeading } from '../../shared-1516/components/EyebrowHeading'
import { LabeledRows } from '../../shared-1516/components/LabeledRows'
import { Lines } from '../../shared-1516/components/Lines'
import { concertTheme as t } from '../../shared-1516/theme'
import { GuideIcon } from '../components/GuideIcon'
import { guide as d } from '../data'

/** Inside right panel: visitor guide, next concert box and contacts. */
export function GuidePanel() {
  return (
    <Panel background={t.paper} style={{ color: t.body }}>
      <Placed x={61} y={55}>
        <EyebrowHeading eyebrow={d.eyebrow} title={d.title} eyebrowColor="#5a4a4a" titleColor={t.heading} />
      </Placed>

      <Placed x={48} y={124} width={384}>
        {d.items.map((item, i) => (
          <div
            key={item.title}
            className="flex items-center"
            style={{ paddingTop: 30, paddingBottom: 33, borderTop: i ? `2px solid ${t.rule}` : undefined }}
          >
            <div className="mr-[4px] flex w-[96px] shrink-0 items-center justify-center">
              <GuideIcon item={item} size={50} />
            </div>
            <div>
              <div className="text-[16px] font-bold leading-[24px]" style={{ color: t.ink }}>
                {item.title}
              </div>
              <Lines lines={item.lines} className="mt-[2px] text-[13.5px] leading-[21px]" />
            </div>
          </div>
        ))}
      </Placed>

      <Placed x={36} y={634} width={408} height={198} className="rounded-[13px] text-center" style={{ background: t.creamBox }}>
        <div className={`${t.font.display} mt-[33px] text-[25px] leading-[30px]`} style={{ color: t.heading }}>
          {d.next.title}
        </div>
        <div className="mt-[15px] text-[16.5px] font-semibold leading-[24px]" style={{ color: t.ink }}>
          {d.next.headline}
        </div>
        <div className="mt-[5px] text-[16.5px] leading-[24px]">{d.next.detail}</div>
        <div className="mt-[15px] text-[12px] leading-[18px]">{d.next.note}</div>
      </Placed>

      <Placed x={61} y={878} className="text-[19px] font-bold leading-[26px]" style={{ color: t.heading }}>
        {d.contactTitle}
      </Placed>
      <Placed x={61} y={920} width={400}>
        <LabeledRows
          rows={d.contacts.map((c) => ({
            label: c.label,
            value: (
              <>
                {c.value}
                {c.extra && <span className="ml-[10px] text-[12px] text-[#777]">{c.extra}</span>}
              </>
            ),
          }))}
          labelWidth={80}
          className="gap-[7px]"
          rowClassName="items-baseline leading-[24px]"
          labelClassName="text-[16px] font-bold text-[#3f3434]"
          valueClassName="text-[15.5px]"
        />
      </Placed>
    </Panel>
  )
}
