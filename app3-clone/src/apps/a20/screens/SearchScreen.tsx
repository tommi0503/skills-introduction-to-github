import { AppScreen, HomeIndicator, ImagePlaceholder, cn } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { ProductCard } from '../components/ProductCard'
import { SearchHeader } from '../components/SearchHeader'
import { activeAge, ages, brands, recent, rising, suggested, type Trend } from '../data'
import { theme } from '../theme'

function SectionLabel({ children, top, right }: { children: string; top: number; right?: string }) {
  return (
    <div className="absolute left-[17px] flex w-[356px] justify-between text-[12.5px]" style={{ top }}>
      <span className="text-[#b0b0b4]">{children}</span>
      {right && <span className="text-[#c4c4c8]">{right}</span>}
    </div>
  )
}

function TrendMark({ trend }: { trend: Trend }) {
  if (trend === 'same') return <span className="h-px w-[7px] bg-[#c4c4c8]" />
  return (
    <span
      className="h-0 w-0 border-x-[3.5px] border-x-transparent"
      style={trend === 'up' ? { borderBottom: `5px solid ${theme.up}` } : { borderTop: `5px solid ${theme.down}` }}
    />
  )
}

export function SearchScreen() {
  const cols = [rising.slice(0, 3), rising.slice(3)]
  return (
    <AppScreen className="font-pretendard">
      <PhoneStatus />
      <SearchHeader placeholder="애니바디 라방 ~39%" />
      <SectionLabel top={111}>추천 검색어</SectionLabel>
      <div className="absolute top-[145px] left-[15px] flex gap-[8px]">
        {suggested.map((s) => (
          <span key={s} className="flex h-[30px] items-center rounded-full px-[12px] text-[13px] font-semibold whitespace-nowrap text-[#222]" style={{ background: theme.chip }}>
            {s}
          </span>
        ))}
      </div>
      <SectionLabel top={195}>뷰티 인기 브랜드</SectionLabel>
      <div className="absolute top-[232px] left-[17px] flex gap-[15px]">
        {brands.map((b, i) => (
          <div key={b} className="flex w-[62px] flex-col items-center">
            <div className="flex h-[62px] w-[62px] items-center justify-center rounded-full border border-[#f0f0f2] bg-white">
              {i === 3 ? (
                <ImagePlaceholder label={b} className="h-[62px] w-[62px] rounded-full" />
              ) : (
                <ImagePlaceholder label={`${b} logo`} className="h-[14px] w-[50px] rounded-[2px]" />
              )}
            </div>
            <span className="mt-[9px] text-[12.5px] font-medium whitespace-nowrap text-[#222]">{b}</span>
          </div>
        ))}
      </div>
      <SectionLabel top={340} right="오후 5:00 업데이트">급상승 검색어</SectionLabel>
      <div className="absolute top-[374px] left-[-44px] flex gap-[6px]">
        {ages.map((a) => (
          <span
            key={a}
            className={cn(
              'flex h-[31px] items-center rounded-full px-[13px] text-[12.5px] whitespace-nowrap',
              a === activeAge ? 'bg-[#222] font-semibold text-white' : 'border border-[#e6e6e8] text-[#a5a5aa]',
            )}
          >
            {a}
          </span>
        ))}
      </div>
      <div className="absolute top-[420px] left-[17px] flex gap-[39px]">
        {cols.map((col, i) => (
          <div key={i} className="flex w-[157px] flex-col">
            {col.map((r) => (
              <div key={r.rank} className="flex h-[40px] items-center text-[13.5px] font-semibold text-[#111]">
                <span className="w-[30px]">{r.rank}</span>
                <span className="flex-1">{r.keyword}</span>
                <TrendMark trend={r.trend} />
              </div>
            ))}
          </div>
        ))}
      </div>
      <div className="absolute top-[550px] left-[177px] flex gap-[8px]">
        {[0, 1, 2].map((d) => (
          <span key={d} className={cn('h-[6px] w-[6px] rounded-full', d === 0 ? 'bg-[#222]' : 'bg-[#e4e4e6]')} />
        ))}
      </div>
      <SectionLabel top={588}>최근 본 상품</SectionLabel>
      <div className="absolute top-[614px] left-[15px] flex gap-[2px]">
        {recent.map((p) => (
          <ProductCard key={p.key} product={p} width={113} imageHeight={135} />
        ))}
      </div>
      <HomeIndicator width={140} bottom={6} />
    </AppScreen>
  )
}
