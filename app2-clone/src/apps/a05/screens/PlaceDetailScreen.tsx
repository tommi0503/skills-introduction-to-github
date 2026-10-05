import { AppScreen } from '../../../ui'
import { place, placeActions } from '../data'
import { theme } from '../theme'
import { ActionChips } from '../components/ActionChips'
import { Chrome } from '../components/Chrome'
import { MapBackdrop } from '../components/MapBackdrop'
import { OvalPhoto } from '../components/OvalPhoto'
import { PhotoStrip } from '../components/PhotoStrip'
import { PlaceHeader } from '../components/PlaceHeader'
import { SavedByCard } from '../components/SavedByCard'
import { SearchBar } from '../components/SearchBar'
import { Sticker } from '../components/Sticker'

export function PlaceDetailScreen() {
  return (
    <AppScreen className="font-archivo">
      <MapBackdrop className="absolute inset-x-0 top-0 h-[160px]" />
      <div className="absolute inset-x-0 top-[126px] bottom-0 rounded-t-[22px]" style={{ background: theme.sheet }}>
        <PlaceHeader />
        <PhotoStrip widths={[141, 153, 80]} height={190} className="absolute left-[7px] top-[136px]" />
        <Sticker lines={place.sticker} className="left-[298px] top-[257px] h-[78px] w-[90px]" />
        <p className="absolute left-[7px] right-[14px] top-[343px] text-[14.6px] leading-[23px] tracking-[0.2px] text-[#3c3c40]">
          {place.about.meta.map((m) => (
            <span key={m} className="text-[#86868a]">
              {m} <span className="text-[#c4c4c8]">•</span>{' '}
            </span>
          ))}
          {place.about.text}
        </p>
        <SavedByCard className="absolute left-[7px] right-[9px] top-[406px] h-[140px]" />
        <OvalPhoto className="absolute left-[6px] top-[567px] h-[47px] w-[40px]" />
        <div className="absolute left-[58px] right-[9px] top-[571px] flex h-[43px] items-center rounded-[12px] border-[1.5px] border-dashed border-[#d9d9dc] bg-white pl-[16px] text-[15px] text-[#a8a8ac]">
          what do you think?
        </div>
        <div className="absolute left-[58px] right-[9px] top-[631px] h-[80px] rounded-[12px] border border-[#e1e1e4] bg-white" />
      </div>
      <div className="absolute inset-x-0 bottom-0 h-[110px]" style={{ background: 'linear-gradient(rgba(246,247,245,0), #f1f2ef 55%)' }} />
      <ActionChips items={placeActions} className="absolute left-[19px] top-[785px]" />
      <SearchBar value={place.query} className="absolute left-[15px] top-[59px] w-[357px]" />
      <Chrome />
    </AppScreen>
  )
}
