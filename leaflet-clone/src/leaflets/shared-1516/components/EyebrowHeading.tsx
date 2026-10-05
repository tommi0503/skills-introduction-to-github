import { cn } from '../../../ui'
import { concertTheme as t } from '../theme'

export interface EyebrowHeadingProps {
  eyebrow: string
  title: string
  eyebrowColor: string
  titleColor: string
  align?: 'left' | 'center'
  className?: string
}

/** Small Latin label above a bold Korean section title (ARTISTS / 함께하는 사람들). */
export function EyebrowHeading({ eyebrow, title, eyebrowColor, titleColor, align = 'left', className }: EyebrowHeadingProps) {
  return (
    <div className={cn(align === 'center' && 'text-center', className)}>
      <div className={cn(t.font.latin, 'text-[17px] font-medium leading-[20px]')} style={{ color: eyebrowColor }}>
        {eyebrow}
      </div>
      <div className="mt-[8px] text-[29px] font-bold leading-[34px] tracking-[-0.01em]" style={{ color: titleColor }}>
        {title}
      </div>
    </div>
  )
}
