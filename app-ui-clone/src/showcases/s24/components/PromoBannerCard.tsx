import { ChevronRight } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { PromoBanner } from '../data'
import { theme } from '../theme'

export interface PromoBannerCardProps {
  banner: PromoBanner
  /** Illustration area on the right (card-relative). */
  art: { x: number; y: number; w: number; h: number }
  className?: string
}

/** Rounded promo banner: two bold lines + circled chevron, illustration placeholder on the right. */
export function PromoBannerCard({ banner, art, className }: PromoBannerCardProps) {
  const last = banner.lines.length - 1
  return (
    <div
      className={cn('relative h-[75px] w-[348px] overflow-hidden rounded-[8px] font-pretendard', className)}
      style={{ background: banner.background }}
    >
      <ImagePlaceholder
        label="배너 일러스트"
        className="absolute"
        style={{ left: art.x, top: art.y, width: art.w, height: art.h }}
      />
      <div className="absolute top-[18px] left-[19px] text-[15.4px] font-semibold leading-[20px] tracking-[-0.3px]" style={{ color: '#1f2440' }}>
        {banner.lines.map((line, i) => (
          <div key={line} className="flex items-center">
            {line}
            {i === last && (
              <span className="ml-[5px] flex h-[17px] w-[17px] items-center justify-center rounded-full border-[1.8px]" style={{ borderColor: '#1f2440' }}>
                <ChevronRight size={11} strokeWidth={3} color={theme.text} />
              </span>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
