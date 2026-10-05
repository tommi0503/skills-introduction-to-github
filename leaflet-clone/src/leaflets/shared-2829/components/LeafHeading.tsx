import { ImagePlaceholder, cn } from '../../../ui'
import { autumn, fonts } from '../theme'

export interface LeafHeadingProps {
  title?: string
  className?: string
  titleClassName?: string
}

/** Section heading led by the small leaf ornament (artwork → placeholder). */
export function LeafHeading({ title, className, titleClassName }: LeafHeadingProps) {
  return (
    <div className={cn('flex items-center gap-[11px]', className)}>
      <ImagePlaceholder label="leaf ornament" className="h-[34px] w-[24px]" style={{ borderRadius: '50% 50% 45% 45% / 60% 60% 40% 40%' }} />
      {title && (
        <h2 className={cn('m-0 whitespace-nowrap text-[25px] leading-none tracking-[-0.5px]', fonts.heading, titleClassName)} style={{ color: autumn.headingBrown }}>
          {title}
        </h2>
      )}
    </div>
  )
}
