import { Lines } from '../../shared-0812'
import type { InfoSection } from '../data'

/** Heading (optional outline icon), bold lead lines or a price table, then notes. */
export function GuideSection({ section }: { section: InfoSection }) {
  const Icon = section.icon
  return (
    <section className="text-[#2d3a6c]">
      <div className="flex h-[54px] items-center gap-[16px]">
        {Icon && (
          <span className="flex h-[50px] w-[52px] items-center justify-center">
            <Icon size={46} strokeWidth={1.6} />
          </span>
        )}
        <h3 className="m-0 font-noto-sans text-[23.5px] font-bold">{section.title}</h3>
      </div>
      {section.lead && <Lines lines={section.lead} className="mt-[4px] text-[15.5px] leading-[23px] font-bold" />}
      {section.rows && (
        <dl className="m-0 mt-[4px] text-[15.5px] leading-[23px]">
          {section.rows.map((r) => (
            <div key={r.label} className="flex">
              <dt className="w-[85px] font-bold">{r.label}</dt>
              <dd className="m-0 font-medium">{r.value}</dd>
            </div>
          ))}
        </dl>
      )}
      <Lines lines={section.notes} className="mt-[11px] text-[15px] leading-[22px] text-[#4f5a80]" />
    </section>
  )
}
