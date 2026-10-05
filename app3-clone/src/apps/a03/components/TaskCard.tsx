import { Clock3, EllipsisVertical, Tag } from 'lucide-react'
import type { Task } from '../data'
import { nd } from '../theme'

/** Task list card: priority pill, kebab, two-line title, time range and tag chip. */
export function TaskCard({ task }: { task: Task }) {
  return (
    <div className="relative h-[158px] rounded-[18px] bg-white shadow-[0_4px_14px_rgba(20,30,50,0.05)] px-[14px] pt-[15px]">
      <span
        className="flex h-[30px] w-[89px] items-center justify-center rounded-full text-[10.5px]"
        style={{ background: nd.pill }}
      >
        {task.priority}
      </span>
      <EllipsisVertical size={20} strokeWidth={2.6} className="absolute top-[16px] right-[16px]" />
      <p className="mt-[11px] text-[17px] leading-[27px] font-medium whitespace-pre-line">{task.title}</p>
      <div className="absolute right-[13px] bottom-[15px] left-[19px] flex items-center justify-between">
        <span className="flex items-center gap-[5px] text-[10px]" style={{ color: nd.muted }}>
          <Clock3 size={11} strokeWidth={1.8} />
          {task.time}
        </span>
        <span className="flex h-[24px] items-center gap-[4px] rounded-full px-[9px] text-[9.5px]" style={{ background: '#f4f5f7' }}>
          <Tag size={10} strokeWidth={1.8} />
          {task.tag}
        </span>
      </div>
    </div>
  )
}
