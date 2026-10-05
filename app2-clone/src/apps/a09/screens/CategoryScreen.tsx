import { ChevronLeft, Search } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { category } from '../data'
import { FvStatusBar } from '../components/FvStatusBar'
import { RoundButton } from '../components/RoundButton'
import { FilterChips } from '../components/FilterChips'
import { SubcategoryCard } from '../components/SubcategoryCard'
import { GigRow } from '../components/GigRow'
import { FiverrTabBar } from '../components/FiverrTabBar'

export function CategoryScreen() {
  return (
    <AppScreen background="#fafafa" className="font-figtree">
      <FvStatusBar />
      <RoundButton icon={ChevronLeft} iconSize={24} className="absolute top-[58px] left-[14px]" />
      <RoundButton icon={Search} iconSize={17} strokeWidth={2.4} className="absolute top-[58px] right-[17px]" />
      <h1 className="absolute inset-x-0 top-[128px] text-center text-[21px] leading-[28px] font-medium text-[#222325]">{category.title}</h1>
      <FilterChips items={category.filters} className="absolute top-[177px] left-[14px]" />
      <div className="absolute top-[231px] left-[14px] flex gap-[12px]">
        {category.subcategories.map((s) => (
          <SubcategoryCard key={s} label={s} />
        ))}
      </div>
      <div className="absolute top-[372px] left-[9px] flex flex-col gap-[15.5px]">
        {category.gigs.map((g) => (
          <GigRow key={g.title} gig={g} />
        ))}
      </div>
      <FiverrTabBar active="search" />
    </AppScreen>
  )
}
