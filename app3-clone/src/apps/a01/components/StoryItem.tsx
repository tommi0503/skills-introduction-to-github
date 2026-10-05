import { Plus } from 'lucide-react'
import { Avatar } from '../../../ui'
import type { Story } from '../data'
import { StoryRing } from './StoryRing'

const SIZE = 90

/** One entry of the stories tray: ring (or own avatar with plus badge) and a truncated label. */
export function StoryItem({ story }: { story: Story }) {
  return (
    <div className="flex w-[92px] shrink-0 flex-col items-center">
      {story.kind === 'own' ? (
        <div className="relative flex items-center justify-center" style={{ width: SIZE, height: SIZE }}>
          <Avatar size={79} />
          <span className="absolute right-[4px] bottom-[6px] flex h-[25px] w-[25px] items-center justify-center rounded-full border-[2.5px] border-white bg-black text-white">
            <Plus size={15} strokeWidth={3} />
          </span>
        </div>
      ) : (
        <StoryRing size={SIZE} ring={4} gap={4} />
      )}
      <span className="mt-[9px] w-[100px] truncate text-center text-[12px] leading-none text-[#262626]">{story.label}</span>
    </div>
  )
}
