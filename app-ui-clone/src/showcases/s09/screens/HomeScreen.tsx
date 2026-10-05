import { HomeIndicator, ImagePlaceholder, SearchField } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { DarkButton } from '../components/DarkButton'
import { DarkHeader } from '../components/DarkHeader'
import { DishCard } from '../components/DishCard'
import { QuickActionList } from '../components/QuickActionList'
import { SectionTitle } from '../components/SectionTitle'
import { TagChip } from '../components/TagChip'
import { cartCount, categories, quickActions, recommended } from '../data'
import { theme } from '../theme'

/** Home: brand header with search, shortcuts, categories and recommendations. */
export function HomeScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.canvas }}>
      <DarkHeader height={179} cartCount={cartCount}>
        <Box rect={{ x: 23, y: 118, w: 331, h: 40 }}>
          <SearchField
            placeholder="Search for something tasty..."
            iconSize={20}
            className="h-full gap-[9px] rounded-[10px] bg-[#454545] px-[12px] text-[#9d9d9d]"
            textClassName="font-poppins text-[13.5px]"
          />
        </Box>
      </DarkHeader>
      <Box rect={{ x: 0, y: 150, w: 375, h: 178 }} className="rounded-b-[22px] bg-white" />
      <Box rect={{ x: 23, y: 192, w: 331, h: 130 }}>
        <QuickActionList items={quickActions} rowHeight={43} />
      </Box>

      <Box rect={{ x: 23, y: 353, w: 332, h: 22 }}>
        <SectionTitle title="Top Categories" />
      </Box>
      <Box rect={{ x: 23, y: 394.6, w: 360, h: 40 }} className="flex gap-[14.5px]">
        {categories.map((c) => (
          <TagChip key={c.key} tag={c} className="bg-white" />
        ))}
      </Box>

      <Box rect={{ x: 23, y: 470.5, w: 332, h: 22 }}>
        <SectionTitle title="Recommended for you" />
      </Box>
      <Box rect={{ x: 23, y: 509, w: 331, h: 420 }} className="grid grid-cols-2 gap-x-[15px] gap-y-[15px]">
        {recommended.map((d) => (
          <DishCard key={d.key} dish={d} />
        ))}
        {recommended.map((d) => (
          <div key={`${d.key}-more`} className="relative h-[200px] overflow-hidden rounded-[13px] bg-white">
            <ImagePlaceholder label="dish" className="absolute top-[14px] left-1/2 h-[122px] w-[122px] -translate-x-1/2 rounded-full" />
          </div>
        ))}
      </Box>

      <Box rect={{ x: 38.5, y: 728, w: 299, h: 43 }}>
        <DarkButton className="justify-center">Check out 2 products</DarkButton>
      </Box>
      <HomeIndicator width={116} bottom={6} />
    </div>
  )
}
