import { ImagePlaceholder } from '../../../ui'
import { Lines } from '../components/Lines'
import { hero } from '../data'
import { theme, type } from '../theme'

export function Hero() {
  return (
    <section className="absolute left-0 w-full text-center" style={{ top: 228, color: theme.ink }}>
      <h1 className={theme.display} style={type.h1}>
        <Lines lines={hero.title} />
      </h1>
      <Lines lines={hero.lead} style={{ ...type.lead, color: theme.muted, marginTop: 24 }} />
      <div className="flex justify-center gap-4" style={{ marginTop: 33 }}>
        {hero.signups.map((s) => (
          <span
            key={s.provider}
            className="flex items-center"
            style={{ ...type.button, width: s.width, height: 50, borderRadius: 10, background: theme.ink, color: theme.page, padding: 6 }}
          >
            <span className="flex h-[38px] w-[38px] items-center justify-center rounded-[7px] bg-white">
              <ImagePlaceholder label={`${s.provider} logo`} style={{ width: 20, height: 20 }} />
            </span>
            <span style={{ marginLeft: 12 }}>{s.label}</span>
          </span>
        ))}
      </div>
      <p style={{ ...type.micro, color: theme.muted, marginTop: 16 }}>
        <span className="underline" style={{ fontWeight: 400 }}>
          {hero.email}
        </span>{' '}
        • {hero.note}
      </p>
    </section>
  )
}
