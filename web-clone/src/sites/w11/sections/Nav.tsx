import { Plus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { MonoButton } from '../components/MonoButton'

/** Floating translucent navigation bar over the hero. */
export function Nav() {
  return (
    <header className="absolute left-[24px] top-[24px] z-20 h-[56px] w-[1392px] rounded-[10px] bg-black/[0.07]">
      <ImagePlaceholder label="Origin logo" className="absolute left-[24px] top-[18px] h-[22px] w-[20px] rounded-[6px]" />
      <nav className="absolute left-[516px] top-[11px] flex gap-[9px]">
        {nav.links.map((l) => (
          <MonoButton
            key={l.label}
            variant="ghost"
            className={l.menu ? 'h-[34px] bg-white/[0.04] px-[12px] font-medium rounded-[8px]' : 'h-[34px] bg-white/[0.04] px-[12px] font-normal rounded-[8px]'}
          >
            {l.label}
            {l.menu && <Plus size={16} strokeWidth={1.5} className="ml-[1px] opacity-80" />}
          </MonoButton>
        ))}
      </nav>
      <MonoButton variant="ghost" className="absolute left-[1172px] top-[11px] h-[34px] w-[69px] text-[#fafafa]">
        {nav.login}
      </MonoButton>
      <MonoButton variant="light" arrow className="absolute left-[1251px] top-[4px] h-[48px] w-[137px]">
        {nav.cta}
      </MonoButton>
    </header>
  )
}
