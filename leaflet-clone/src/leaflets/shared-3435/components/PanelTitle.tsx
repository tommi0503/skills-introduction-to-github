import { cn } from '../../../ui'
import { larana } from '../theme'

export interface PanelTitleProps {
  children: string
  className?: string
}

/** Centered navy section title (인사말 / 오시는 길 / 진료 안내 …). */
export function PanelTitle({ children, className }: PanelTitleProps) {
  return (
    <h2 className={cn('m-0 text-center text-[33px] font-bold leading-[36px] tracking-[0.04em]', className)} style={{ color: larana.navy }}>
      {children}
    </h2>
  )
}
