import { ChevronDown, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { OrangeButton } from '../components/OrangeButton'
import { announcement, nav } from '../data'
import { theme } from '../theme'

/** Announcement strip + main navigation. */
export function Header() {
  return (
    <header className={`absolute left-0 top-0 z-10 w-[1440px] text-white ${theme.font.sans}`}>
      <div className="relative flex h-[32px] items-center justify-center text-[12px] leading-[16px]" style={{ background: theme.color.bar }}>
        <span>{announcement.text}</span>
        <span className="ml-[3px] underline">{announcement.link}</span>
        <X size={14} className="absolute left-[1413px] top-[9px]" />
      </div>
      <div className="relative h-[54px]" style={{ background: theme.color.nav }}>
        <ImagePlaceholder label="Giga logo" tone="#e8e6e2" className="absolute left-[56px] top-[16px] h-[22px] w-[22px] rounded-full" />
        <span className="absolute left-[85px] top-[15px] text-[21px] font-medium leading-[24px] tracking-[-0.5px]">{nav.brand}</span>
        {nav.menu.map((m) => (
          <span key={m.label} className="absolute top-[15px] flex items-center gap-[7px] text-[14px] leading-[24px] text-white/80" style={{ left: m.x }}>
            {m.label}
            <ChevronDown size={14} strokeWidth={1.5} className="opacity-70" />
          </span>
        ))}
        <span className="absolute left-[1168px] top-[6px] flex h-[42px] w-[85px] items-center justify-center font-inter text-[14px]">
          {nav.signIn}
        </span>
        <OrangeButton label={nav.cta} className="left-[1265px] top-[6px] h-[42px] w-[119px] border border-white/40" />
      </div>
    </header>
  )
}
