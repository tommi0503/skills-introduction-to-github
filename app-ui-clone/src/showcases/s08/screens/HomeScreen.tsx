import { Bell } from 'lucide-react'
import { ChipGroup, ImagePlaceholder, SearchField } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { Eyebrow } from '../components/Eyebrow'
import { MarketTabBar } from '../components/MarketTabBar'
import { MasonryGrid } from '../components/MasonryGrid'
import { featured, homeCategories, homeProducts } from '../data'
import { theme } from '../theme'

function FeaturedBanner() {
  return (
    <div className="relative h-full w-full overflow-hidden rounded-[10px]">
      <ImagePlaceholder label="mid-century living room" tone="#c9c3b9" className="absolute inset-0" />
      <Eyebrow color="#ffffff" className="absolute top-[78px] left-[18px] text-[9.4px] tracking-[0.24em]">
        {featured.eyebrow}
      </Eyebrow>
      <div className="absolute top-[97px] left-[17px] font-condensed text-[27px] leading-[32.5px] font-medium text-white">
        {featured.title.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <span
        className="absolute top-[128px] right-[19px] flex h-[33px] w-[89px] items-center justify-center rounded-[5px] font-dm text-[13px] font-medium tracking-[0.05em] text-white"
        style={{ background: theme.accent }}
      >
        {featured.cta}
      </span>
    </div>
  )
}

/** MARQET home feed. */
export function HomeScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.bg }}>
      <Box rect={{ x: 16, y: 47, w: 150, h: 36 }} className="font-condensed text-[34px] leading-[36px] font-medium">
        <span className="inline-block origin-left scale-x-[0.76]" style={{ color: theme.ink }}>MARQET</span>
      </Box>
      <Box rect={{ x: 332, y: 53, w: 20, h: 20 }} style={{ color: theme.ink }}>
        <Bell size={20} strokeWidth={1.9} />
        <span className="absolute top-[0px] right-[0px] h-[6px] w-[6px] rounded-full" style={{ background: theme.accent }} />
      </Box>

      <Box rect={{ x: 15, y: 97, w: 346, h: 40 }}>
        <SearchField
          placeholder="Search for vintage, handmade..."
          iconSize={17}
          className="h-full gap-[9px] rounded-full bg-[#f2efe6] px-[15px] text-[#8a857c]"
          textClassName="font-dm text-[13px] leading-[18px] translate-y-[1px]"
        />
      </Box>

      <Box rect={{ x: 15, y: 152.7, w: 400, h: 34 }}>
        <ChipGroup
          items={homeCategories.map((c) => ({ key: c, label: c }))}
          activeKey={homeCategories[0]}
          gap={11}
          className="h-full"
          chipClassName="h-full rounded-full px-[19.5px] font-dm text-[13px] font-medium"
          activeClassName="bg-[#2a1f18] text-white"
          inactiveClassName="bg-[#e9e5da] text-[#2a201a]"
        />
      </Box>

      <Box rect={{ x: 15, y: 208, w: 346, h: 180 }}>
        <FeaturedBanner />
      </Box>

      <Box rect={{ x: 15, y: 418.5, w: 346, h: 340 }}>
        <MasonryGrid columns={homeProducts} gap={15} showSave />
      </Box>

      <MarketTabBar active="home" fillActive />
    </div>
  )
}
