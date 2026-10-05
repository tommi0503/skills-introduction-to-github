import { EyebrowLink } from '../components/EyebrowLink'
import { Prose } from '../components/Prose'
import { intro } from '../data'
import { theme } from '../theme'

export function Intro() {
  return (
    <section className="absolute inset-x-0 top-[1115px]">
      <EyebrowLink label={intro.link} className="absolute left-[241px] top-0" />
      <div className={`${theme.fonts.display} absolute left-[561px] top-0 w-[638px] space-y-[32px] text-[20px] leading-7 tracking-[-0.3px]`}>
        {intro.paragraphs.map((p) => <Prose key={p.strong} strong={p.strong} rest={p.rest} />)}
      </div>
    </section>
  )
}
