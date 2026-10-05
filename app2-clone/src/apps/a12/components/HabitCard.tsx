import { Flame, Info, Star } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import type { Habit } from '../data'
import { Difficulty } from './Difficulty'

export interface HabitCardProps {
  habit: Habit
  height: number
  className?: string
}

/** Illustrated habit card on the Today list. */
export function HabitCard({ habit, height, className }: HabitCardProps) {
  const welcome = habit.badge.kind === 'welcome'
  return (
    <div
      className={cn('relative overflow-hidden rounded-[10px] border-2', className)}
      style={{ height, borderColor: habit.highlight ? '#e07a35' : '#151515' }}
    >
      <ImagePlaceholder tone={habit.tone} label="habit illustration" className="absolute inset-0" />
      {welcome ? (
        <div className="absolute top-[8px] left-[8px] flex h-[16px] items-center gap-[4px] rounded-[4px] bg-black/30 px-[5px] text-[8.5px] font-medium text-white/85">
          <Star size={9} fill="#f08a3a" stroke="none" />
          {habit.badge.label}
        </div>
      ) : (
        <div className="absolute top-[5px] left-[6px] flex h-[24px] items-center gap-[3px] rounded-[8px] bg-[#6a3416]/85 px-[7px] text-[12px] font-bold text-white">
          <Flame size={12} fill="#f5833a" stroke="#f5833a" />
          {habit.badge.label}
        </div>
      )}
      <Info
        size={26}
        strokeWidth={1.4}
        className={cn('absolute top-[9px] right-[9px] text-white', habit.infoDim && 'opacity-40')}
      />
      <div className="absolute left-[7px] text-[19px] font-bold tracking-[-0.4px] whitespace-nowrap text-white" style={{ top: welcome ? 61 : 61 }}>
        {habit.title}
      </div>
      <div className="absolute left-[7px]" style={{ top: welcome ? 95 : 95 }}>
        <Difficulty />
      </div>
    </div>
  )
}
