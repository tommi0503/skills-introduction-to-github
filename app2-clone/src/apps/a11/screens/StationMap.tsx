import { ImagePlaceholder } from '../../../ui'
import { StationMapFrame } from '../components/StationMapFrame'
import { overviewPins } from '../data'

export function StationMap() {
  return (
    <StationMapFrame pins={overviewPins}>
      <div className="absolute top-[709px] left-[24px] flex items-center gap-[1px] text-[17px] font-medium tracking-[-0.3px]">
        <ImagePlaceholder label="maps logo" className="h-[14px] w-[12px] rounded-[3px]" />
        Maps
      </div>
      <div className="absolute top-[714px] left-[84px] text-[9px] font-medium text-white/70 underline">Legal</div>
    </StationMapFrame>
  )
}
