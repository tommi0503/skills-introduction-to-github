import { ImagePlaceholder, cn } from '../../../ui'
import type { StoryItem } from '../data'
import { theme } from '../theme'

export interface StoryCardProps {
  story: StoryItem
  className?: string
}

/** Story card: photo background (placeholder) with label + two-line title. */
export function StoryCard({ story, className }: StoryCardProps) {
  return (
    <div className={cn('relative h-[231px] w-[249px] shrink-0 overflow-hidden rounded-[6px] font-pretendard', className)}>
      <ImagePlaceholder label={`${story.label} 사진`} tone="#c9cbd0" className="absolute inset-0" />
      {story.isNew && (
        <div
          className="absolute top-[24px] flex h-[38px] w-[38px] items-center justify-center rounded-full text-[11.5px] font-extrabold text-black"
          style={{ background: theme.lime, left: 20 }}
        >
          NEW
        </div>
      )}
      <div className="absolute top-[140px] left-[21px] text-white">
        <div className="text-[12.5px] font-light leading-[16px] tracking-[-0.2px]">{story.label}</div>
        <div className="mt-[5px] text-[16.6px] font-bold leading-[24px] tracking-[-0.3px]">
          {story.title.map((line) => (
            <div key={line}>{line}</div>
          ))}
        </div>
      </div>
    </div>
  )
}
