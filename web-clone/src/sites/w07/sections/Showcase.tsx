import { ImagePlaceholder } from '../../../ui'
import { carousel, type ShotKind } from '../data'
import { theme } from '../theme'

const CARD_W: Record<ShotKind, number> = { web: 576, phone: 304 }
const SHOT: Record<ShotKind, { w: number; h: number; r: number }> = {
  web: { w: 512, h: 320, r: 12 },
  phone: { w: 240, h: 520, r: 32 },
}

/** Horizontal strip of app screenshots, each card with an overlapping app icon. */
export function Showcase() {
  return (
    <section className="absolute left-0 w-full" style={{ top: 2345, height: 384 }}>
      {carousel.map((c) => (
        <div
          key={c.label}
          className="absolute top-0 overflow-hidden"
          style={{ left: c.x, width: CARD_W[c.kind], height: 384, borderRadius: 32, background: theme.surface }}
        >
          <ImagePlaceholder
            label={c.label}
            className="absolute"
            style={{ left: 32, top: 32, width: SHOT[c.kind].w, height: SHOT[c.kind].h, borderRadius: SHOT[c.kind].r }}
          />
          <ImagePlaceholder
            label="App icon"
            tone="#d4d6da"
            className="absolute"
            style={{ left: 20, top: 20, width: 63, height: 63, borderRadius: '30%' }}
          />
        </div>
      ))}
    </section>
  )
}
