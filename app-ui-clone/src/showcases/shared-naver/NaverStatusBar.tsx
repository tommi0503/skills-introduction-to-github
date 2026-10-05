import { BellOff, Navigation, Wifi, Zap } from 'lucide-react'
import { SignalBars, cn } from '../../ui'

export type TimeGlyph = 'location' | 'silent' | 'none'

export interface NaverStatusBarProps {
  time: string
  glyph?: TimeGlyph
  /** Text & icon colour. */
  color?: string
  /** Battery: charging = green fill + bolt. */
  charging?: boolean
  /** 0..1 */
  level?: number
  /** Vertical centre of the row (logical px). */
  centerY?: number
  className?: string
}

function TimeAddon({ glyph }: { glyph: TimeGlyph }) {
  if (glyph === 'location')
    return <Navigation size={13} strokeWidth={0} fill="currentColor" style={{ transform: 'rotate(0deg)', marginLeft: 3 }} />
  if (glyph === 'silent') return <BellOff size={14} strokeWidth={2.4} fill="currentColor" style={{ marginLeft: 3 }} />
  return null
}

function BatteryGlyph({ charging, level, color }: { charging: boolean; level: number; color: string }) {
  return (
    <div className="relative flex items-center" style={{ width: 27, height: 13 }}>
      <div
        className="relative"
        style={{ width: 24, height: 12.5, borderRadius: 4, border: `1.2px solid ${color}`, opacity: 1, padding: 1.6 }}
      >
        <div className="absolute inset-0" style={{ borderRadius: 4, border: `1.2px solid ${color}`, opacity: 0 }} />
        <div
          style={{
            width: `${level * 100}%`,
            height: '100%',
            borderRadius: 2,
            background: charging ? '#3fc94f' : color,
          }}
        />
      </div>
      <span style={{ width: 1.6, height: 4.5, marginLeft: 1, borderRadius: 1, background: color, opacity: 0.45 }} />
      {charging && (
        <Zap
          size={12}
          strokeWidth={1.6}
          fill={color}
          stroke="#fff"
          className="absolute"
          style={{ left: 6.5, top: 0.5, color }}
        />
      )}
    </div>
  )
}

/** iOS status bar as captured in the Naver Pay screenshots (logical px, absolutely laid out). */
export function NaverStatusBar({
  time,
  glyph = 'location',
  color = '#000',
  charging = false,
  level = 0.6,
  centerY = 29.3,
  className,
}: NaverStatusBarProps) {
  return (
    <div className={cn('pointer-events-none absolute inset-x-0 top-0 z-40', className)} style={{ height: 50, color }}>
      <div
        className="absolute flex items-center font-inter font-semibold"
        style={{ left: 45.5, top: centerY - 10, height: 20, fontSize: 17, letterSpacing: -0.3 }}
      >
        <span>{time}</span>
        <TimeAddon glyph={glyph} />
      </div>
      <div className="absolute flex items-center" style={{ right: 32, top: centerY - 7, height: 14, gap: 7 }}>
        <SignalBars size={1.03} />
        <Wifi size={17} strokeWidth={2.9} />
        <BatteryGlyph charging={charging} level={level} color={charging ? color : color} />
      </div>
    </div>
  )
}
