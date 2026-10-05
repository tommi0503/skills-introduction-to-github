import { ImagePlaceholder } from '../../../ui'
import type { FloatingTile } from '../data'
import { theme } from '../theme'

/** Scatter of tilted image tiles (each a flat placeholder) over a canvas area. */
export function FloatingTiles({ tiles }: { tiles: FloatingTile[] }) {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
      {tiles.map((t, i) => (
        <ImagePlaceholder
          key={i}
          className="absolute"
          style={{
            left: t.x - t.w / 2,
            top: t.y - t.h / 2,
            width: t.w,
            height: t.h,
            borderRadius: theme.cardRadius,
            transform: `rotate(${t.r}deg)`,
          }}
        />
      ))}
    </div>
  )
}
