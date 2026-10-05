import { ArrowRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Pill } from '../components/Pill'
import { Lines } from '../components/Lines'
import { hero } from '../data'
import { theme, type } from '../theme'

export function Hero() {
  return (
    <section className="absolute left-0 w-full text-center" style={{ top: 228, color: theme.ink }}>
      <h1 style={type.display}>
        {hero.lines.map((line) => (
          <div key={line.before} className="flex h-20 items-center justify-center gap-[17px] whitespace-nowrap">
            <span>{line.before}</span>
            <ImagePlaceholder label={line.icon} style={{ width: 68, height: 68, borderRadius: '30%', marginTop: -2 }} />
            <span>{line.after}</span>
          </div>
        ))}
      </h1>
      <Lines lines={hero.lead} style={{ ...type.lead, color: theme.muted, marginTop: 40 }} />
      <div className="flex justify-center gap-2" style={{ marginTop: 64 }}>
        <Pill variant="dark">{hero.primary}</Pill>
        <Pill variant="soft" style={{ paddingRight: 14 }}>
          {hero.secondary}
          <ArrowRight size={20} strokeWidth={2} />
        </Pill>
      </div>
    </section>
  )
}
