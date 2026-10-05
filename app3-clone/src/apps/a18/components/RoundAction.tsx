import { ImagePlaceholder, cn } from '../../../ui'
import type { ShareAction } from '../data'

export interface RoundActionProps {
  action: ShareAction
  size: number
  iconSize?: number
  className?: string
  /** Placeholder tone for brand marks. */
  markTone?: string
}

export function RoundAction({ action, size, iconSize = 18, className, markTone = '#cfcfcf' }: RoundActionProps) {
  const Icon = action.icon
  return (
    <div className={cn('flex shrink-0 items-center justify-center rounded-full', className)} style={{ width: size, height: size }}>
      {Icon ? (
        <Icon size={iconSize} strokeWidth={2.4} />
      ) : (
        <ImagePlaceholder tone={markTone} label={action.key} className="rounded-[4px]" style={{ width: iconSize, height: iconSize }} />
      )}
    </div>
  )
}
