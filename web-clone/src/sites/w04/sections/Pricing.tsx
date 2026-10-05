import { ImagePlaceholder, cn } from '../../../ui'
import { pricing, type Plan } from '../data'
import { theme } from '../theme'
import { SectionHeading } from '../components/Heading'
import { Chip, Pill } from '../components/Pill'
import { Corners } from '../components/Dashed'

const TOP = 3554

function TabSwitch() {
  return (
    <div className="mx-auto mt-[80px] flex h-[50px] w-[562px] items-center gap-1 rounded-full border border-[#ececec] px-1">
      {pricing.tabs.map(({ label, icon: Icon, active }) => (
        <span
          key={label}
          className="flex h-10 items-center gap-2 rounded-full px-[14px] text-[16px] font-medium tracking-[-0.16px]"
          style={active ? { background: theme.color.orange, color: '#fff' } : { color: theme.color.ink }}
        >
          <Icon className="size-5" strokeWidth={1.5} />
          {label}
        </span>
      ))}
    </div>
  )
}

function Flow() {
  const f = pricing.flow
  return (
    <div className="absolute left-[617px] top-[41px] h-[168px] w-[541px] rounded-[4px] border border-[#f0f0f0] px-6 pt-[24px] text-[14px] leading-[16.1px] tracking-[-0.14px]">
      <div className="flex justify-between">
        <span className="text-[#707070]">{f.from}</span>
        <span style={{ color: theme.color.orange }}>{f.to}</span>
      </div>
      <div className="mt-[12px] flex gap-3">
        {f.layers.map(({ label, icon: Icon }) => (
          <span
            key={label}
            className="flex h-[61px] w-[89px] flex-col items-center justify-center gap-[6px] rounded-[4px] border border-dashed border-[#ececec] text-[#262626]"
          >
            <Icon className="size-4" strokeWidth={1.5} />
            {label}
          </span>
        ))}
      </div>
      <p className="mt-[14px] text-center text-[#727272]">{f.caption}</p>
      <Corners x={0} y={0} w={540} h={167} />
    </div>
  )
}

function PlanColumn({ plan, first }: { plan: Plan; first: boolean }) {
  return (
    <div className={cn('relative h-full w-[300px] px-8 pt-[32px]', !first && 'border-l border-[#f0f0f0]')}>
      <strong className="block text-[16px] font-medium leading-[19.2px] tracking-[-0.04px] text-[#262626]">{plan.name}</strong>
      <span className="block text-[16px] leading-[19.2px] tracking-[-0.04px] text-[#262626]/70">{plan.tagline}</span>
      <div className="mt-[24px] flex items-baseline gap-1">
        <h4 className="text-[32px] font-medium leading-8 tracking-[-0.8px] text-[#262626]">{plan.price}</h4>
        {plan.unit && <small className="text-[14px] tracking-[-0.14px] text-[#707070]">{plan.unit}</small>}
      </div>
      {plan.note && <small className="mt-1 block text-[14px] leading-[16.1px] tracking-[-0.14px] text-[#707070]">{plan.note}</small>}
      <div className="mt-[24px] space-y-[6px]">
        {plan.features.map((row) => (
          <div key={row.join()} className="flex gap-[6px]">
            {row.map((f) => (
              <Chip key={f}>{f}</Chip>
            ))}
          </div>
        ))}
      </div>
      <Pill className="absolute left-8 top-[253px]">{plan.cta}</Pill>
    </div>
  )
}

export function Pricing() {
  return (
    <section className="relative h-[946px] pt-[30px]">
      <SectionHeading title={pricing.title} body={pricing.body} size={56} gap={16} />
      <TabSwitch />
      <div className="absolute left-[120px] h-[629px] w-[1200px] border-y border-[#f0f0f0]" style={{ top: 3839 - TOP }}>
        <div className="relative h-[250px] border-b border-[#f0f0f0]">
          <div className="absolute left-[41px] top-[81px] w-[400px]">
            <h3 className="text-[18px] font-medium leading-[21.6px] tracking-[-0.45px] text-[#262626]">{pricing.intro.title}</h3>
            <p className="mt-[7px] text-[16px] leading-[19.2px] tracking-[-0.04px] text-[#262626]/70">{pricing.intro.body}</p>
          </div>
          <Flow />
        </div>
        <div className="flex h-[322px]">
          {pricing.plans.map((p, i) => (
            <PlanColumn key={p.name} plan={p} first={i === 0} />
          ))}
        </div>
        <ImagePlaceholder label="Dotted pattern" tone="#fcfcfb" className="h-[55px] w-full border-t border-[#f0f0f0]" />
      </div>
      <Corners x={120} y={3839 - TOP} w={1199} h={628} />
    </section>
  )
}
