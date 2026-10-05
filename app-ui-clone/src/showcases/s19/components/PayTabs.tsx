import { t19 } from '../theme'

export interface PayTabsProps {
  tabs: string[]
  active: number
  height?: number
  className?: string
  style?: React.CSSProperties
}

/** Black pill track with three tabs; the active one sits on a dark grey pill. */
export function PayTabs({ tabs, active, height = 43.5, className, style }: PayTabsProps) {
  return (
    <div className={className} style={{ height, borderRadius: height / 2, background: t19.segTrack, ...style }}>
      <div className="relative flex h-full items-center" style={{ padding: '0 5px' }}>
        {tabs.map((label, i) => (
          <div key={label} className="relative flex flex-1 items-center justify-center" style={{ height: 33.5 }}>
            {i === active && (
              <span className="absolute rounded-full" style={{ inset: '0 4px 0 1.5px', background: t19.segPill }} />
            )}
            <span
              className="relative"
              style={{
                fontSize: 17.2,
                letterSpacing: -0.3,
                fontWeight: i === active ? 700 : 600,
                color: i === active ? '#fff' : t19.segText,
              }}
            >
              {label}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
