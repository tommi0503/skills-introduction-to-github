import { ChevronDown, Ellipsis, Heart, Plus } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { IgStatusBar } from '../components/IgStatusBar'
import { IgTabBar } from '../components/IgTabBar'
import { StoryItem } from '../components/StoryItem'
import { feedPost, stories } from '../data'
import { ig } from '../theme'

function FeedHeader() {
  return (
    <div className="absolute inset-x-0 top-[66px] flex h-[36px] items-center justify-between px-[16px]">
      <Plus size={27} strokeWidth={1.6} />
      <div className="flex items-center gap-[6px] pl-[14px]">
        <ImagePlaceholder className="h-[30px] w-[114px] rounded-[4px]" label="Instagram wordmark" />
        <ChevronDown size={14} strokeWidth={2.2} />
      </div>
      <div className="relative">
        <Heart size={26} strokeWidth={1.8} />
        <span className="absolute top-[-2px] right-[-2px] h-[9px] w-[9px] rounded-full border-[1.5px] border-white bg-[#ff3040]" />
      </div>
    </div>
  )
}

function PostHeader() {
  return (
    <div className="absolute inset-x-0 top-[244px] flex h-[34px] items-center pr-[12px] pl-[7px]">
      <div className="relative h-[30px] w-[34px]">
        <ImagePlaceholder className="absolute top-0 right-[2px] h-[20px] w-[20px] rounded-full border-[1.5px] border-white" />
        <ImagePlaceholder className="absolute bottom-0 left-0 h-[24px] w-[24px] rounded-full border-[1.5px] border-white" />
      </div>
      <span className="ml-[10px] flex-1 truncate text-[14px] font-semibold tracking-[-0.1px] text-[#262626]">
        {feedPost.authors} <span className="font-normal">and</span> {feedPost.coAuthor}
      </span>
      <span
        className="flex h-[31px] w-[70px] items-center justify-center rounded-[8px] text-[14px] font-semibold"
        style={{ background: ig.followBg }}
      >
        Follow
      </span>
      <Ellipsis size={20} strokeWidth={2.2} className="ml-[13px]" />
    </div>
  )
}

/** Instagram home feed: stories tray and the top of a carousel post. */
export function FeedScreen() {
  return (
    <AppScreen className="font-inter text-black">
      <IgStatusBar />
      <FeedHeader />
      <div className="absolute top-[110px] left-[6px] flex gap-[11px]">
        {stories.map((s) => (
          <StoryItem key={s.key} story={s} />
        ))}
      </div>
      <PostHeader />
      <div className="absolute inset-x-0 top-[287px] h-[480px]">
        <ImagePlaceholder className="h-full w-full" label="post photo" />
        <span className="absolute top-[16px] right-[14px] rounded-full bg-black/55 px-[8px] py-[4px] text-[12px] leading-none font-medium text-white">
          {feedPost.counter}
        </span>
      </div>
      <IgTabBar activeKey="home" />
    </AppScreen>
  )
}
