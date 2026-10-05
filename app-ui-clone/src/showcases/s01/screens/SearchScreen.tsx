import { ChipGroup } from '../../../ui'
import { BottomFade } from '../components/BottomFade'
import { ProductTile } from '../components/ProductTile'
import { PromoBanner } from '../components/PromoBanner'
import { SearchHeader } from '../components/SearchHeader'
import { gridProducts, promo, search, styleFilters } from '../data'

/** Rentique search: query field, promo banner, style filters and product grid. */
export function SearchScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white">
      <div className="absolute inset-x-[18px] top-[68px]">
        <SearchHeader placeholder={search.placeholder} />
      </div>
      <div className="absolute inset-x-[18px] top-[127px]">
        <PromoBanner {...promo} />
      </div>
      <ChipGroup
        items={styleFilters}
        activeKey="all"
        gap={7}
        className="absolute left-[18px] top-[287px]"
        chipClassName="h-[31px] rounded-[6px] px-[10px] text-[13px] font-medium"
        activeClassName="bg-[#222] text-white"
        inactiveClassName="bg-[#f4f4f5] text-[#1c1c1c]"
      />
      <div className="absolute left-[18px] top-[337px] grid grid-cols-2 gap-x-[11px] gap-y-[12px]">
        {gridProducts.map((p) => (
          <ProductTile key={p.id} product={p} />
        ))}
      </div>
      <BottomFade height={55} />
    </div>
  )
}
