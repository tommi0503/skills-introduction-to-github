import { BackTitleHeader, NaverStatusBar, WebToolbar } from '../../shared-naver'
import { FilterChips } from '../components/FilterChips'
import { StoreListItem } from '../components/StoreListItem'
import { storeChips, stores } from '../data'

export function StoreMethodsScreen() {
  return (
    <>
      <NaverStatusBar time="1:31" charging />
      <BackTitleHeader title="매장별 결제 방법" centerY={86} arrowSize={26} arrowLeft={18.5} />
      <div
        className="absolute flex items-center"
        style={{ left: 19.5, right: 19.5, top: 124, height: 47, background: '#f7f8fa', borderRadius: 4 }}
      >
        <span
          className="flex items-center justify-center font-inter font-bold text-white"
          style={{ marginLeft: 14.5, width: 28, height: 19.5, borderRadius: 4, background: '#00ac54', fontSize: 12.5 }}
        >
          TIP
        </span>
        <span style={{ marginLeft: 10, fontSize: 14.5, color: '#212224', letterSpacing: -0.4 }}>
          화면을 최대한 밝게 하고 가까이 스캔해주세요.
        </span>
      </div>
      <FilterChips className="absolute" items={storeChips} active={0} widths={[52, 64, 54, 81, 60]} style={{ left: 19.6, top: 192 }} />
      <div className="absolute" style={{ left: 0, right: 0, top: 249.5 }}>
        {stores.map((s) => (
          <StoreListItem key={s.name} store={s} />
        ))}
      </div>
      <WebToolbar />
    </>
  )
}
