import { ChevronLeft, ChevronRight, Mic } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Button } from '../components/Button'
import { Column } from '../components/Column'
import { hero } from '../data'
import { serifStyle, theme } from '../theme'

const ORIGIN = { x: 81, y: 64 }

export function Hero() {
  return (
    <Column height={722} borderBottom>
      <div className="absolute inset-x-0 top-[54px] flex flex-col items-center text-center">
        <h1 className={theme.fonts.serif} style={serifStyle(40, 46)}>
          <span style={{ color: theme.faded }}>{hero.titleMuted}</span>
          <br />
          <span style={{ color: theme.ink }}>{hero.title}</span>
        </h1>
        <p className="mt-[24px] w-[520px] text-[16px] leading-6" style={{ color: theme.muted }}>{hero.body}</p>
        <div className="mt-[32px] flex gap-[12px]">
          {hero.ctas.map((c) => (
            <Button key={c.label} variant={c.variant}>{c.label}</Button>
          ))}
        </div>
      </div>

      {hero.orbs.map(([x, y, s]) => (
        <ImagePlaceholder
          key={x}
          label="voice orb"
          className="absolute rounded-full"
          style={{ left: x - ORIGIN.x, top: y - ORIGIN.y, width: s, height: s }}
        />
      ))}
      <div
        className="absolute flex size-[48px] items-center justify-center rounded-full bg-[#fefefe]/90"
        style={{ left: 696 - ORIGIN.x, top: 500 - ORIGIN.y }}
      >
        <Mic className="size-[20px]" style={{ color: theme.greenDark }} fill={theme.greenDark} strokeWidth={2} />
      </div>
      <ChevronLeft className="absolute size-[20px]" style={{ left: 314 - ORIGIN.x, top: 514 - ORIGIN.y, color: theme.faded }} strokeWidth={1.75} />
      <ChevronRight className="absolute size-[20px]" style={{ left: 1106 - ORIGIN.x, top: 514 - ORIGIN.y, color: theme.faded }} strokeWidth={1.75} />

      <div className="absolute inset-x-0 text-center" style={{ top: 665 - ORIGIN.y }}>
        <p className="text-[18px] leading-[24.75px] font-medium" style={{ color: theme.ink }}>{hero.voice.name}</p>
        <p className="mt-[4px] text-[12px] leading-[16.5px]" style={{ color: theme.muted }}>{hero.voice.tone}</p>
      </div>
    </Column>
  )
}
