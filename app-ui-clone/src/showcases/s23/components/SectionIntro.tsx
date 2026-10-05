import { cn } from '../../../ui'
import { theme } from '../theme'

export interface SectionIntroProps {
  title: string
  subtitle: string
  className?: string
}

export function SectionIntro({ title, subtitle, className }: SectionIntroProps) {
  return (
    <div className={cn('px-[25px] font-pretendard', className)}>
      <h2 className="text-[22.3px] font-bold leading-[26px] tracking-[0.2px]" style={{ color: theme.ink }}>
        {title}
      </h2>
      <p className="mt-[11px] text-[14.6px] leading-[18px] tracking-[0.35px]" style={{ color: theme.sub }}>
        {subtitle}
      </p>
    </div>
  )
}
