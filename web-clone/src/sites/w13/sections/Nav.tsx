import { ChevronDown, Search } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { Pill } from '../components/Pill'

/** Primary navigation (y 60–100). */
export function Nav() {
  return (
    <header className="absolute left-0 top-[60px] z-10 h-[40px] w-[1440px] font-geist text-[14px] text-[#e9ebdf]">
      <ImagePlaceholder label="Retool logo mark" className="absolute left-[32px] top-[11px] h-[18px] w-[18px]" />
      <span className="absolute left-[56px] top-[5px] font-inter text-[22px] leading-[30px] font-normal tracking-[-0.6px]">{nav.brand}</span>
      <nav className="absolute left-[165px] top-[11px] flex items-center gap-[23px] leading-[17px] tracking-[-0.25px]">
        {nav.links.map((l) => (
          <span key={l.label} className="flex items-center gap-[2px]">
            {l.label}
            {l.menu && <ChevronDown size={10} className="opacity-40" />}
          </span>
        ))}
        <Search size={15} className="ml-[1px] opacity-60" />
      </nav>
      <Pill variant="plain" className="absolute left-[1061px] w-[72px]">{nav.signIn}</Pill>
      <Pill variant="outline" className="absolute left-[1139px] w-[124px]">{nav.demo}</Pill>
      <Pill className="absolute left-[1272px] w-[121px]">{nav.cta}</Pill>
    </header>
  )
}
