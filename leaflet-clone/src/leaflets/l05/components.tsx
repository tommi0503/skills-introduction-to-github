import type { ReactNode } from 'react'
import { cn, Placed } from '../../ui'

/** Left-aligned light section heading (이용 안내 / 예약 문의 / 운항 요금). */
export function SectionHeading({ x, y, className, children }: { x: number; y: number; className?: string; children: ReactNode }) {
  return (
    <Placed x={x} y={y} className={cn('whitespace-nowrap font-noto-sans text-[25px] font-light leading-[36px]', className)}>
      {children}
    </Placed>
  )
}
