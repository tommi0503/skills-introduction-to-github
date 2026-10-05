import { ImagePlaceholder } from '../../../ui'
import { hero } from '../data'
import { theme } from '../theme'
import { DownloadButton } from '../components/DownloadButton'

export function Hero() {
  return (
    <section className="relative h-[445px]">
      <ImagePlaceholder label="walking figure backdrop" tone="#2e2e2e" className="absolute inset-y-0 left-[104px] right-[104px]" />
      <div className="relative flex flex-col items-center pt-[65px]">
        <span
          className="flex h-8 items-center rounded-full px-[16px] text-[12px] font-medium tracking-[0.48px]"
          style={{ background: 'rgba(0,0,0,0.24)', color: theme.text82, boxShadow: 'inset 0 0 0 1px #111, 0 1px 0 #3b3b3b' }}
        >
          {hero.pill}
        </span>
        <h1 className={`${theme.serif} mt-[16px] text-[80px] font-bold leading-[72px] tracking-[-3.2px]`} style={{ color: theme.ink }}>
          {hero.title}
        </h1>
        <p className="mt-[36px] w-[568px] text-center text-[18px] leading-[28.8px]" style={{ color: theme.text82 }}>
          {hero.body}
        </p>
        <DownloadButton size="lg" className="mt-[33px] w-[248px]">
          {hero.cta}
        </DownloadButton>
        <div className="mt-[17px] flex items-baseline gap-[5px] font-medium" style={{ color: theme.text62 }}>
          <span className="text-[12px]">{hero.availableLabel}</span>
          <span className="text-[14px] underline decoration-white/30 underline-offset-[4px]">{hero.availableLink}</span>
        </div>
      </div>
    </section>
  )
}
