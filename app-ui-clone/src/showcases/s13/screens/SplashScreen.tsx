import { MoveRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { BarberPhone } from '../components/BarberPhone'
import { Headline } from '../components/Headline'
import { copy } from '../data'
import { theme } from '../theme'

/** Full-bleed photo splash with headline, CTA and "powered by" footer. */
export function SplashScreen() {
  return (
    <BarberPhone background={theme.ink} statusColor="#fff">
      <ImagePlaceholder label="Barber cutting hair photo" className="absolute inset-0 -z-0" />
      <div className="absolute inset-x-0 top-0 h-[90px]" style={{ background: theme.splashTopScrim }} />
      <div className="absolute inset-x-0 bottom-0 top-[420px]" style={{ background: theme.splashScrim }} />
      <div className="absolute inset-x-0 top-[546px] flex flex-col items-center text-white">
        <Headline lines={copy.splashTitle} className="text-center text-[30px] font-medium leading-[37.6px] tracking-[-0.2px]" />
      </div>
      <button
        type="button"
        className="absolute left-[34px] top-[693px] flex h-[50px] w-[309px] items-center justify-center gap-[8px] rounded-full bg-white text-[14px] font-medium text-black"
      >
        {copy.splashCta}
        <MoveRight size={16} strokeWidth={1.8} />
      </button>
      <div className="absolute inset-x-0 top-[762px] flex items-center justify-center gap-[7px] text-[12.5px] text-white/75">
        <span>{copy.poweredBy}</span>
        <ImagePlaceholder label="Level App logo" className="h-[15px] w-[15px] rounded-[3px]" />
        <ImagePlaceholder label="Level App wordmark" className="h-[10px] w-[76px] rounded-[2px] opacity-80" />
      </div>
    </BarberPhone>
  )
}
