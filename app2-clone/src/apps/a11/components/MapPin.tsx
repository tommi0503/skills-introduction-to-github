import { Sailboat } from 'lucide-react'
import type { Pin } from '../data'

/** Tide-station annotation: blue disc with a buoy glyph and an optional caption below. */
export function MapPin({ pin }: { pin: Pin }) {
  const d = pin.size === 'lg' ? 60 : 26
  const lines = pin.label ?? []
  return (
    <>
      <div
        className="absolute flex items-center justify-center rounded-full text-white"
        style={{
          left: pin.x - d / 2,
          top: pin.y - d / 2,
          width: d,
          height: d,
          background: 'radial-gradient(circle at 50% 35%, #5aa2f2, #2f76d6)',
          boxShadow: pin.size === 'lg' ? '0 0 0 2px rgba(10,20,50,0.5), 0 4px 14px rgba(0,0,0,0.4)' : '0 1px 4px rgba(0,0,0,0.35)',
        }}
      >
        <Sailboat size={d * 0.55} strokeWidth={pin.size === 'lg' ? 2 : 2.4} />
      </div>
      {lines.length > 0 && (
        <div
          className="absolute -translate-x-1/2 text-center text-[9.5px] leading-[10.5px] font-bold tracking-[-0.1px] whitespace-nowrap text-white"
          style={{
            left: pin.labelX ?? pin.x,
            top: pin.labelY ?? pin.y + d / 2 + 12.5,
            textShadow: '0 0 3px rgba(0,0,0,0.9), 0 0 1px #000',
          }}
        >
          {lines.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
      )}
    </>
  )
}
