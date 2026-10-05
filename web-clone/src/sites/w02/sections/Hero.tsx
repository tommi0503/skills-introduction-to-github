import { ChevronRight, Download } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { BrowserMockup } from '../components/BrowserMockup'
import { hero, nav } from '../data'
import { theme } from '../theme'

/** Rounded sky card holding nav, headline and the browser mockup. Coordinates are relative to the card (16,16). */
export function Hero() {
  return (
    <div
      className="absolute left-[16px] top-[16px] h-[993px] w-[1408px] overflow-hidden rounded-[33.6px]"
      style={{ boxShadow: '0 6px 12px rgba(0,0,0,0.12)' }}
    >
      <ImagePlaceholder label="sky background" tone={theme.sky} className="absolute inset-0" />

      <header className="absolute inset-x-0 top-[10px] flex h-[36px] items-center pl-[21px] pr-[17px]">
        <div className="flex items-center gap-[5px]">
          <ImagePlaceholder label="Aside logo mark" tone="#0a0a0a" className="size-[26px] rounded-full" />
          <span className={`${theme.fonts.display} text-[24px] leading-none font-medium tracking-[-0.5px]`} style={{ color: theme.ink }}>{nav.brand}</span>
        </div>
        <nav className="absolute left-[524px] flex gap-[40px] text-[14px] leading-5 font-medium" style={{ color: theme.ink }}>
          {nav.links.map((l) => <span key={l}>{l}</span>)}
        </nav>
        <span className={`${theme.fonts.display} ml-auto flex h-[36px] w-[86px] items-center justify-center rounded-[16.8px] text-[14px] leading-5 font-medium`} style={{ background: '#377885', color: '#fafafa' }}>
          {nav.cta}
        </span>
      </header>

      <div className="absolute inset-x-0 top-[121px] flex flex-col items-center text-center">
        <span className={`${theme.fonts.display} flex h-[24px] items-center rounded-full border px-[9px] text-[12px] leading-4 font-semibold tracking-[0.12px]`} style={{ borderColor: 'rgba(10,40,50,0.18)', color: 'rgba(10,40,50,0.75)', background: 'rgba(255,255,255,0.12)' }}>
          {hero.badge}
          <ChevronRight className="ml-[2px] size-[12px]" />
        </span>
        <h1 className={`${theme.fonts.display} mt-[16px] text-[48px] leading-[52px] font-normal tracking-[-0.48px]`} style={{ color: theme.ink }}>
          {hero.title.map((l) => <span key={l} className="block">{l}</span>)}
        </h1>
        <span className="mt-[33px] flex h-[38px] w-[120px] items-center justify-center gap-[6px] rounded-full text-[16px] leading-6 font-[450]" style={{ background: '#6f8084', color: '#fafafa' }}>
          <Download className="size-[16px]" strokeWidth={1.75} />
          {hero.cta}
        </span>
      </div>

      <BrowserMockup className="left-[60px] top-[401px] h-[640px] w-[1288px]" />
    </div>
  )
}
