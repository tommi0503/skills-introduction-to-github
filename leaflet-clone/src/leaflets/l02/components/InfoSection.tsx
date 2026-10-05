import { cn } from '../../../ui'
import { Lines } from './Lines'

interface InfoSectionProps {
  title: string
  highlight: string
  lines: string[]
  highlightColor: string
  className?: string
}

/** "• title" + coloured highlight line + grey description. */
export function InfoSection({ title, highlight, lines, highlightColor, className }: InfoSectionProps) {
  return (
    <section className={cn('flex flex-col', className)}>
      <h3 className="m-0 flex items-center text-[24px] font-bold leading-none tracking-[-0.03em] text-[#1e1e1e]">
        <span className="mr-[8px] text-[16px]">•</span>
        {title}
      </h3>
      <div className="ml-[16px] mt-[12px]">
        <p className="m-0 text-[20.5px] font-medium leading-[30px] tracking-[-0.03em]" style={{ color: highlightColor }}>{highlight}</p>
        <Lines lines={lines} className="text-[20px] leading-[31px] tracking-[-0.03em] text-[#555]" />
      </div>
    </section>
  )
}
