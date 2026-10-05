import { DestinationInput } from '../components/DestinationInput'
import { MapLayer } from '../components/MapLayer'
import { NoticeBar } from '../components/NoticeBar'
import { PromoBannerCard } from '../components/PromoBannerCard'
import { ReserveRow } from '../components/ReserveRow'
import { SheetGrabber } from '../components/SheetGrabber'
import { ShortcutRow } from '../components/ShortcutRow'
import { TadaStatusBar } from '../components/TadaStatusBar'
import { destinationPlaceholder, friendBanner, greeting, homeNotice, reserve, shortcuts } from '../data'
import { theme } from '../theme'

export interface MapHomeScreenProps {
  time?: string
  /** Hide the status bar when another layer (drawer) draws its own. */
  showStatusBar?: boolean
  showLocate?: boolean
}

/** Home: map with the "where to?" bottom sheet. */
export function MapHomeScreen({ time = '12:30', showStatusBar = true, showLocate = true }: MapHomeScreenProps) {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white font-pretendard">
      <MapLayer height={340} showLocate={showLocate} />
      {showStatusBar && (
        <div className="absolute inset-x-0 top-0 z-10">
          <TadaStatusBar time={time} battery={{ level: 0.6, fill: '#4cd964', charging: true }} />
        </div>
      )}
      <div
        className="absolute inset-x-0 top-[321.8px] h-[190px] rounded-t-[16px] bg-white"
        style={{ boxShadow: '0 -2px 8px rgba(0,0,0,0.04)' }}
      >
        <SheetGrabber className="mt-[9.5px]" />
        <div className="mt-[23.5px] px-[26px] text-[17.5px] font-bold tracking-[-0.3px]" style={{ color: theme.ink }}>
          {greeting}
        </div>
        <DestinationInput placeholder={destinationPlaceholder} className="mx-[21px] mt-[12.5px]" />
        <ShortcutRow items={shortcuts} className="mt-[15px]" />
      </div>
      <div className="absolute inset-x-0 top-[512px] h-[11px]" style={{ background: 'linear-gradient(#f3f3f5,#f8f8fa)' }} />
      <div className="absolute inset-x-0 top-[523px] bottom-0 bg-white">
        <ReserveRow title={reserve.title} actions={reserve.actions} className="mt-[23px]" />
        <div className="mx-[21px] mt-[18px] h-px" style={{ background: theme.line }} />
        <PromoBannerCard
          banner={friendBanner}
          art={{ x: 224, y: 0, w: 124, h: 75 }}
          className="mx-[21px] mt-[27px]"
        />
        <div className="mx-[21px] mt-[22px] h-[60px] rounded-[8px] bg-[#dee1e8]" />
      </div>
      <NoticeBar notice={homeNotice} />
    </div>
  )
}
