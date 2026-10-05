interface BottomFadeProps {
  height: number
  to?: string
}

/** Frosted fade that dissolves scrolled content into the bottom edge of the screen. */
export function BottomFade({ height, to = 'rgba(221,221,221,0.96)' }: BottomFadeProps) {
  return (
    <div
      className="pointer-events-none absolute inset-x-0 bottom-0 z-30"
      style={{ height, background: `linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(240,240,240,0.85) 45%, ${to} 100%)` }}
    />
  )
}
