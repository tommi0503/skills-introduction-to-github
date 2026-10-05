import type { ReactNode } from 'react'
import { ImagePlaceholder, cn } from '../../../ui'

/** Corner's portrait-oval profile photo, optionally with a corner badge. `className` sets size/position. */
export function OvalPhoto({ className, badge, tone }: { className?: string; badge?: ReactNode; tone?: string }) {
  return (
    <div className={cn('shrink-0', className)}>
      <div className="relative h-full w-full">
        <ImagePlaceholder label="profile photo" tone={tone} className="h-full w-full rounded-[50%]" />
        {badge && <div className="absolute -right-[1px] bottom-[2px]">{badge}</div>}
      </div>
    </div>
  )
}
