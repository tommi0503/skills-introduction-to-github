import { AppScreen } from '../../../ui'
import { CategoryRow } from '../components/CategoryRow'
import { FloatingTabBar } from '../components/FloatingTabBar'
import { HomeSearch } from '../components/HomeSearch'
import { HomeTabs } from '../components/HomeTabs'
import { OfferCarousel } from '../components/OfferCarousel'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { PromoBanner } from '../components/PromoBanner'
import { StoreSection } from '../components/StoreSection'
import { categories, homeTabs, navItems, offers, promo, searchPlaceholder, storeTiles, storeTilesNextRow, tripleSection } from '../data'

export function HomeScreen() {
  return (
    <AppScreen className="font-figtree">
      <PhoneStatusBar />
      <HomeSearch placeholder={searchPlaceholder} />
      <HomeTabs tabs={homeTabs} activeKey="today" />
      <CategoryRow items={categories} top={169} />
      <PromoBanner {...promo} top={274} />
      <OfferCarousel offers={offers} top={491} />
      <StoreSection {...tripleSection} tiles={storeTiles} nextRow={storeTilesNextRow} top={657} />
      <FloatingTabBar items={navItems} activeKey="home" />
    </AppScreen>
  )
}
