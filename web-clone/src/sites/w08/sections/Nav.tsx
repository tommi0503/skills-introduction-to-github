import { ChevronDown } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Button } from '../components/Button'
import { nav } from '../data'
import { theme, type } from '../theme'

export function Nav() {
  return (
    <header
      className="absolute flex items-center"
      style={{
        left: 48,
        top: 24,
        width: 1344,
        height: 72,
        borderRadius: 16,
        background: theme.white,
        color: theme.ink,
        boxShadow: '0 8px 24px rgba(7,26,49,0.06)',
        paddingLeft: 16,
        paddingRight: 12,
      }}
    >
      <ImagePlaceholder label="Calendly mark" style={{ width: 32, height: 32, borderRadius: 10 }} />
      <ImagePlaceholder label="Calendly wordmark" style={{ width: 116, height: 28, marginLeft: 8 }} />
      <nav className="ml-[32px] flex items-center gap-[20px]">
        {nav.menus.map((m) => (
          <span key={m.label} className="flex items-center gap-[4px]" style={type.nav}>
            {m.label}
            {m.dropdown && <ChevronDown size={16} strokeWidth={2} />}
          </span>
        ))}
      </nav>
      <span className="ml-auto" style={type.nav}>
        {nav.sales}
      </span>
      <Button variant="outline" width={73} height={47} style={{ marginLeft: 18, fontWeight: 400 }}>
        {nav.login}
      </Button>
      <Button width={159} height={47} style={{ marginLeft: 12, fontWeight: 400 }}>
        {nav.cta}
      </Button>
    </header>
  )
}
