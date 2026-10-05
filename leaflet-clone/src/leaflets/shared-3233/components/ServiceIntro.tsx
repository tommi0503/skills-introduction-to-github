import { ImagePlaceholder, cn } from '../../../ui'
import { hutech, hutechType } from '../theme'

export interface ServiceIntroProps {
  /** Footprint of the two-tone cloud illustration (not expressible with lucide → placeholder). */
  iconBox: { width: number; height: number }
  /** Height reserved for the illustration so the headings line up across panels. */
  slotHeight?: number
  label: string
  headline: string
  className?: string
}

/** Large illustration + "SERVICE 0N" + two-line headline that opens each inside panel. */
export function ServiceIntro({ iconBox, slotHeight = 179, label, headline, className }: ServiceIntroProps) {
  return (
    <div className={cn('flex flex-col', className)}>
      <div style={{ height: slotHeight }}>
        <ImagePlaceholder label="service illustration" style={{ ...iconBox, borderRadius: 24 }} />
      </div>
      <h2 className={cn('m-0 mt-[36px] text-[43px] leading-[52px]', hutechType.display)} style={{ color: hutech.accent }}>
        {label}
      </h2>
      <p className="m-0 mt-[24px] whitespace-pre-line text-[29px] leading-[37px] tracking-[-0.01em]" style={{ color: hutech.inkSoft }}>
        {headline}
      </p>
    </div>
  )
}
