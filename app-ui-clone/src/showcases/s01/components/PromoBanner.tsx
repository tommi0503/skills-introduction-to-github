import { ImagePlaceholder } from '../../../ui'

interface PromoBannerProps {
  title: string[]
  subtitle: string
  cta: string
}

/** Dark promo card: copy + CTA on the left, campaign photo bleeding in from the right. */
export function PromoBanner({ title, subtitle, cta }: PromoBannerProps) {
  return (
    <div className="relative h-[142px] overflow-hidden rounded-[9px] bg-[#0b0d0c]">
      <ImagePlaceholder className="absolute inset-y-0 right-0 w-[122px]" label="promo photo" />
      <div className="relative px-[17px] pt-[18px] text-white">
        {title.map((line) => (
          <div key={line} className="text-[17.4px] leading-[21.5px] font-bold tracking-[-0.2px]">
            {line}
          </div>
        ))}
        <div className="mt-[6px] text-[9.5px] font-medium">{subtitle}</div>
        <button type="button" className="mt-[17px] h-[27px] w-[80px] rounded-[4px] bg-white text-[11.5px] font-semibold text-[#111]">
          {cta}
        </button>
      </div>
    </div>
  )
}
