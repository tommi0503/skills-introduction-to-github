import { ChevronDown, ChevronLeft, Layers, Loader, LocateFixed, Share, TriangleAlert } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { FiStatusBar } from '../components/FiStatusBar'
import { CircleIcon } from '../components/CircleIcon'
import { PetMarker } from '../components/PetMarker'
import { DeviceStatusRow } from '../components/DeviceStatusRow'
import { lost, lostStatus, pet } from '../data'
import { fi } from '../theme'

const floatShadow = 'shadow-[0_1px_4px_rgba(0,0,0,0.12)]'

export function LostModeScreen() {
  return (
    <AppScreen>
      <ImagePlaceholder className="absolute inset-x-0 top-0 h-[710px]" label="map" />
      <FiStatusBar />

      <CircleIcon icon={ChevronLeft} size={40} iconSize={22} strokeWidth={2.4} className={`absolute left-[15px] top-[62px] ${floatShadow}`} />
      <div className={`absolute left-[150px] top-[62px] flex h-[40px] items-center gap-[4px] rounded-full bg-white px-[15px] text-[20px] font-medium ${floatShadow}`}>
        {pet.name}
        <ChevronDown size={15} strokeWidth={2.6} />
      </div>
      <div className={`absolute left-[337px] top-[62px] flex h-[87px] w-[36px] flex-col items-center justify-around rounded-full bg-white py-[4px] ${floatShadow}`}>
        <Layers size={19} strokeWidth={2.2} fill="#000" />
        <LocateFixed size={20} strokeWidth={2.4} />
      </div>
      <CircleIcon icon={Loader} size={36} iconSize={20} className={`absolute left-[336px] top-[166px] ${floatShadow}`} />

      {/* map overlays */}
      <span className="absolute left-[298px] top-[336px] flex h-[22px] w-[22px] items-center justify-center rounded-full border-[1.5px] border-white bg-[#2f6ae0] text-[11px] font-semibold text-white">
        A
      </span>
      <PetMarker className="absolute left-[52px] top-[362px]" size={52} />
      <div className="absolute left-[22px] top-[414px] h-[30px] whitespace-nowrap bg-[#eef06a] px-[10px] pt-[3px] text-[14px] font-semibold leading-[22px] text-black">
        {lost.place}
      </div>

      <div className={`absolute left-[290px] top-[603px] flex h-[38px] items-center gap-[6px] rounded-full bg-white px-[14px] text-[13px] font-semibold ${floatShadow}`} style={{ color: '#2f6ae0' }}>
        {lost.share}
        <Share size={14} strokeWidth={2.4} />
      </div>
      <div className={`absolute left-[222px] top-[650px] flex h-[39px] items-center gap-[7px] rounded-full bg-white px-[14px] text-[13px] font-semibold ${floatShadow}`} style={{ color: fi.red }}>
        {lost.lostMode}
        <TriangleAlert size={17} strokeWidth={2.2} fill={fi.red} stroke="#fff" />
      </div>

      {/* bottom sheet */}
      <div className="absolute inset-x-0 top-[708px] bottom-0 bg-white">
        <DeviceStatusRow status={lostStatus} className="absolute left-[21px] top-[22px]" />
        <div className="absolute left-[20px] right-[20px] top-[46px] flex items-baseline">
          <span className="text-[19.5px] font-semibold tracking-[-0.2px] text-black">{lost.place}</span>
          <span className="mx-[2px] flex-1 border-b-[2px] border-dotted border-[#b0b0b0]" />
          <span className="text-[15px]" style={{ color: fi.grey }}>{lost.duration}</span>
        </div>
        <div className="absolute left-[20px] top-[80px] text-[15px] text-[#333]">{lost.city}</div>
      </div>
    </AppScreen>
  )
}
