import { cn } from '../../../ui'

export interface SectionHeadingProps {
  title: string
  /** Colour of the heading text and the rule below it. */
  color: string
  ruleColor?: string
  ruleThickness?: number
  /** Gap between the heading text and the rule (px). */
  gap?: number
  className?: string
  titleClassName?: string
}

/** Small accent heading with a full-width rule underneath (연락처 / 기업 이념 / 핵심 장점 …). */
export function SectionHeading({
  title,
  color,
  ruleColor,
  ruleThickness = 3,
  gap = 12,
  className,
  titleClassName,
}: SectionHeadingProps) {
  return (
    <div className={cn('flex flex-col', className)}>
      <h3 className={cn('m-0 font-bold', titleClassName)} style={{ color }}>
        {title}
      </h3>
      <div style={{ marginTop: gap, height: ruleThickness, background: ruleColor ?? color }} />
    </div>
  )
}
