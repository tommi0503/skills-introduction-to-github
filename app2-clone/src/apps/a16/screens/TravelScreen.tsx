import { ChevronLeft, Share } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { BookTile } from '../components/BookTile'
import { Chrome } from '../components/Chrome'
import { CircleButton } from '../components/CircleButton'
import { travel } from '../data'
import { theme } from '../theme'

export function TravelScreen() {
  return (
    <AppScreen>
      <header className="absolute inset-x-0 top-0 h-[256px]" style={{ background: theme.travel }}>
        <Chrome color="#fff" chipClassName="bg-[#8a6a67]/95!" />
        <CircleButton
          icon={ChevronLeft}
          iconSize={20}
          toneClassName={theme.headerButton}
          className="absolute top-[68px] left-[18px]"
        />
        <CircleButton
          icon={Share}
          iconSize={18}
          toneClassName={theme.headerButton}
          className="absolute top-[68px] right-[24px]"
        />
        <h1 className="absolute inset-x-0 top-[123px] text-center text-[23px] font-normal text-white">{travel.title}</h1>
        <p className="absolute inset-x-[40px] top-[162px] text-center text-[13.5px] leading-[17px] text-white/90">{travel.description}</p>
        <p className="absolute inset-x-0 top-[233px] text-center text-[11.5px] text-white/55">{travel.meta}</p>
      </header>
      <div className="absolute top-[277px] left-[17px] grid grid-cols-2 gap-x-[16px] gap-y-[32px]">
        {travel.books.map((b) => (
          <BookTile key={b.key} book={b} />
        ))}
      </div>
    </AppScreen>
  )
}
