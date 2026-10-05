import { StationMapFrame } from '../components/StationMapFrame'
import { StationSummaryCard } from '../components/StationSummaryCard'
import { selectedStation, summaryConditions, zoomedPins } from '../data'

export function StationSelected() {
  return (
    <StationMapFrame pins={zoomedPins}>
      <div className="absolute top-[386px] left-[275.5px] h-[6px] w-[6px] rounded-full bg-[#3d86e8]" />
      <StationSummaryCard className="top-[600px] left-[22px]" {...selectedStation} conditions={summaryConditions} />
    </StationMapFrame>
  )
}
