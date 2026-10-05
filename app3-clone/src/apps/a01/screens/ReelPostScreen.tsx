import { BadgeCheck, Ellipsis, Music2, User, VolumeX } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { IgStatusBar } from '../components/IgStatusBar'
import { IgTabBar } from '../components/IgTabBar'
import { PostActionBar } from '../components/PostActionBar'
import { StoryRing } from '../components/StoryRing'
import { reelPost } from '../data'
import { ig } from '../theme'

function VideoOverlayHeader() {
  return (
    <div className="absolute inset-x-0 top-[6px] flex items-center pr-[12px] pl-[5px] text-white">
      <StoryRing size={40} ring={2.5} gap={2} />
      <div className="ml-[5px] flex-1 leading-none">
        <div className="flex items-center gap-[4px] text-[15px] font-semibold tracking-[-0.3px]">
          {reelPost.author}
          <BadgeCheck size={14} strokeWidth={2.4} fill="#fff" className="text-[#8b8580]" />
        </div>
        <div className="mt-[4px] flex items-center gap-[4px] text-[13px] tracking-[-0.3px]">
          <Music2 size={12} strokeWidth={2.4} />
          {reelPost.audio}
        </div>
      </div>
      <span className="flex h-[31px] w-[68px] items-center justify-center rounded-[8px] border border-white/70 text-[14px] font-semibold">
        Follow
      </span>
      <Ellipsis size={20} strokeWidth={2.4} className="ml-[13px]" />
    </div>
  )
}

function RoundBadge({ children, className }: { children: React.ReactNode; className: string }) {
  return (
    <span className={`absolute flex h-[26px] w-[26px] items-center justify-center rounded-full bg-black/45 text-white ${className}`}>
      {children}
    </span>
  )
}

/** Instagram reel/post detail with video overlay, counters and caption. */
export function ReelPostScreen() {
  return (
    <AppScreen className="font-inter text-black">
      <IgStatusBar />
      <div className="absolute inset-x-0 top-[80px] h-[608px]">
        <ImagePlaceholder tone={ig.photoDark} className="h-full w-full" label="video" />
        <VideoOverlayHeader />
        <RoundBadge className="bottom-[14px] left-[12px]">
          <User size={13} strokeWidth={2.4} fill="#fff" />
        </RoundBadge>
        <RoundBadge className="right-[15px] bottom-[14px]">
          <VolumeX size={13} strokeWidth={2.4} />
        </RoundBadge>
      </div>
      <PostActionBar actions={reelPost.actions} saveIcon={reelPost.saveIcon} className="absolute inset-x-0 top-[699px]" />
      <p className="absolute top-[735px] right-[14px] left-[11px] truncate text-[13.5px] tracking-[-0.35px] text-[#111]">
        <span className="font-semibold">{reelPost.author}</span> {reelPost.caption}{' '}
        <span className="text-[#8e8e8e]">more</span>
      </p>
      <p className="absolute top-[756px] left-[11px] text-[12px] text-[#8e8e8e]">{reelPost.time}</p>
      <IgTabBar activeKey="home" className="top-[764px] h-auto pt-[12px]" />
    </AppScreen>
  )
}
