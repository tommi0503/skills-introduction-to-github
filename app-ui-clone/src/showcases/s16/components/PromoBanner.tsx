import { Sparkles } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'
import { GradientButton } from './GradientButton'

export interface PromoBannerProps {
  eyebrow: string
  /** Headline parts; the highlighted part is rendered dimmer. */
  lines: string[]
  cta: string
}

/** Dark stacked promo card with a product photo on the right. */
export function PromoBanner({ eyebrow, lines, cta }: PromoBannerProps) {
  const [pre, hi, post, line2] = lines
  return (
    <div className="relative mx-[15px] h-[181px]">
      <div className="absolute inset-x-[18px] top-[20px] bottom-0 rounded-[14px] bg-[#4a4a4a]" />
      <div className="absolute inset-x-0 top-0 h-[169px] overflow-hidden rounded-[14px]" style={{ background: theme.dark }}>
        <ImagePlaceholder className="absolute top-0 right-0 h-full w-[140px]" label="shopping bag photo" />
        <div className="absolute top-[16px] left-[16px] flex items-center gap-[6px] text-[12px]" style={{ color: '#d0743c' }}>
          <Sparkles size={15} strokeWidth={1.5} color="#e5e5e5" />
          {eyebrow}
        </div>
        <div className="absolute top-[45px] left-[15px] text-[23px] leading-[28px] font-[450] tracking-[-0.4px] text-white">
          {pre}
          <span className="text-[#a8a8a8]">{hi}</span>
          {post}
          <br />
          {line2}
        </div>
        <GradientButton label={cta} className="absolute top-[117px] left-[15px] h-[37px] w-[100px] text-[14px]" />
      </div>
    </div>
  )
}
