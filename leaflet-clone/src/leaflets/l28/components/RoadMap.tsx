import { MapPin } from 'lucide-react'
import { Pill, Placed } from '../../../ui'
import { autumn } from '../../shared-2829/theme'
import { directions } from '../data'

/** Schematic road diagram: rounded bars, a location marker and its label. */
export function RoadMap() {
  const { roads, marker } = directions
  return (
    <>
      {roads.map((r, i) => (
        <Placed key={i} x={r.x} y={r.y} width={r.w} height={r.h} className="rounded-full" style={{ background: autumn.roads }} />
      ))}
      <Placed x={marker.labelX} y={marker.labelY} width={120} height={26} className="rounded-full" style={{ background: autumn.markerLabel }}>
        <Pill className="h-full w-full text-[14.5px] font-semibold text-white">{marker.label}</Pill>
      </Placed>
      <Placed x={marker.x - 7} y={marker.y - 3}>
        <MapPin size={42} fill={autumn.marker} color={autumn.marker} strokeWidth={1.5} className="[&_circle]:fill-white [&_circle]:stroke-white" />
      </Placed>
    </>
  )
}
