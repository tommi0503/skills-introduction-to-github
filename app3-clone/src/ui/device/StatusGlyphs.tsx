/**
 * iOS status-bar glyphs drawn with plain boxes so they inherit currentColor.
 * (Lucide's signal/battery icons don't match the iOS silhouette.)
 */
export function SignalBars({ size = 1 }: { size?: number }) {
  const heights = [4, 6, 8.5, 11]
  return (
    <div className="flex items-end" style={{ gap: 1.5 * size, height: 11 * size }}>
      {heights.map((h) => (
        <span key={h} className="rounded-[1px] bg-current" style={{ width: 3 * size, height: h * size }} />
      ))}
    </div>
  )
}

export interface BatteryProps {
  size?: number
  /** 0..1 */
  level?: number
  /** Fill colour override (e.g. green when charging). */
  fill?: string
  charging?: boolean
}

export function Battery({ size = 1, level = 1, fill, charging }: BatteryProps) {
  return (
    <div className="flex items-center" style={{ gap: 1 * size }}>
      <div
        className="relative rounded-[4px] border border-current/40"
        style={{ width: 25 * size, height: 12 * size, padding: 1.5 * size, borderRadius: 4 * size }}
      >
        <div
          className="h-full rounded-[2px]"
          style={{ width: `${level * 100}%`, background: fill ?? 'currentColor', borderRadius: 2 * size }}
        />
        {charging && (
          <span
            className="absolute inset-0 flex items-center justify-center font-bold"
            style={{ fontSize: 9 * size, lineHeight: 1 }}
          >
            ⚡
          </span>
        )}
      </div>
      <span className="rounded-r-sm bg-current/40" style={{ width: 1.5 * size, height: 4 * size }} />
    </div>
  )
}
