import { Check, ChevronRight } from 'lucide-react'
import { cn } from '../../../ui'
import type { Task } from '../data'

/** One checklist item: status circle, title + meta, chevron for open items. */
export function TaskRow({ task, divider }: { task: Task; divider: boolean }) {
  return (
    <div className="relative flex h-[67px] items-center pr-[16px] pl-[16px]">
      <span
        className={cn(
          'flex h-[25px] w-[25px] shrink-0 items-center justify-center rounded-full',
          task.done ? 'bg-[#18171c] text-white' : 'border border-[#dcdcdf]',
        )}
      >
        {task.done && <Check size={11} strokeWidth={2.8} />}
      </span>
      <div className="ml-[13.5px] flex-1">
        <div className={cn('text-[14px] font-semibold tracking-[-0.1px]', task.done && 'text-[#b3b3b8] line-through')}>{task.title}</div>
        <div className="mt-[2px] text-[11px] font-medium text-[#9c9ca1]">{task.meta}</div>
      </div>
      {!task.done && <ChevronRight size={14} strokeWidth={1.8} className="text-[#b8b8bd]" />}
      {divider && <span className="absolute right-0 bottom-0 left-[55px] h-px bg-[#ececee]" />}
    </div>
  )
}
