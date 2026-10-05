import { cn } from '../../../ui'
import { seoul } from '../theme'

interface SectionNumberProps {
  number: string
  title: string
  /** 'inline': number then title on one baseline; 'stacked': title under the number. */
  layout: 'inline' | 'stacked'
  align?: 'left' | 'center'
  /** Inline only: share the baseline (default) or centre the title on the number. */
  inlineAlign?: 'baseline' | 'center'
  className?: string
}

/** Big sky-blue section number with its slate heading (01 과거와 미래가 …). */
export function SectionNumber({ number, title, layout, align = 'left', inlineAlign = 'baseline', className }: SectionNumberProps) {
  return (
    <div
      className={cn(
        'flex',
        layout === 'inline' ? cn('gap-[16px]', inlineAlign === 'center' ? 'items-center' : 'items-baseline') : 'flex-col gap-[16px]',
        align === 'center' && 'items-center text-center',
        className,
      )}
    >
      <span className="font-montserrat text-[58px] font-semibold leading-[44px] tracking-[-0.01em]" style={{ color: seoul.sky }}>
        {number}
      </span>
      <span className="whitespace-nowrap font-nanum-gothic text-[25px] font-extrabold leading-none tracking-[-0.02em]" style={{ color: seoul.slate }}>
        {title}
      </span>
    </div>
  )
}
