import { ImagePlaceholder, cn } from '../../../ui'
import { theme } from '../theme'

export interface EventBannerProps {
  kicker: string
  before: string
  highlight: string
  after: string
  className?: string
}

/** Full-width grey promo strip with a highlighted amount and a coupon illustration. */
export function EventBanner({ kicker, before, highlight, after, className }: EventBannerProps) {
  return (
    <div
      className={cn('relative h-[87.5px] w-full font-pretendard', className)}
      style={{ background: 'linear-gradient(90deg,#efefef 0%,#e9e9e9 50%,#e2e2e2 100%)' }}
    >
      <div className="absolute top-[20px] left-[29px]">
        <div className="text-[16.5px] leading-[20px] tracking-[-0.4px] text-[#4a4a4a]">{kicker}</div>
        <div className="mt-[3px] text-[20.5px] font-bold leading-[26px] tracking-[-0.5px] text-[#2a2a2a]">
          {before}
          <span className="relative inline-block">
            <span className="absolute inset-x-[-1px] top-[3px] bottom-[2px]" style={{ background: theme.lime }} />
            <span className="relative">{highlight}</span>
          </span>
          {after}
        </div>
      </div>
      <ImagePlaceholder label="쿠폰 일러스트" tone="#cfd2d6" className="absolute top-[14px] left-[272px] h-[57px] w-[84px] rounded-[4px]" />
    </div>
  )
}
