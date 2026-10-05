import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { SearchBar } from '../components/SearchBar'
import { StoreSection } from '../components/StoreSection'
import { activeTab, searchPlaceholder, stores } from '../data'
import { theme } from '../theme'

export function CartScreen() {
  return (
    <AppScreen className="font-inter">
      <StatusBar paddingTop={18} paddingX={54} fontSize={17} className="!pr-[35px]" />
      <SearchBar placeholder={searchPlaceholder} className="absolute top-[62px] right-[20px] left-[20px]" />
      <div className="absolute inset-x-0 top-[137px]">
        {stores.map((s, i) => (
          <div key={s.id}>
            {i > 0 && <div className="my-[25px] h-[3px]" style={{ background: theme.divider }} />}
            <StoreSection store={s} />
          </div>
        ))}
      </div>
      <BottomNav active={activeTab} />
      <HomeIndicator bottom={4} width={138} />
    </AppScreen>
  )
}
