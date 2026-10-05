import { Lines } from '../components/Lines'
import { PlacedImage } from '../components/Placeholder'
import { library, libraryMedia, toolbar, toolbarSearch as SearchIcon, type LibraryCard } from '../data'
import { theme, type } from '../theme'

export function Library() {
  return (
    <section className="absolute left-0 w-full" style={{ top: 2889, color: theme.ink }}>
      <Lines lines={library.title} className="text-center" style={type.h2} />
      <div
        className="absolute grid grid-cols-3 gap-5"
        style={{ left: theme.gutter, top: 176, width: theme.contentWidth, gridAutoRows: 330 }}
      >
        {library.cards.map((c) => (
          <Card key={c} title={c} />
        ))}
      </div>
    </section>
  )
}

function Card({ title }: { title: LibraryCard }) {
  return (
    <div className="relative overflow-hidden" style={{ borderRadius: 24, background: theme.surface }}>
      <p className="relative z-10 text-center" style={{ ...type.cardTitle, paddingTop: 24 }}>
        {title}
      </p>
      {libraryMedia[title].map((r, i) => (
        <PlacedImage key={i} rect={r} label={`${title} preview`} />
      ))}
      {title === 'UI Elements' && <Toolbar />}
    </div>
  )
}

/** Floating icon toolbar shown in the "UI Elements" card. */
function Toolbar() {
  return (
    <div className="absolute flex items-center gap-2" style={{ left: 27, top: 162 }}>
      <div className="flex h-12 items-center rounded-full bg-white px-[6px]">
        {toolbar.map(({ icon: Icon, active }, i) => (
          <span
            key={i}
            className="flex h-9 w-[54px] items-center justify-center rounded-full"
            style={{ background: active ? '#f7f7f7' : undefined }}
          >
            <Icon size={20} strokeWidth={2} />
          </span>
        ))}
      </div>
      <span className="flex h-12 w-12 items-center justify-center rounded-full bg-white">
        <SearchIcon size={20} strokeWidth={2.4} />
      </span>
    </div>
  )
}
