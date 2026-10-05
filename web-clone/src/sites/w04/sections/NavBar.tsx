import { ChevronsUpDown, OctagonAlert, Search } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { Pill } from '../components/Pill'

export function NavBar() {
  return (
    <header className="relative flex h-[72px] items-center px-5 text-[16px] font-medium text-[#262626]">
      <ImagePlaceholder label="Cloudflare cloud mark" className="h-[26px] w-[57px]" />
      <ImagePlaceholder label="Cloudflare wordmark" className="ml-3 h-3 w-[146px]" />
      <nav className="absolute left-[516px] top-[18px] flex">
        {nav.links.map((l) => (
          <span key={l.label} className="flex h-9 items-center gap-[7px] rounded-[6px] px-3 tracking-[-0.45px]">
            {l.label}
            {l.menu && <ChevronsUpDown className="size-4 text-[#262626]/40" strokeWidth={1.5} />}
          </span>
        ))}
      </nav>
      <div className="ml-auto flex items-center gap-1">
        <span className="mr-[10px] flex items-center gap-[6px] font-normal tracking-[-0.1px] text-[#b52831]">
          <OctagonAlert className="size-4" strokeWidth={1.75} />
          {nav.alert}
        </span>
        <Pill className="w-[66px]">{nav.login}</Pill>
        <Pill className="w-[126px]">{nav.contact}</Pill>
        <Pill className="w-[38px] px-0">
          <Search className="size-4 shrink-0" strokeWidth={2} />
        </Pill>
      </div>
    </header>
  )
}
