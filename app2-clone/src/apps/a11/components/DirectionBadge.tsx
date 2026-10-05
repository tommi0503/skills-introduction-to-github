export interface DirectionBadgeProps {
  x: number
  y: number
  size: number
  value: string
  caption: string
  /** arrow head position and rotation (deg, 0 = pointing right) */
  arrow: { x: number; y: number; rotate: number }
}

/** Small round read-out sitting outside the compass ring with a pointer triangle. */
export function DirectionBadge({ x, y, size, value, caption, arrow }: DirectionBadgeProps) {
  return (
    <>
      <div
        className="absolute flex flex-col items-center justify-center rounded-full border border-white/10 bg-[#36405c]/80 text-white"
        style={{ left: x - size / 2, top: y - size / 2, width: size, height: size }}
      >
        <span className="text-[13px] leading-[14px] font-bold">{value}</span>
        <span className="text-[6px] leading-[8px] font-semibold tracking-[0.3px] text-white/50">{caption}</span>
      </div>
      <svg
        className="absolute"
        width={12}
        height={12}
        style={{ left: arrow.x - 6, top: arrow.y - 6, transform: `rotate(${arrow.rotate}deg)` }}
      >
        <path d="M1 0.5 L11 6 L1 11.5 Z" fill="rgba(255,255,255,0.75)" />
      </svg>
    </>
  )
}
