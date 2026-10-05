import { ImagePlaceholder } from '../../../ui'
import { region } from '../data'
import { SectionHeading } from '../components/Heading'
import { Corners } from '../components/Dashed'

export function Region() {
  return (
    <section className="relative h-[1003px]">
      <SectionHeading title={region.title} body={region.body} gap={21} className="pt-[98px]" />
      <ImagePlaceholder label="Dotted globe" className="absolute left-[230px] top-[203px] h-[500px] w-[980px]" />
      <div className="absolute left-[120px] top-[703px] flex h-[193px] w-[1200px] border-y border-[#f0f0f0]">
        {region.features.map(({ icon: Icon, title, body }, i) => (
          <div key={title} className={i ? 'w-[400px] border-l border-[#f0f0f0] px-8 pt-8' : 'w-[400px] px-8 pt-8'}>
            <Icon className="size-7 text-[#262626]" strokeWidth={1.5} />
            <h3 className="mt-[13px] text-[18px] font-medium leading-[21.6px] tracking-[-0.45px] text-[#262626]">{title}</h3>
            <p className="mt-[3px] w-[335px] text-[16px] leading-[19.2px] tracking-[-0.25px] text-[#262626]/70">{body}</p>
          </div>
        ))}
      </div>
      <Corners x={120} y={703} w={1199} h={192} />
    </section>
  )
}
