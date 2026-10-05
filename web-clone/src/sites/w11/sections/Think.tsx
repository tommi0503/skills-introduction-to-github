import { ImagePlaceholder } from '../../../ui'
import { think } from '../data'
import { theme } from '../theme'
import { SerifTitle } from '../components/SerifTitle'

/** Rounded dark panel with headline, subcopy and award badges. Section origin: y=1232. */
export function Think() {
  return (
    <section className="relative h-[528px]">
      <div className="absolute left-[32px] top-[16px] h-[497px] w-[1376px] overflow-hidden rounded-[32px]" style={{ background: theme.colors.panel }}>
        <ImagePlaceholder label="Gradient glow" tone={theme.tones.glow} className="absolute bottom-0 left-0 h-[70px] w-full" />
      </div>
      <SerifTitle
        lines={think.title}
        size={48}
        lineHeight={55.2}
        className="absolute left-0 top-[112px] w-full text-[#fafafa]"
      />
      <p className="absolute left-[510px] top-[247px] m-0 w-[420px] text-center font-inter text-[16px] leading-[24px] font-light text-white/60">
        {think.body}
      </p>
      {think.awards.map((a) => (
        <ImagePlaceholder
          key={a.x}
          label="Award badge"
          tone={theme.tones.award}
          className="absolute top-[343px] h-[75px]"
          style={{ left: a.x, width: a.w }}
        />
      ))}
    </section>
  )
}
