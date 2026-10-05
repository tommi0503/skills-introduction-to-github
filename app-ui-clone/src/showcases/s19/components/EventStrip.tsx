import { ImagePlaceholder } from '../../../ui'
import type { EventCardData } from '../data'
import { t19 } from '../theme'

export interface EventStripProps {
  events: EventCardData[]
  top: number
  /** Left edge of the first card (logical px). */
  cardsLeft?: number
}

/** "네이버페이 이달의 이벤트" heading and the horizontally scrolling coloured event cards. */
export function EventStrip({ events, top, cardsLeft = 15.5 }: EventStripProps) {
  return (
    <div className="absolute inset-x-0" style={{ top }}>
      <div style={{ marginLeft: 23.7, fontSize: 19.9, fontWeight: 700, letterSpacing: -0.5, color: '#fff' }}>
        <span style={{ color: t19.accent }}>네이버페이</span> 이달의 이벤트
      </div>
      <div className="absolute flex" style={{ left: cardsLeft, top: 43, gap: 9.3 }}>
        {events.map((e, i) => (
          <div key={i} className="relative shrink-0" style={{ width: 155.8, height: 200, borderRadius: 16, background: e.color }}>
            <ImagePlaceholder
              label="event illustration"
              tone="#d9dbe0"
              className="absolute rounded-full"
              style={{ left: 38.2, top: 31, width: 78.4, height: 78.4 }}
            />
            {e.caption && (
              <div
                className="absolute inset-x-0 text-center"
                style={{ top: 131.5, fontSize: 14, color: 'rgba(255,255,255,0.78)', letterSpacing: -0.4 }}
              >
                {e.caption}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
