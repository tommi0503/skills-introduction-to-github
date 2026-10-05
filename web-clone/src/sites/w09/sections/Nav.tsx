import { ScanSearch, Search } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { PillButton } from '../components/PillButton'
import { nav } from '../data'
import { theme } from '../theme'

const linkStyle = { fontSize: 15, lineHeight: '22px', letterSpacing: '-0.28px', color: theme.color.navText }

/** Top bar: logo, text links, centred search field, auth actions. */
export function Nav() {
  return (
    <header className="absolute left-0 top-0 z-10 h-[92px]" style={{ width: theme.contentWidth }}>
      <ImagePlaceholder label="Cosmos logo" className="absolute left-[37px] top-[35px] h-[22px] w-[22px] rounded-full" />
      <nav className="absolute left-[84px] top-[35px] flex gap-[24px] font-medium" style={linkStyle}>
        {nav.links.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </nav>
      <div
        className="absolute left-[488px] top-[19px] flex h-[54px] w-[455px] items-center rounded-full pl-[16px] pr-[14px]"
        style={{ background: theme.color.searchBg, border: `1px solid ${theme.color.searchBorder}` }}
      >
        <Search size={18} strokeWidth={1.75} color={theme.color.hint} />
        <span className="ml-[11px] text-[14px]" style={{ color: theme.color.hint, letterSpacing: '-0.32px' }}>
          {nav.searchHint} {nav.searchExample}
        </span>
        <ScanSearch size={20} strokeWidth={1.5} color={theme.color.hint} className="ml-auto" />
        <ImagePlaceholder label="AI search mark" className="ml-[14px] h-[20px] w-[20px] rounded-full" />
      </div>
      <span className="absolute left-[1219px] top-[35px] font-medium" style={linkStyle}>
        {nav.login}
      </span>
      <PillButton className="absolute left-[1288px] top-[22px] h-[48px] w-[101px] text-[15px]" style={{ letterSpacing: '-0.28px' }}>
        {nav.signup}
      </PillButton>
    </header>
  )
}
