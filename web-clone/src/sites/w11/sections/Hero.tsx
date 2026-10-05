import { WalletCards } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { hero } from '../data'
import { theme } from '../theme'
import { MonoButton } from '../components/MonoButton'
import { SerifTitle } from '../components/SerifTitle'
import { Nav } from './Nav'

/** Sky hero: promo pill, display title, CTA and the phone mockup with an advice card. */
export function Hero() {
  const { promo, phone, card } = hero
  return (
    <section className="relative h-[1232px] overflow-hidden text-white">
      <ImagePlaceholder label="Sky video background" tone={theme.tones.sky} className="absolute inset-0" />
      <Nav />

      <div className="absolute left-[600px] top-[135px] flex h-[38px] w-[240px] items-center rounded-[50px] bg-white/[0.05] pl-[14px] font-inter text-[12px] leading-[12px] tracking-[-0.12px] uppercase">
        <s className="text-white/40">{promo.was}</s>
        <span className="ml-[3px]">{promo.now}</span>
        <span className="ml-[9px] flex h-[22px] items-center rounded-[10px] bg-white/[0.08] px-[8px] text-[10px] font-medium tracking-[1.6px]">
          {promo.badge}
        </span>
      </div>

      <SerifTitle
        as="h1"
        lines={hero.titleLines}
        size={96}
        lineHeight={110.4}
        className="absolute left-0 top-[197px] w-full"
      />

      <p className="absolute left-[510px] top-[442px] m-0 w-[420px] text-center font-inter text-[16px] leading-[24px] font-light text-white/60">
        {hero.body}
      </p>
      <MonoButton arrow className="absolute left-[652px] top-[514px] h-[48px] w-[136px]">
        {hero.cta}
      </MonoButton>

      <ImagePlaceholder
        label="Phone mockup"
        tone={theme.tones.phone}
        className="absolute rounded-[90px]"
        style={{ left: phone.x, top: phone.y, width: phone.w, height: phone.h }}
      />
      <div className="absolute left-[696px] top-[690px] flex h-[48px] w-[48px] items-center justify-center rounded-[10px] border border-white/25 bg-white/[0.08]">
        <WalletCards size={20} strokeWidth={1.5} />
      </div>
      <div className={`${theme.fonts.serif} absolute left-0 top-[754px] w-full text-center text-[48px] leading-[55.2px] tracking-[-0.6px] text-[#fafafa]`}>
        {hero.found.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>

      <div className="absolute left-[477px] top-[904px] h-[248px] w-[468px] rounded-[24px] border border-white/15 bg-white/[0.08] pl-[26px]">
        <div className={`${theme.fonts.mono} mt-[26px] text-[15px] leading-[24px] font-medium tracking-[2.4px] uppercase text-white/30`}>
          {card.eyebrow}
        </div>
        <h3 className={`${theme.fonts.serif} m-0 mt-[23px] text-[36px] leading-[41.4px] font-normal text-white/80`}>{card.title}</h3>
        <p className="m-0 mt-[20px] w-[400px] font-inter text-[20px] leading-[28.4px] font-light tracking-[-0.2px]">{card.body}</p>
      </div>
    </section>
  )
}
