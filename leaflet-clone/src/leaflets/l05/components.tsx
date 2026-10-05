import type { ReactNode } from 'react'
import { cn, ImagePlaceholder, Placed } from '../../ui'
import { photo, theme } from './theme'

/** Left-aligned light section heading (이용 안내 / 예약 문의 / 운항 요금). */
export function SectionHeading({ x, y, className, children }: { x: number; y: number; className?: string; children: ReactNode }) {
  return (
    <Placed x={x} y={y} className={cn('whitespace-nowrap font-noto-sans text-[25px] font-light leading-[36px]', className)}>
      {children}
    </Placed>
  )
}

/** Ship photo spanning the top of the two right panels with a slanted lower edge. */
export function SpanningPhoto() {
  return (
    <ImagePlaceholder
      label="cruise ship photo"
      tone={theme.photoTone}
      className="absolute top-0"
      style={{
        left: photo.x,
        width: photo.width,
        height: photo.rightBottom,
        clipPath: `polygon(0 0, 100% 0, 100% 100%, 0 ${photo.leftBottom}px)`,
      }}
    />
  )
}

