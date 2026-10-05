import { Placed } from '../../../ui'
import { AppStatusBar } from '../components/AppStatusBar'
import { BookShelf } from '../components/BookShelf'
import { FadeOut } from '../components/FadeOut'
import { library, shelves } from '../data'
import { theme } from '../theme'

/** Left phone — "My Favourite BOOKS" shelves. */
export function LibraryScreen() {
  return (
    <div className="absolute inset-0">
      <AppStatusBar />
      <Placed x={0} y={86} width={393} className="text-center text-[#111]">
        <div className="font-inter text-[13.6px] leading-[20px] font-semibold tracking-[-0.01em]">{library.eyebrow}</div>
      </Placed>
      <Placed x={0} y={102} width={393} className="text-center">
        <div className="font-times text-[63px] leading-[63px] tracking-[-0.015em] text-[#111]">{library.title}</div>
      </Placed>

      <Placed x={0} y={198} width={393}>
        {shelves.map((s) => (
          <BookShelf key={s.title} shelf={s} />
        ))}
      </Placed>

      <FadeOut top={722} color={theme.screen} />

      <Placed x={113} y={775}>
        <button type="button" className="h-[58px] w-[167px] rounded-full bg-black font-inter text-[15px] font-semibold text-white">
          {library.cta}
        </button>
      </Placed>
    </div>
  )
}
