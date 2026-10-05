import { ArrowLeft, ArrowRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Eyebrow } from '../components/Eyebrow'
import { OrangeButton } from '../components/OrangeButton'
import { PixelText } from '../components/PixelText'
import { industries as s } from '../data'
import { theme } from '../theme'

const CARD = { top: 1975, h: 432 }

function NavButton({ left, active, children }: { left: number; active?: boolean; children: React.ReactNode }) {
  return (
    <span
      className="absolute top-[1868px] flex h-[44px] w-[44px] items-center justify-center rounded-[8px] border border-white/10"
      style={{ left, background: active ? '#2b2c2e' : '#161718', color: active ? '#fff' : 'rgba(232,237,239,0.45)' }}
    >
      {children}
    </span>
  )
}

/** "Giga agents are flexible." — header with carousel arrows, lead-capture card and stacked industry photos. */
export function Industries() {
  return (
    <section className={theme.font.sans}>
      <Eyebrow label={s.eyebrow} className="left-[169px] top-[1779px]" color="rgba(255,255,255,0.88)" />
      <PixelText lines={[s.title]} size={52.63} lineHeight={63} className="absolute left-[169px] top-[1805px]" style={{ color: theme.color.text, letterSpacing: '-0.6px' }} />
      <p className="absolute left-[169px] top-[1885px] text-[18px] leading-[27px]" style={{ color: theme.color.textDim }}>
        {s.body}
      </p>
      <NavButton left={1179}>
        <ArrowLeft size={18} />
      </NavButton>
      <NavButton left={1227} active>
        <ArrowRight size={18} />
      </NavButton>

      <div className="absolute left-[166px] top-[1972px] h-[438px] w-[1108px] rounded-[6px]" style={{ background: '#101112' }} />
      <div className="absolute left-[169px] w-[602px] rounded-l-[4px]" style={{ top: CARD.top, height: CARD.h, background: theme.color.card }}>
        <h3 className="absolute left-[25px] top-[24px] w-[540px] font-inter text-[34px] leading-[39.44px] tracking-[-0.68px]">
          <span style={{ color: 'rgb(236,235,231)' }}>{s.cardLead} </span>
          <span style={{ color: 'rgba(232,237,239,0.62)' }}>{s.cardRest}</span>
        </h3>
        <div className="absolute left-[25px] top-[243px] h-[104px] w-[536px] rounded-[12px] border border-white/10 shadow-[inset_0_2px_6px_rgba(0,0,0,0.6)]" style={{ background: theme.color.field }}>
          <span className={`absolute left-[16px] top-[16px] text-[15px] text-white/45 ${theme.font.mono}`}>{s.field}</span>
        </div>
        <OrangeButton label={s.submit} className="left-[413px] top-[363px] h-[44px] w-[148px]" />
      </div>
      {s.slices.map(([x, w], i) => (
        <ImagePlaceholder
          key={x}
          label="industry photo"
          tone={i === 0 ? undefined : theme.color.imageDark}
          className="absolute border-l border-black/40"
          style={{ left: x, top: CARD.top, width: w, height: CARD.h }}
        />
      ))}
    </section>
  )
}
