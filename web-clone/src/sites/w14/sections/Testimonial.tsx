import { ImagePlaceholder } from '../../../ui'
import { testimonial } from '../data'
import { colors, fonts } from '../theme'
import { Lines, PillButton, Text } from '../components/primitives'

/** Customer quote with portrait card. */
export function Testimonial({ height }: { height: number }) {
  return (
    <section className={`flex justify-center pt-[82px] pl-0 ${fonts.sans}`} style={{ height }}>
      <div className="flex h-[219px] w-[174px] shrink-0 flex-col items-center overflow-hidden rounded-[10px] border" style={{ borderColor: colors.border, background: colors.subtle }}>
        <ImagePlaceholder label="customer portrait" style={{ width: 174, height: 174 }} />
        <ImagePlaceholder label="bunq logo" className="mt-[10px]" style={{ width: 59, height: 25 }} />
      </div>
      <div className="ml-[40px] w-[552px] whitespace-nowrap">
        <Text role="card" as="h4">
          <Lines lines={testimonial.quote} />
        </Text>
        <p className="mt-[9px] flex text-[16px] leading-[24px] font-medium" style={{ color: colors.muted }}>
          <span>{testimonial.author},</span>
          <span className="ml-[5px]">{testimonial.role}</span>
          <span className="ml-[8px]" style={{ color: colors.ink }}>
            {testimonial.company}
          </span>
        </p>
        <PillButton arrow className="mt-[22px]">
          {testimonial.cta}
        </PillButton>
      </div>
    </section>
  )
}
