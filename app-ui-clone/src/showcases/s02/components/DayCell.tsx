import { ImagePlaceholder, cn } from '../../../ui'
import type { DayState } from '../data'

interface DayCellProps {
  day: number
  state: DayState
}

const styles: Record<Exclude<DayState, 'photo'>, string> = {
  default: 'border border-[#ededed] text-[#858585]',
  faded: 'border border-[#f3f3f3] text-[#d0d0d0]',
  selected: 'bg-[#1f1f1f] text-white',
  pending: 'bg-[#8d8d8d] text-white',
}

/** 36pt round calendar day in one of several selection states. */
export function DayCell({ day, state }: DayCellProps) {
  return (
    <div
      className={cn(
        'relative flex h-[36px] w-[36px] items-center justify-center overflow-hidden rounded-full text-[14px]',
        state !== 'photo' && styles[state],
      )}
    >
      {state === 'photo' && <ImagePlaceholder className="absolute inset-0" tone="#cfd3d8" label="destination" />}
      <span className={cn('relative', state === 'photo' && 'text-white font-medium')}>{day}</span>
    </div>
  )
}
