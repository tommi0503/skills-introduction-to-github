import { Search, Sparkle } from 'lucide-react'
import { Lines } from '../components/Lines'
import { story } from '../data'
import { theme, type } from '../theme'

export function Story() {
  return (
    <section className="absolute" style={{ left: theme.gutter, top: 1868, ...type.h2, color: theme.ink }}>
      <Lines lines={story.primary} />
      <Lines lines={story.secondary} style={{ color: theme.muted, marginTop: 44 }} />
      <div className="flex items-center" style={{ marginTop: 80 }}>
        <span className="relative mr-4 inline-block h-10 w-10">
          <Search size={34} strokeWidth={2.4} className="absolute bottom-0 left-0" />
          <Sparkle size={16} strokeWidth={0} fill="currentColor" className="absolute right-0 top-0" />
        </span>
        <span>{story.feature}</span>
        <span className="ml-[1px] inline-block h-[42px] w-[2px]" style={{ background: theme.ink }} />
      </div>
    </section>
  )
}
