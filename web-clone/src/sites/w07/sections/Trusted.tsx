import { ImagePlaceholder } from '../../../ui'
import { trusted } from '../data'
import { theme, type } from '../theme'

export function Trusted() {
  return (
    <section className="absolute left-0 w-full" style={{ top: 1539 }}>
      <p className="text-center" style={{ ...type.small, color: theme.muted }}>
        {trusted.caption}
      </p>
      {trusted.logos.map((l) => (
        <ImagePlaceholder key={l.label} label={`${l.label} logo`} className="absolute" style={{ left: l.x, top: 60, width: l.w, height: 28 }} />
      ))}
      <hr className="absolute border-0" style={{ left: theme.gutter, top: 168, width: theme.contentWidth, height: 1, background: theme.surface }} />
    </section>
  )
}
