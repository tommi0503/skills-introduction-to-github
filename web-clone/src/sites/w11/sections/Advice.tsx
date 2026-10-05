import { PieChart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { advice } from '../data'
import { theme } from '../theme'
import { SerifTitle } from '../components/SerifTitle'

/** Dot-grid canvas, headline and stacked notification pills. Section origin: y=2994. */
export function Advice() {
  const n = advice.notification
  return (
    <section className="relative h-[900px]">
      <ImagePlaceholder label="Dot grid canvas" tone={theme.tones.canvas} className="absolute left-[20px] top-0 h-[900px] w-[1400px]" />
      <span className="absolute left-[712px] top-[236px] h-[16px] w-[16px] rounded-full" style={{ background: theme.colors.green }} />
      <SerifTitle
        as="h1"
        lines={advice.title}
        size={80}
        lineHeight={80}
        letterSpacing={-0.8}
        className="absolute left-0 top-[316px] w-full text-white"
      />
      <div className="absolute left-[452px] top-[524px] h-[90px] w-[536px] rounded-[224px] border border-white/[0.04]" style={{ background: theme.colors.pillBack2 }} />
      <div className="absolute left-[419px] top-[537px] h-[101px] w-[603px] rounded-[224px] border border-white/[0.05]" style={{ background: theme.colors.pillBack1 }} />
      <div
        className="absolute left-[385px] top-[550px] h-[112px] w-[670px] rounded-[224px] border border-white/[0.06] font-inter text-white"
        style={{ background: theme.colors.pill }}
      >
        <PieChart size={32} strokeWidth={1.5} className="absolute left-[36px] top-[40px] text-white/40" />
        <div className="absolute left-[92px] top-[26px] w-[466px] text-[20px] leading-[30px] font-light tracking-[-0.2px]">
          {n.text} <strong className="font-bold">{n.strong}</strong>
        </div>
        <div className="absolute left-[582px] top-[44px] text-[16px] leading-[24px] font-light tracking-[-0.16px] text-white/30">{n.time}</div>
      </div>
    </section>
  )
}
