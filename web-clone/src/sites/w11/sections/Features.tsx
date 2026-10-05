import { ChevronLeft, ChevronRight, Pause } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { features, type Feature } from '../data'
import { theme } from '../theme'

const CARD_W = 420
const GAP = 24

function FeatureCard({ f }: { f: Feature }) {
  return (
    <article
      className="relative h-[592px] shrink-0 rounded-[24px] border"
      style={{ width: CARD_W, background: theme.colors.card, borderColor: theme.colors.cardBorder }}
    >
      <ImagePlaceholder
        label="Product UI mockup"
        tone={theme.tones.mock}
        className="absolute left-[48px] top-[48px] w-[322px] rounded-[20px]"
        style={{ height: f.mediaH }}
      />
      <div className="absolute left-[48px] w-[322px] font-inter font-light" style={{ top: f.titleTop }}>
        <h3 className="m-0 text-[20px] leading-[21.6px] font-light tracking-[-0.2px] text-white">{f.title}</h3>
        <p className="m-0 mt-[12px] text-[16px] leading-[21.6px] tracking-[-0.16px] text-white/30">{f.body}</p>
      </div>
    </article>
  )
}

const controls = [ChevronLeft, Pause, ChevronRight]

/** Horizontal feature carousel with playback controls. Section origin: y=2330. */
export function Features() {
  return (
    <section className="relative h-[664px]">
      <div className="absolute left-[32px] top-[-1px] flex" style={{ gap: GAP }}>
        {features.map((f) => (
          <FeatureCard key={f.title} f={f} />
        ))}
      </div>
      <div className="absolute left-[624px] top-[616px] flex gap-[24px]">
        {controls.map((Icon, i) => (
          <button
            key={i}
            className="flex h-[48px] w-[48px] items-center justify-center rounded-full text-white"
            style={{ background: theme.colors.control }}
          >
            <Icon size={i === 1 ? 22 : 24} strokeWidth={1.5} />
          </button>
        ))}
      </div>
    </section>
  )
}
