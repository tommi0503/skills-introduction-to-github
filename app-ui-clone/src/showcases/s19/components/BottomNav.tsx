import { ChartSpline, Folder, House } from 'lucide-react'
import { HomeIndicator } from '../../../ui'
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
    </span>
  )
}

function CameraFab() {
  return (
    <div
      className="absolute flex items-center justify-center rounded-full"
      style={{ left: 195.5 - 30, top: -11.5, width: 60, height: 60, background: '#fff' }}
    >
      <div className="flex items-center justify-center rounded-full" style={{ width: 50, height: 50, background: '#00df55' }}>
        <div className="relative flex items-center justify-center" style={{ width: 26.5, height: 26.5, borderRadius: 7, background: '#050505' }}>
          <span className="rounded-full" style={{ width: 11, height: 11, border: '2.4px solid #00df55' }} />
          <span className="absolute rounded-full" style={{ width: 3, height: 3, top: 4.5, right: 5, background: '#00df55' }} />
        </div>
      </div>
    </div>
  )
}

/** White app tab bar with the raised green QR/camera button. */
export function BottomNav({ items, top = 757.5 }: { items: NavItem[]; top?: number }) {
  return (
    <div className="absolute inset-x-0 bottom-0 z-30 bg-white" style={{ top }}>
      <CameraFab />
      {items.map((it) => (
        <div key={it.label} className="absolute flex flex-col items-center" style={{ left: it.x - 30, width: 60, top: 9 }}>
          <div className="flex items-center justify-center" style={{ height: 24 }}>
            <NavIcon kind={it.icon} />
          </div>
          <span style={{ marginTop: 8, fontSize: 11, color: '#333', letterSpacing: -0.3, fontWeight: 500 }}>{it.label}</span>
        </div>
      ))}
      <HomeIndicator width={138} bottom={7.5} className="!h-[4.5px]" />
    </div>
  )
}
