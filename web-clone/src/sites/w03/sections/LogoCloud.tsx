import { logoCloud } from '../data'
import { Serif } from '../components/Type'

/** Heading over the customer-logo marquee (logos were not rendered at capture time). */
export function LogoCloud() {
  return (
    <section className="h-[701px] pt-[128px]">
      <Serif className="text-center text-[32px] leading-[33.6px] tracking-[0.1px] text-[#0f0e0d]">{logoCloud.title}</Serif>
    </section>
  )
}
