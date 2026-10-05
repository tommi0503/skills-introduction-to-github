import { ImagePlaceholder } from '../../../ui'
import { Eyebrow } from '../components/Eyebrow'
import { PixelText } from '../components/PixelText'
import { hero } from '../data'
import { theme } from '../theme'
import { DemoWidget } from './DemoWidget'

/** Gradient-art hero (flat placeholder) with title, intro copy and the voice/chat demo widget. */
export function Hero() {
  return (
    <section className={`absolute left-0 top-0 h-[900px] w-[1440px] text-white ${theme.font.sans}`}>
      <ImagePlaceholder label="gradient artwork" tone={theme.color.heroArt} className="absolute inset-0" />
      <Eyebrow label={hero.eyebrow} className="left-[170px] top-[133px]" />
      <PixelText as="h1" lines={hero.title} size={72} lineHeight={64} className="absolute left-[170px] top-[168px]" style={{ letterSpacing: '-0.6px' }} />
      <p className="absolute left-[867px] top-[184px] w-[403px] text-[19px] leading-[27.55px]">{hero.body}</p>
      <DemoWidget />
    </section>
  )
}
