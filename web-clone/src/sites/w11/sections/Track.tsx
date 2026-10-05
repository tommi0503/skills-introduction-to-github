import { track } from '../data'
import { MonoButton } from '../components/MonoButton'
import { SerifTitle } from '../components/SerifTitle'

/** "Track your entire financial life." headline + CTA. Section origin: y=1900. */
export function Track() {
  return (
    <section className="relative h-[430px]">
      <SerifTitle
        lines={track.title}
        size={80}
        lineHeight={80}
        letterSpacing={-0.8}
        className="absolute left-0 top-[118px] w-full text-[#fafafa]"
      />
      <MonoButton variant="dark" className="absolute left-[634px] top-[302px] h-[48px] w-[172px] rounded-[8px] border border-white/10">
        {track.cta}
      </MonoButton>
    </section>
  )
}
