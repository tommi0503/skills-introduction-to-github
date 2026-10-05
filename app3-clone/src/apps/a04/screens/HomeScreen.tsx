import { Bell, ChevronDown, Menu, Plus, Search } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { HomeTabBar } from '../components/HomeTabBar'
import { ListingRow } from '../components/ListingRow'
import { categories, homeHeader, listings, writeLabel } from '../data'
import { kr } from '../theme'

function Header() {
  return (
    <div className="absolute inset-x-0 top-[68px] flex h-[32px] items-center pr-[18px] pl-[20px]">
      <span className="flex flex-1 items-center gap-[3px] text-[19px] font-bold tracking-[-0.3px]">
        {homeHeader.town}
        <ChevronDown size={17} strokeWidth={2.2} className="mt-[2px]" />
      </span>
      <div className="flex items-center gap-[19px]">
        <Menu size={25} strokeWidth={1.6} />
        <Search size={24} strokeWidth={1.9} />
        <Bell size={23} strokeWidth={1.9} />
      </div>
    </div>
  )
}

function CategoryChips() {
  return (
    <div className="absolute top-[129px] left-[16px] flex gap-[9px]">
      {categories.map(({ key, icon: Icon, label }) => (
        <span key={key} className="flex h-[38px] items-center gap-[5px] rounded-[10px] px-[14px] text-[13px]" style={{ background: kr.chip }}>
          <Icon size={14} strokeWidth={2} />
          {label}
        </span>
      ))}
    </div>
  )
}

/** Karrot-style home feed: town header, category shortcuts, listings, FAB and tab bar. */
export function HomeScreen() {
  return (
    <AppScreen className="font-pretendard" style={{ color: kr.text }}>
      <Chrome />
      <Header />
      <CategoryChips />
      <div className="absolute inset-x-0 top-[172px]">
        {listings.map((l) => (
          <ListingRow key={l.key} item={l} />
        ))}
      </div>
      <span
        className="absolute top-[703px] right-[18px] flex h-[45px] items-center gap-[4px] rounded-full pr-[18px] pl-[14px] text-[15px] font-semibold text-white shadow-[0_3px_8px_rgba(0,0,0,0.15)]"
        style={{ background: kr.orange }}
      >
        <Plus size={18} strokeWidth={2.4} />
        {writeLabel}
      </span>
      <HomeTabBar activeKey="home" />
    </AppScreen>
  )
}
