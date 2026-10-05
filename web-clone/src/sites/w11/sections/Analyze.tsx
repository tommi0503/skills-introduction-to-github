import { ImagePlaceholder } from '../../../ui'
import { analyze } from '../data'
import { theme } from '../theme'
import { SerifTitle } from '../components/SerifTitle'

/** Two-up cards: photo with headline, and dark product mockup card. Section origin: y=3894. */
export function Analyze() {
  return (
    <section className="relative h-[700px]">
      <div className="absolute left-[32px] top-0 h-[700px] w-[676px] overflow-hidden rounded-[24px]">
        <ImagePlaceholder label="Flowers photo" tone={theme.tones.photo} className="absolute inset-0" />
        <SerifTitle
          lines={analyze.title}
          size={80}
          lineHeight={80}
          letterSpacing={-0.8}
          className="absolute left-[96px] top-[96px] w-[484px] text-[#fafafa]"
        />
        <p className="absolute left-[96px] top-[481px] m-0 w-[484px] text-center font-inter text-[20px] leading-[27px] font-light tracking-[-0.2px] text-white">
          {analyze.body}
        </p>
      </div>
      <div
        className="absolute left-[733px] top-0 h-[700px] w-[675px] overflow-hidden rounded-[24px] border"
        style={{ background: theme.colors.card, borderColor: theme.colors.cardBorder }}
      >
        <ImagePlaceholder label="Calendar mockup" tone={theme.tones.mock} className="absolute left-[92px] top-[198px] h-[232px] w-[96px] rounded-r-[12px]" />
      </div>
    </section>
  )
}
