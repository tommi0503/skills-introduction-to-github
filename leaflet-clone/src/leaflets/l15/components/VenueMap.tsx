import { concertTheme as t } from '../../shared-1516/theme'

export interface VenueMapProps {
  title: string
  width: number
  height: number
}

/** Simplified route diagram: rounded grey card with street lines and a venue dot. */
export function VenueMap({ title, width, height }: VenueMapProps) {
  const line = { background: t.mapLine }
  return (
    <div className="relative rounded-[13px]" style={{ width, height, background: t.mapBox }}>
      <div className={`${t.font.display} absolute inset-x-0 text-center text-[16px]`} style={{ top: 28, color: t.ink }}>
        {title}
      </div>
      <div className="absolute" style={{ ...line, left: 33, top: 116, width: 301, height: 2 }} />
      <div className="absolute" style={{ ...line, left: 94, top: 77, width: 2, height: 105 }} />
      <div className="absolute" style={{ ...line, left: 275, top: 75, width: 2, height: 106 }} />
      <div className="absolute rounded-full" style={{ background: '#4a1f22', left: 87, top: 109, width: 16, height: 16 }} />
    </div>
  )
}
