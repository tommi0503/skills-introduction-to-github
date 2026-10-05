import { ImagePlaceholder } from '../../../ui'
import { BondWordmark } from '../components/BondWordmark'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { splash } from '../data'
import { bond } from '../theme'

export function SplashScreen() {
  return (
    <div className="relative h-full font-inter" style={{ background: bond.splash }}>
      <HighlightStatusBar />
      <ImagePlaceholder label="bond cloud logo" className="absolute rounded-[40px]" style={{ left: 151, top: 326, width: 89, height: 74 }} />
      <div className="absolute inset-x-0 flex justify-center" style={{ top: 424 }}>
        <BondWordmark text={splash.brand} size={51} />
      </div>
      <p className="absolute inset-x-0 text-center text-[11.7px] leading-[18.5px] text-[#9a9a9a]" style={{ top: 719 }}>
        {splash.legal.lead}
        <br />
        <span className="text-[#555]">{splash.legal.links[0]}</span> &amp;{' '}
        <span className="text-[#555]">{splash.legal.links[1]}</span>
      </p>
      <div
        className="absolute flex items-center justify-center rounded-full text-[15px] font-semibold text-white"
        style={{ left: 23, top: 774, width: 347, height: 52, background: bond.ink, boxShadow: '0 6px 14px rgba(0,0,0,0.18)' }}
      >
        {splash.cta}
      </div>
    </div>
  )
}
