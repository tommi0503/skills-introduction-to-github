import { Pause } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { customers } from '../data'
import { SectionHeading } from '../components/Heading'

/** Section origin in page coordinates; child positions below are page-relative minus this. */
const TOP = 1843

function Tabs() {
  return (
    <div className="absolute left-[120px] h-[77px] w-[1200px] overflow-hidden border-y border-[#f0f0f0]" style={{ top: 1991 - TOP }}>
      {[148, 170, 192].map((x) => (
        <span key={x} className="absolute top-[30px] size-[15px] rounded-full border border-[#ececec]" style={{ left: x - 120 - 7 }} />
      ))}
      <span className="absolute left-[113px] top-[16px] h-[42px] w-[104px] rounded-[6px] border border-[#ececec] bg-white" />
      <span className="absolute bottom-0 left-[100px] h-[2px] w-[129px] bg-[#ff7038]" />
      {customers.tabs.map((t) => (
        <span
          key={t.name}
          className={cn(
            'absolute top-[29px] flex items-center gap-2 text-[14px] font-medium leading-[16.1px] tracking-[-0.14px]',
            t.active ? 'text-[#262626]' : 'text-[#707070]',
          )}
          style={{ left: t.x - 120 - 34 }}
        >
          <ImagePlaceholder label={`${t.name} logo`} className="size-6" />
          <span className="ml-[2px]">{t.name}</span>
        </span>
      ))}
      <div className="absolute right-0 top-0 h-full w-[60px] bg-gradient-to-l from-white to-white/0" />
    </div>
  )
}

function Quote() {
  return (
    <figure
      className="absolute left-[201px] h-[275px] w-[1038px] rounded-[8px] border border-dashed border-[#e9e9e9] bg-[#fdfdfc]"
      style={{ top: 2148 - TOP }}
    >
      <blockquote className="relative ml-[47px] mt-[36px] text-[32px] font-medium leading-[32px] tracking-[-0.8px] text-[#262626]">
        <span className="absolute -left-4 top-0 text-[24px]">“</span>
        {customers.quote.map((l, i) => (
          <span key={l} className="block">
            {l}
            {i === customers.quote.length - 1 && <span className="ml-[6px] text-[24px]">”</span>}
          </span>
        ))}
      </blockquote>
      <figcaption className="ml-[47px] mt-[26px] text-[16px] leading-[19.2px] tracking-[-0.04px] text-[#707070]">
        <strong className="font-medium text-[#262626]">{customers.author}</strong>, {customers.role}, {customers.company}
      </figcaption>
      <ImagePlaceholder label="Shopify logo" className="absolute left-[882px] top-[67px] h-[97px] w-[82px]" />
      <ImagePlaceholder label="Portrait" className="absolute left-[842px] top-[132px] size-[64px] rounded-full border-2 border-white" />
    </figure>
  )
}

export function Customers() {
  return (
    <section className="relative h-[930px]">
      <SectionHeading title={customers.title} body={customers.body} gap={31} className="pt-[6px]" />
      <Tabs />
      <span
        className="absolute left-[137px] flex size-9 items-center justify-center rounded-full border border-[#ececec]"
        style={{ top: 2081 - TOP }}
      >
        <Pause className="size-3 fill-[#262626] text-[#262626]" strokeWidth={2} />
      </span>
      <Quote />
      <p
        className="absolute inset-x-0 text-center text-[19.2px] leading-[23.04px] tracking-[-0.48px] text-[#262626]/70"
        style={{ top: 2463 - TOP }}
      >
        {customers.more}
      </p>
      {customers.logos.map((l) => (
        <ImagePlaceholder key={l.x} label="Customer logo" className="absolute" style={{ left: l.x, top: l.y - TOP, width: l.w, height: l.h }} />
      ))}
    </section>
  )
}
