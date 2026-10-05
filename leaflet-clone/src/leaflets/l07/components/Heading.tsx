import type { ReactNode } from 'react'
import { cn, Placed } from '../../../ui'

/** Heavy section heading (입장료 / 인사말 / 오시는 길). */
export function Heading({ x, y, color, className, children }: { x: number; y: number; color: string; className?: string; children: ReactNode }) {
  return (
    <Placed x={x} y={y} className={cn('whitespace-nowrap font-pretendard text-[42px] font-black leading-[50px] tracking-[0.02em]', className)} style={{ color }}>
      {children}
    </Placed>
  )
}
