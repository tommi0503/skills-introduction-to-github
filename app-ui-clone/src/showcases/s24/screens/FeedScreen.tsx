import { MapLayer } from '../components/MapLayer'
import { NoticeBar } from '../components/NoticeBar'
import { PromoBannerCard } from '../components/PromoBannerCard'
import { ReserveRow } from '../components/ReserveRow'
import { SheetGrabber } from '../components/SheetGrabber'
import { StoryCard } from '../components/StoryCard'
import { TadaStatusBar } from '../components/TadaStatusBar'
import { feedNotice, nextBanner, reserve, storyCards } from '../data'
import { theme } from '../theme'

/** Sheet expanded: promotions and stories feed. */
export function FeedScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white font-pretendard">
      <MapLayer height={120} showLocate={false} />
      <div className="absolute inset-x-0 top-0 z-10">
        <TadaStatusBar time="12:20" battery={{ level: 0.3 }} />
      </div>
      <div className="absolute inset-x-0 top-[83.7px] bottom-0 overflow-hidden rounded-t-[16px] bg-white">
        <SheetGrabber className="mt-[10px]" />
        <ReserveRow title={reserve.title} actions={reserve.actions} className="-mt-[1px] opacity-[0.18] blur-[0.6px]" />
        <div className="mx-[21px] mt-[18.5px] h-px" style={{ background: theme.line }} />
        <PromoBannerCard
          banner={nextBanner}
          art={{ x: 197, y: 17, w: 120, h: 45 }}
          className="mx-[21px] mt-[27.5px]"
        />
        <div className="mt-[19px] flex flex-col items-center">
          {storyCards.map((item, i) => (
            <div key={item.id} className="flex flex-col items-center">
              {i > 0 && <div className="my-[21px] h-px w-[348px]" style={{ background: theme.line }} />}
              <StoryCard item={item} />
            </div>
          ))}
        </div>
      </div>
      <NoticeBar notice={feedNotice} />
    </div>
  )
}
