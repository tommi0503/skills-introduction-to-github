import type { Swatch } from '../data'

interface SwatchDotProps {
  swatch: Swatch
  size: number
}

/** Colour option dot; the selected one gets a white gap + outline ring. */
export function SwatchDot({ swatch, size }: SwatchDotProps) {
  return (
    <span
      className="block shrink-0 rounded-full"
      style={{
        width: size,
        height: size,
        background: swatch.color,
        boxShadow: swatch.selected ? `0 0 0 1px #fff, 0 0 0 2px ${swatch.color}` : undefined,
      }}
    />
  )
}
