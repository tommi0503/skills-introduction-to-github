import { ChartSpline, Folder, House } from 'lucide-react'
import type { NavItem } from '../data'

const ICON = 24

function NavIcon({ kind }: { kind: NavItem['icon'] }) {
  const common = { size: ICON, strokeWidth: 1.6, color: '#222' }
  if (kind === 'asset')
    return (
      <span className="relative flex items-center justify-center">
        <Folder {...common} size={30} />
        <span className="absolute font-bold" style={{ fontSize: 11, top: 9, color: '#222' }}>₩</span>
      </span>
    )
  if (kind === 'benefit')
    return (
      <span
        className="flex items-center justify-center rounded-full font-bold"
        style={{ width: 22.5, height: 22.5, border: '1.6px solid #222', fontSize: 12, color: '#222' }}
      >
        N
      </span>
    )
  if (kind === 'stock') return <ChartSpline {...common} />
  return (
    <span className="relative flex items-center justify-center">
      <House {...common} />
      <span className="absolute grid grid-cols-2" style={{ top: 11, gap: 1.6 }}>
        {[0, 1, 2, 3].map((i) => (
          <span key={i} style={{ width: 2.6, height: 2.6, borderRadius: 0.6, background: '#222' }} />
        ))}
      </span>
    </span>
  )
}

function CameraFab({ color }: { color: string }) {
  return (
    <div
      className="absolute flex items-center justify-center rounded-full"
      style={{ left: 195.5 - 29, top: -9.5, width: 58, height: 58, background: '#fff' }}
    >
      <div className="flex items-center justify-center rounded-full" style={{ width: 50, height: 50, background: color }}>
        <div className="relative flex items-center justify-center" style={{ width: 26.5, height: 26.5, borderRadius: 7, background: '#050505' }}>
          <span className="rounded-full" style={{ width: 11, height: 11, border: `2.4px solid ${color}` }} />
          <span className="absolute rounded-full" style={{ width: 3, height: 3, top: 4.5, right: 5, background: color }} />
        </div>
      </div>
    </div>
  )
}

/** White app tab bar with the raised green QR/camera button. */
export interface BottomNavProps {
  items: NavItem[]
  top?: number
  fabColor?: string
  indicatorColor?: string
}

export function BottomNav({ items, top = 757.5, fabColor = '#00df55', indicatorColor = '#111' }: BottomNavProps) {
  return (
    <div className="absolute inset-x-0 bottom-0 z-30 bg-white" style={{ top }}>
      <CameraFab color={fabColor} />
      {items.map((it) => (
        <div key={it.label} className="absolute flex flex-col items-center" style={{ left: it.x - 30, width: 60, top: 9 }}>
          <div className="flex items-center justify-center" style={{ height: 24 }}>
            <NavIcon kind={it.icon} />
          </div>
          <span style={{ marginTop: 3.5, fontSize: 11, color: '#333', letterSpacing: -0.3, fontWeight: 500 }}>{it.label}</span>
        </div>
      ))}
      <span className="absolute left-1/2 -translate-x-1/2 rounded-full" style={{ width: 138, height: 4.5, bottom: 7.5, background: indicatorColor }} />
    </div>
  )
}
