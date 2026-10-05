import { cn } from '../../../ui'
import { seoul } from '../theme'

interface SectionNumberProps {
  number: string
  title: string
  /** 'inline': number then title on one baseline; 'stacked': title under the number. */
  layout: 'inline' | 'stacked'
  align?: 'left' | 'center'
  className?: string
}

/** Big sky-blue section number with its slate heading (01 과거와 미래가 …). */
export function SectionNumber({ number, title, layout, align = 'left', className }: SectionNumberProps) {
  return (
    <div
      className={cn(
        'flex',
        layout === 'inline' ? 'items-baseline gap-[16px]' : 'flex-col gap-[16px]',
        align === 'center' && 'items-center text-center',
        className,
      )}
    >
      <span className="font-montserrat text-[58px] font-semibold leading-[44px] tracking-[-0.01em]" style={{ color: seoul.sky }}>
        {number}
      </span>
      <span className="whitespace-nowrap font-nanum-gothic text-[24px] font-extrabold leading-none tracking-[-0.02em]" style={{ color: seoul.slate }}>
        {title}
      </span>
    </div>
  )
}
