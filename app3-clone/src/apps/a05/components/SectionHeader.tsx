import { ArrowRight } from 'lucide-react'
import { ue } from '../theme'

export interface SectionHeaderProps {
  title: string
  subtitle?: string
  arrow?: boolean
  className?: string
}

export function SectionHeader({ title, subtitle, arrow, className }: SectionHeaderProps) {
  return (
    <div className={`flex items-center justify-between px-[16px] ${className ?? ''}`}>
      <div>
        <h2 className="text-[19.5px] leading-[24px] font-bold tracking-[-0.5px]">{title}</h2>
        {subtitle && (
          <p className="mt-[4px] text-[13px]" style={{ color: ue.muted }}>
            {subtitle}
          </p>
        )}
      </div>
      {arrow && (
        <span className="flex h-[36px] w-[36px] items-center justify-center rounded-full" style={{ background: ue.field }}>
          <ArrowRight size={17} strokeWidth={2.2} />
        </span>
      )}
    </div>
  )
}
