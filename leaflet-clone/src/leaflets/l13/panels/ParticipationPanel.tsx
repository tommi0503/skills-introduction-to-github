import { ImagePlaceholder, KeyValueList, Panel, Placed } from '../../../ui'
import { RoundedStripe } from '../../shared-1314/components/RoundedStripe'
import { RuledHeading } from '../../shared-1314/components/RuledHeading'
import { fairTheme as t } from '../../shared-1314/theme'
import { participation as d } from '../data'

const stripeLayers = [
  { color: t.stripe.outline, width: 3 },
  { color: t.stripe.teal, width: 11 },
  { color: t.stripe.outline, width: 3 },
  { color: t.stripe.tan, width: 9 },
  { color: t.stripe.outline, width: 3 },
]

const headingClass = 'font-noto-sans text-[42px] font-medium leading-none tracking-[0.02em]'

/** Left outer panel: stripes ornament, sign-up with QR code, contacts. */
export function ParticipationPanel() {
  return (
    <Panel background={t.slate} style={{ color: t.onSlate }}>
      {d.stripes.map((s) => (
        <RoundedStripe key={s.y} x={0} y={s.y} width={s.width} height={s.height} layers={stripeLayers} fill={t.stripe.fill} />
      ))}

      <RuledHeading x={257} y={333} width={223} ruleY={400} ruleColor={t.ruleOnSlate} className={headingClass}>
        {d.title}
      </RuledHeading>

      <Placed x={300} y={438} width={137} height={133} className="bg-white">
        <ImagePlaceholder className="absolute" style={{ left: 22, top: 20, width: 92, height: 92 }} label="QR code" />
      </Placed>

      <Placed x={41} y={476}>
        <div className="font-noto-sans text-[18px] font-bold leading-none">{d.apply.title}</div>
        <div className="mt-[22px] font-noto-sans text-[17px] leading-[27px]" style={{ color: t.onSlateMuted }}>
          {d.apply.lines.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
      </Placed>

      <RuledHeading x={257} y={691} width={223} ruleY={758} ruleColor={t.ruleOnSlate} className={headingClass}>
        {d.contactTitle}
      </RuledHeading>

      <Placed x={41} y={786} width={420}>
        <KeyValueList
          items={d.contacts.map((c) => ({ key: c.label, label: c.label, value: c.value }))}
          labelWidth={90}
          className="gap-[11px] font-noto-sans"
          rowClassName="items-baseline leading-[28px]"
          labelClassName="text-[18px] font-bold"
          valueClassName="text-[19px] tracking-[0.02em]"
        />
      </Placed>
    </Panel>
  )
}
