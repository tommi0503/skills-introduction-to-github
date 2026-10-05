import { Search } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar, cn } from '../../../ui'
import { activeVertical, feed, navTabs, verticals } from '../data'
import { FeeToast } from '../components/FeeToast'
import { NavBar } from '../components/NavBar'
import { StayRowSection } from '../components/StayRowSection'
import { VerticalTabs } from '../components/VerticalTabs'
import { FONT, palette as c } from '../theme'

export function FeedScreen() {
  return (
    <AppScreen className={cn(FONT)}>
      <header className="relative h-[196px] bg-[#f7f7f7]" style={{ boxShadow: '0 2px 6px rgba(0,0,0,0.05)' }}>
        <StatusBar paddingX={34} paddingTop={18} fontSize={16} />
        <div
          className="mx-[24px] mt-[9px] flex h-[57px] items-center justify-center gap-[8px] rounded-full bg-white text-[13.5px] font-semibold"
          style={{ color: c.text, boxShadow: '0 3px 14px rgba(0,0,0,0.12)' }}
        >
          <Search size={13} strokeWidth={2.8} />
          {feed.searchLabel}
        </div>
        <VerticalTabs
          items={verticals}
          active={activeVertical}
          centers={[80, 194, 309]}
          iconSize={44}
          showNew
          labelGap={1}
          underlineWidth={40}
          className="mt-[13px]"
        />
      </header>
      <div className="mt-[42px] flex flex-col gap-[25px]">
        {feed.rows.map((r) => (
          <StayRowSection key={r.id} row={r} />
        ))}
      </div>
      <FeeToast label={feed.toast} className="absolute top-[694px] left-[97px] z-20" />
      <NavBar tabs={navTabs} active="explore" />
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
