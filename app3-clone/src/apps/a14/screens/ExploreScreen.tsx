import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { explore } from '../data'
import { CategoryTabs } from '../components/CategoryTabs'
import { ExploreSearch } from '../components/ExploreSearch'
import { ExploreTabBar } from '../components/ExploreTabBar'
import { ListingCard } from '../components/ListingCard'
import { MapPill } from '../components/MapPill'

const CATEGORY_CENTERS = [42, 125, 218, 312, 400]

export function ExploreScreen() {
  return (
    <AppScreen className="font-inter">
      <StatusBar paddingX={33} paddingTop={14} fontSize={16} />
      <div className="mt-[-3px]">
        <ExploreSearch title={explore.searchTitle} sub={explore.searchSub} />
      </div>
      <div className="mt-[11px]">
        <CategoryTabs items={explore.categories} active={explore.activeCategory} centers={CATEGORY_CENTERS} />
      </div>
      <div className="mt-[23px] flex flex-col gap-[40px]">
        {explore.listings.map((l) => (
          <ListingCard key={l.id} listing={l} />
        ))}
      </div>
      <MapPill label={explore.mapLabel} className="absolute top-[682px] left-[147px]" />
      <ExploreTabBar tabs={explore.tabs} active={explore.activeTab} />
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
