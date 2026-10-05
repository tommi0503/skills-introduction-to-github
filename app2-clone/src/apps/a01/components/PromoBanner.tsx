import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

export interface PromoBannerProps {
  badge: string
  title: string[]
  cta: string
  top: number
}

/** Patterned promo banner (graphic → placeholder) with a framed serif headline. */
export function PromoBanner({ badge, title, cta, top }: PromoBannerProps) {
  return (
    <div className="absolute" style={{ left: 20, top, width: 350, height: 166 }}>
      <ImagePlaceholder className="absolute inset-0 rounded-[16px]" label="promo pattern" />
      <div
        className="absolute flex flex-col items-center justify-center bg-white font-times text-[24px] leading-[26px] tracking-[-0.3px] text-[#3a3a3a]"
        style={{ left: 50, top: 29, width: 250, height: 109 }}
      >
        {title.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </div>
      <span
        className="absolute rounded-full bg-white px-[8px] py-[4px] text-[10px] leading-none font-bold"
        style={{ left: 16, top: -10, color: theme.badgePink }}
      >
        {badge}
      </span>
      <span
        className="absolute rounded-full px-[11px] py-[8px] text-[13.5px] leading-none font-semibold text-[#2a2a2e]"
        style={{ left: 225, top: 151, background: '#eeedf6' }}
      >
        {cta}
      </span>
    </div>
  )
}
