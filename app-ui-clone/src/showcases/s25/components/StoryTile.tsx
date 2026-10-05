import { Plus } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { Story } from '../data'

const cardShadow = '0 3px 10px rgba(0,0,0,0.12)'

function Badge({ tone, right = -13 }: { tone: Story['badge']; right?: number }) {
  if (!tone) return null
  return (
    <div
      className="absolute rounded-full bg-white p-[2px]"
      style={{ right, bottom: -3, width: 26, height: 26, boxShadow: '0 1px 4px rgba(0,0,0,0.12)' }}
    >
      <ImagePlaceholder label={tone === 'brand' ? 'bond logo' : 'avatar'} className="h-full w-full rounded-full" />
    </div>
  )
}

/** The picture part of a story — each variant is a small strategy keyed by `visual`. */
function StoryVisualView({ story }: { story: Story }) {
  switch (story.visual) {
    case 'add':
      return (
        <div
          className="flex h-[83px] w-[83px] items-center justify-center rounded-full bg-white text-[#777]"
          style={{ boxShadow: '0 4px 14px rgba(0,0,0,0.06)', marginBottom: 4 }}
        >
          <Plus size={30} strokeWidth={1.6} />
        </div>
      )
    case 'stack':
      return (
        <div className="relative" style={{ width: 66, height: 87, marginRight: 4 }}>
          <div className="absolute rounded-[7px] bg-[#6d6d6d]" style={{ inset: 0, transform: 'rotate(5deg) translate(5px,0px)' }} />
          <div
            className="absolute rounded-[7px] bg-white p-[2px]"
            style={{ inset: 0, transform: 'rotate(-2.5deg)', boxShadow: cardShadow }}
          >
            <ImagePlaceholder label="story photo" className="h-full w-full rounded-[5px]" />
          </div>
          <Badge tone={story.badge} />
        </div>
      )
    case 'card':
      return (
        <div className="relative rounded-[8px] bg-white px-[14px] pt-[6px]" style={{ width: 70, height: 92, boxShadow: cardShadow }}>
          <ImagePlaceholder label="story screenshot" className="h-[56px] w-full rounded-[4px]" />
          <Badge tone={story.badge} />
        </div>
      )
    case 'photo':
      return (
        <div className="relative rounded-[7px] bg-white p-[2px]" style={{ width: 78, height: 79, boxShadow: cardShadow, transform: 'rotate(-0.5deg)' }}>
          <ImagePlaceholder label="story photo" className="h-full w-full rounded-[5px]" />
          <Badge tone={story.badge} right={-6} />
        </div>
      )
  }
}

export function StoryTile({ story, className }: { story: Story; className?: string }) {
  return (
    <div className={cn('flex w-[115px] flex-col items-center', className)}>
      <div className="flex h-[96px] items-end justify-center">
        <StoryVisualView story={story} />
      </div>
      <span
        className={cn('mt-[16px] text-[14.5px] leading-[18px] font-semibold', story.seen ? 'text-[#8f8f8f]' : 'text-[#111]')}
        style={{ letterSpacing: -0.2 }}
      >
        {story.name}
      </span>
      {story.time && <span className="text-[12.5px] leading-[17px] text-[#9d9d9d]">{story.time}</span>}
    </div>
  )
}
