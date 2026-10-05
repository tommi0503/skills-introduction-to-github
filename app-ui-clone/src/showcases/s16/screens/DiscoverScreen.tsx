import { ChipGroup, ImagePlaceholder } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { NavHeader } from '../components/NavHeader'
import { PromoBanner } from '../components/PromoBanner'
import { StatusChip } from '../components/StatusChip'
import { StoreCard } from '../components/StoreCard'
import { discoverScreen as d } from '../data'
import { navItems } from '../nav'
import { theme } from '../theme'

export function DiscoverScreen() {
  return (
    <div className="absolute inset-0" style={{ color: theme.ink }}>
      <div className="absolute top-[50px] right-0 left-0">
        <NavHeader title={d.title} />
      </div>
      <div className="absolute top-[101px] left-[15px] text-[23.5px] font-[450] tracking-[-0.5px]">{d.heading}</div>

      <div className="absolute top-[151px] right-0 left-0">
        <PromoBanner {...d.promo} />
      </div>

      <div className="absolute top-[346px] left-[15px] text-[17.5px] tracking-[-0.2px]">{d.categoriesTitle}</div>
      <ChipGroup
        items={d.categories}
        activeKey={d.activeCategory}
        className="absolute top-[382px] left-[15px]"
        gap={5}
        chipClassName="h-[40px] rounded-full px-[22px] text-[13px]"
        activeClassName="bg-[#1f1f1f] text-white"
        inactiveClassName="bg-white text-[#444]"
      />

      <div className="absolute top-[439px] left-[16px] text-[17.5px] tracking-[-0.2px]">{d.storesTitle}</div>
      <div className="absolute top-[475px] right-[15px] left-[16px] grid grid-cols-2 gap-x-[8px] gap-y-[11px]">
        {d.stores.map((s) => (
          <StoreCard key={s.key} store={s} />
        ))}
      </div>

      <div className="absolute top-[757px] left-[16px] text-[19px]">{d.trendingTitle}</div>
      <div className="absolute top-[790px] right-[15px] left-[16px] flex h-[80px] items-start rounded-[18px] bg-white pt-[12px] pr-[11px] pl-[13px]">
        <ImagePlaceholder className="h-[50px] w-[50px] rounded-full" label="product" />
        <div className="ml-[5px] flex-1 pt-[3px]">
          <div className="text-[16px] leading-[20px]">{d.trending.title}</div>
          <div className="mt-[2px] text-[12px]" style={{ color: theme.muted }}>
            {d.trending.subtitle}
          </div>
        </div>
        <StatusChip label={d.trending.status} tone="grey" className="mt-[6px] h-[28px] bg-[#f6f6f6]! px-[12px] text-[10.5px]! text-[#8a8a8a]!" />
      </div>

      <BottomNav items={navItems} activeKey="discover" />
    </div>
  )
}
