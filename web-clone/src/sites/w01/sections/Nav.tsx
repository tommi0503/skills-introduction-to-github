import { ChevronDown } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Button } from '../components/Button'
import { Column } from '../components/Column'
import { nav } from '../data'
import { theme } from '../theme'

export function Nav() {
  return (
    <Column height={64} borderBottom className="flex items-center px-[48px]">
      <div className="flex items-center gap-[6px]">
        <ImagePlaceholder label="Cartesia mark" className="size-[20px]" />
        <span className={`${theme.fonts.serif} text-[24px] leading-5 tracking-[-0.2px]`} style={{ color: theme.ink }}>
          CARTESIA
        </span>
      </div>
      <nav className="ml-[16px] flex items-center gap-[4px]">
        {nav.links.map((l) => (
          <span key={l.label} className="flex h-9 items-center gap-[4px] px-[8px] text-[14px] leading-5 font-medium" style={{ color: theme.ink }}>
            {l.label}
            {l.dropdown && <ChevronDown className="size-3" strokeWidth={1.75} />}
          </span>
        ))}
      </nav>
      <div className="ml-auto flex items-center gap-[16px]">
        {nav.actions.map((a) => (
          <Button key={a.label} variant={a.variant}>{a.label}</Button>
        ))}
      </div>
    </Column>
  )
}
