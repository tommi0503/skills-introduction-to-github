import { ImagePlaceholder } from '../../../ui'
import { SectionTitle } from '../components/SectionTitle'
import { teamsSection as s } from '../data'
import { theme } from '../theme'

const LOGO = { w: 100, h: 60, pitch: 120 }
/** Edge fade: logos near the strip ends are dimmed like the reference mask. */
const fade = (i: number, n: number) => (i === 0 || i === n - 1 ? 0.15 : 1)

/** Client logo marquee (two rows of logo placeholders) under a centred title. */
export function Teams() {
  return (
    <>
      <div className="absolute left-0 top-[3659px] flex justify-center" style={{ width: theme.contentWidth }}>
        <SectionTitle text={s.title} size={38} lineHeight={38} />
      </div>
      {s.rows.map((row) =>
        Array.from({ length: row.count }, (_, i) => (
          <ImagePlaceholder
            key={`${row.y}-${i}`}
            label="customer logo"
            className="absolute"
            style={{ left: row.startX + i * LOGO.pitch, top: row.y, width: LOGO.w, height: LOGO.h, opacity: fade(i, row.count) }}
          />
        )),
      )}
    </>
  )
}
