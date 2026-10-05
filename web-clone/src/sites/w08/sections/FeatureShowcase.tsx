import { ArrowRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Lines } from '../components/Lines'
import { activeFeature, features, learnMore } from '../data'
import { theme, type } from '../theme'

/** Gradient-art stage with tab icons and the active feature card (calendar mockup as placeholder). */
export function FeatureShowcase() {
  const f = features[activeFeature]
  const Icon = f.icon
  return (
    <section className="absolute" style={{ left: 120, top: 624, width: 1200, height: 610 }}>
      <ImagePlaceholder label="Gradient background art" className="absolute inset-0" style={{ borderRadius: 32 }} />
      <div className="absolute flex gap-2" style={{ left: 476, top: 48 }}>
        {features.map((t, i) => (
          <span
            key={t.label}
            className="flex h-14 w-14 items-center justify-center rounded-[18px]"
            style={{ background: i === activeFeature ? theme.tabActive : theme.tabIdle, boxShadow: '0 0 0 4px #fff inset', color: i === activeFeature ? theme.ink : '#8b929b' }}
          >
            <t.icon size={26} strokeWidth={2} />
          </span>
        ))}
      </div>
      <span className="absolute h-4 w-1 bg-white" style={{ left: 502, top: 104 }} />
      <article
        className="absolute"
        style={{ left: 102, top: 118, width: 996, height: 429, borderRadius: 24, background: theme.page, color: theme.ink }}
      >
        <div className="absolute" style={{ left: 48, top: 58 }}>
          <div className={`flex items-center gap-1 ${theme.display}`} style={type.label}>
            <span className="flex h-6 w-6 items-center justify-center rounded-md" style={{ background: theme.tabActive }}>
              <Icon size={15} strokeWidth={2.4} />
            </span>
            {f.label}
          </div>
          <h2 className={theme.body} style={{ ...type.featureTitle, marginTop: 28 }}>
            <Lines lines={f.title} />
          </h2>
          <Lines lines={f.body} style={{ ...type.body, color: theme.muted, marginTop: 16 }} />
          <span
            className="mt-6 inline-flex items-center gap-2 border-b pb-[9px] pt-[9px]"
            style={{ ...type.nav, borderColor: theme.ink, paddingRight: 2 }}
          >
            {learnMore}
            <ArrowRight size={16} strokeWidth={2} />
          </span>
        </div>
        <ImagePlaceholder label="Calendar booking mockup" className="absolute" style={{ left: 432, top: 48, width: 516, height: 333, borderRadius: 16 }} />
      </article>
    </section>
  )
}
