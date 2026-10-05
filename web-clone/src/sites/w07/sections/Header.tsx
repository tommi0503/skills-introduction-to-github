import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { theme, type } from '../theme'

export function Header() {
  return (
    <header className="absolute left-0 top-0 h-[92px] w-full" style={{ color: theme.ink }}>
      <ImagePlaceholder label="Mobbin logo" className="absolute" style={{ left: 198, top: 36, width: 43, height: 20 }} />
      <nav className="absolute flex gap-6" style={{ left: 273, top: 35 }}>
        {nav.links.map((l) => (
          <span key={l} style={type.nav}>
            {l}
          </span>
        ))}
      </nav>
      {nav.socials.map((s) => (
        <ImagePlaceholder key={s.label} label={s.label} className="absolute" style={{ left: s.x, top: 36, width: 20, height: 20 }} />
      ))}
      <span className="absolute" style={{ left: 1173, top: 32, width: 1, height: 28, background: theme.divider }} />
      <span className="absolute" style={{ ...type.nav, left: 1198, top: 35 }}>
        {nav.login}
      </span>
    </header>
  )
}
