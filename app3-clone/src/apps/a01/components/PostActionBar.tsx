import type { LucideIcon } from 'lucide-react'
import type { PostAction } from '../data'

export interface PostActionBarProps {
  actions: PostAction[]
  saveIcon: LucideIcon
  className?: string
}

/** Like / comment / repost / share counters with the save button pinned right. */
export function PostActionBar({ actions, saveIcon: Save, className }: PostActionBarProps) {
  return (
    <div className={`flex items-center pr-[16px] pl-[12px] ${className ?? ''}`}>
      <div className="flex flex-1 items-center gap-[13px]">
        {actions.map(({ key, icon: Icon, count }) => (
          <div key={key} className="flex items-center gap-[6px]">
            <Icon size={24} strokeWidth={1.8} className={key === 'comment' ? '-scale-x-100' : undefined} />
            <span className="text-[13.5px] font-semibold tracking-[-0.4px]">{count}</span>
          </div>
        ))}
      </div>
      <Save size={24} strokeWidth={1.9} />
    </div>
  )
}
