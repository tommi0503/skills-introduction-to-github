import { EyebrowLink } from '../components/EyebrowLink'
import { MediaCard } from '../components/MediaCard'
import { capability } from '../data'
import { theme } from '../theme'

export function Capability() {
  return (
    <section className="absolute inset-x-0 top-[1412px] h-[1300px]">
      <div className="absolute inset-y-0 h-[520px]" style={{ left: theme.column.left, width: theme.column.width, background: 'linear-gradient(#fafafa, #ffffff)' }} />
      <div className="relative flex flex-col items-center pt-[96px] text-center">
        <EyebrowLink label={capability.link} />
        <h2 className={`${theme.fonts.display} mt-[24px] text-[44px] leading-[48px] font-[450]`} style={{ color: theme.ink }}>
          {capability.title.map((l) => <span key={l} className="block">{l}</span>)}
        </h2>
      </div>
      <p className="absolute left-[361px] top-[616px] w-[718px] text-[18px] leading-7" style={{ color: theme.ink }}>{capability.body}</p>
      <div className="absolute left-[121px] top-[796px] flex gap-[24.5px]">
        {capability.cards.map((c) => <MediaCard key={c.title} label={`${c.title} demo`} {...c} />)}
      </div>
    </section>
  )
}
