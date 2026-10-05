import { ChevronDown } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { nav, navActions } from '../data'
import { theme } from '../theme'
import { PillButton } from '../components/PillButton'

export function Nav() {
  return (
    <header className="relative h-16" style={{ color: theme.ink }}>
      <ImagePlaceholder label="logo" className="absolute" style={{ left: 110, top: 19, width: 50, height: 20 }} />
      <nav className="absolute flex gap-1" style={{ left: 195, top: 16 }}>
        {nav.map((l) => (
          <span key={l.label} className="flex h-8 items-center gap-1 px-3 text-[13px] font-[450] leading-[19.5px]">
            {l.label}
            {l.dropdown && <ChevronDown size={12} strokeWidth={2} />}
          </span>
        ))}
      </nav>
      <div className="absolute flex items-center" style={{ left: 1055, top: 12 }}>
        <PillButton variant="soft" className="w-[127px]" style={{ height: 40 }}>
          {navActions.secondary}
        </PillButton>
        <span className="ml-[9px] flex h-9 overflow-hidden rounded-full" style={{ background: theme.ink }}>
          <span className="flex w-[100px] items-center justify-center text-[14px] font-[450] text-white">{navActions.primary}</span>
          <span className="flex w-[37px] items-center justify-center border-l border-white/20 text-white">
            <ChevronDown size={16} strokeWidth={2} />
          </span>
        </span>
      </div>
    </header>
  )
}
