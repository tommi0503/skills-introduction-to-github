import { ChevronDown } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { colors, fonts } from '../theme'
import { PillButton } from '../components/primitives'

/** Top navigation bar: logo, menu links, auth actions. */
export function Header() {
  return (
    <header className={`relative flex h-[48px] items-center pl-[148px] pr-[148px] ${fonts.sans}`}>
      <ImagePlaceholder label="GitBook logo" style={{ width: nav.logo.w, height: nav.logo.h }} />
      <nav className="ml-[174px] flex items-center gap-[31px]">
        {nav.links.map((l) => (
          <span key={l.label} className="flex items-center gap-[6px] text-[14px] leading-[21px] font-medium tracking-[0.14px]" style={{ color: colors.body }}>
            {l.label}
            {l.menu && <ChevronDown size={12} strokeWidth={1.6} color={colors.muted} />}
          </span>
        ))}
      </nav>
      <div className="ml-auto flex items-center">
        <span className="mr-[24px] text-[14px] leading-[22px] font-medium" style={{ color: colors.muted }}>
          {nav.login}
        </span>
        <PillButton variant="nav" className="!h-[32px] !px-[15px] !text-[14px] !tracking-normal !font-medium">
          {nav.secondary}
        </PillButton>
        <PillButton className="ml-[8px] !h-[32px] !px-[20px] !text-[14px] !tracking-normal !font-medium">{nav.primary}</PillButton>
      </div>
    </header>
  )
}
