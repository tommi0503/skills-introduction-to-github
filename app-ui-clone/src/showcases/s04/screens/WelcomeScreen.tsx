import { Mail, Truck } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { PillButton } from '../components/PillButton'
import { welcome } from '../data'
import { fonts, theme } from '../theme'

/** Rays behind the hero burger: a plain conic gradient, not an illustration. */
const rays = `repeating-conic-gradient(from 8deg at 50% 52%, ${theme.welcomeRay} 0deg 11deg, transparent 11deg 30deg)`

export function WelcomeScreen() {
  return (
    <div className={`absolute inset-0 ${fonts.ui}`} style={{ background: theme.welcomeRed }}>
      <div className="absolute inset-0 opacity-50" style={{ background: rays }} />

      <div
        className="absolute left-[50px] top-[80px] flex h-[38px] w-[260px] -rotate-[1deg] items-center justify-center text-[21px] font-[450]"
        style={{ background: theme.cream, color: theme.creamText, borderRadius: 3 }}
      >
        {welcome.ribbon}
      </div>

      <h1
        className={`absolute inset-x-0 top-[152px] z-10 origin-top scale-x-[0.84] text-center text-white ${fonts.display}`}
        style={{ fontSize: 74, lineHeight: '64px', letterSpacing: -0.6 }}
      >
        {welcome.titleLines.map((line) => (
          <span key={line} className="block">
            {line}
          </span>
        ))}
      </h1>

      <ImagePlaceholder label="burger photo" className="absolute left-[30px] top-[270px] h-[286px] w-[316px] rounded-[48px]" />

      <div className="absolute inset-x-[16px] top-[578px] flex flex-col gap-[16px]">
        <PillButton
          label={welcome.primaryCta}
          icon={Mail}
          className="bg-[#f6d8ce] text-[16.5px] font-medium text-[#2a1a17]"
          iconClassName="text-[#2a1a17]"
        />
        <PillButton label={welcome.secondaryCta} icon={Truck} className="border-[1.5px] border-[#f3a28f] text-[16.5px] font-medium text-white" />
      </div>

      <p className="absolute inset-x-[22px] top-[722px] text-center text-[12.6px] leading-[16.6px]" style={{ color: '#f4a594' }}>
        {welcome.legal.prefix}
        <b className="font-medium text-white">{welcome.legal.terms}</b>
        {welcome.legal.joiner}
        <b className="font-medium text-white">{welcome.legal.privacy}</b>
      </p>
    </div>
  )
}
