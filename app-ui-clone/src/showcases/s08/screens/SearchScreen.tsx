import { ChevronDown, ChevronLeft, CircleX } from 'lucide-react'
import { ChipGroup, SearchField } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { MarketTabBar } from '../components/MarketTabBar'
import { MasonryGrid } from '../components/MasonryGrid'
import { resultCount, searchFilters, searchProducts, searchQuery } from '../data'
import { theme } from '../theme'

/** Search results for a query, with dropdown filters. */
export function SearchScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.bg }}>
      <Box rect={{ x: 16, y: 55, w: 20, h: 20 }} style={{ color: theme.ink }}>
        <ChevronLeft size={20} strokeWidth={2} />
      </Box>
      <Box rect={{ x: 49, y: 44.5, w: 311, h: 40 }}>
        <SearchField
          value={searchQuery}
          iconSize={19}
          className="h-full gap-[8px] rounded-full bg-[#f2efe6] pr-[13px] pl-[12px] text-[#2a201a]"
          textClassName="font-dm text-[14px]"
          trailing={<CircleX size={17} strokeWidth={1.8} />}
        />
      </Box>

      <Box rect={{ x: 14, y: 100, w: 400, h: 35.5 }}>
        <ChipGroup
          items={searchFilters.map((f) => ({
            key: f,
            label: (
              <>
                {f}
                <ChevronDown size={12} strokeWidth={2} className="ml-[6px]" />
              </>
            ),
          }))}
          gap={8.5}
          className="h-full"
          chipClassName="h-full rounded-[7px] border px-[15px] font-dm text-[13px]"
          inactiveClassName="border-[#e7e3d8] bg-[#f2efe6] text-[#2a201a]"
        />
      </Box>

      <Box rect={{ x: 14, y: 165, w: 300, h: 15 }} className="font-dm text-[10.5px] leading-[15px] tracking-[0.12em]">
        <span style={{ color: '#7d776e' }}>{resultCount}</span>
      </Box>

      <Box rect={{ x: 14, y: 195.8, w: 346, h: 600 }}>
        <MasonryGrid columns={searchProducts} gap={15} />
      </Box>

      <MarketTabBar active="search" />
    </div>
  )
}
