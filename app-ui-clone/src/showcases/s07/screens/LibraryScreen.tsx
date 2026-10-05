import { ListFilter } from 'lucide-react'
import { ChipGroup, SearchField, TabBar } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { DocCard } from '../components/DocCard'
import { MonoTab } from '../components/MonoTab'
import { libraryFilters, libraryTabs, scanDocs } from '../data'
import { theme } from '../theme'

/** Library grid of scanned documents. */
export function LibraryScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.paper }}>
      <Box rect={{ x: 15, y: 44.5, w: 200, h: 34 }} className="font-geist text-[23px] leading-[34px] font-semibold tracking-[-0.02em]">
        <span style={{ color: theme.ink }}>Library</span>
      </Box>
      <Box rect={{ x: 324, y: 45, w: 36, h: 36 }}>
        <div className="flex h-full w-full items-center justify-center rounded-[8px] bg-white" style={{ boxShadow: `0 0 0 1px ${theme.hairline}` }}>
          <ListFilter size={19} strokeWidth={2.2} color={theme.ink} />
        </div>
      </Box>

      <Box rect={{ x: 15, y: 105, w: 345, h: 40 }}>
        <SearchField
          placeholder="Search documents..."
          iconSize={19}
          className="h-full gap-[8px] rounded-[8px] bg-white px-[12px] text-[#6f6e6a] shadow-[0_0_0_1px_#ebe8e2]"
          textClassName="font-inter text-[13.3px] leading-[18px] translate-y-[1px]"
        />
      </Box>

      <Box rect={{ x: 15, y: 160, w: 380, h: 32 }}>
        <ChipGroup
          items={libraryFilters.map((f) => ({ key: f, label: f }))}
          activeKey={libraryFilters[0]}
          className="flex h-full gap-[8px]"
          chipClassName="flex h-full items-center rounded-[7px] px-[16px] font-inter text-[13.5px] font-[550] whitespace-nowrap"
          activeClassName="bg-[#151515] text-white"
          inactiveClassName="bg-white text-[#1b1b1b] shadow-[0_0_0_1px_#e7e4dd]"
        />
      </Box>
      <Box rect={{ x: 0, y: 210, w: 375, h: 1 }} style={{ background: theme.hairline }} />

      <Box rect={{ x: 14, y: 226, w: 346, h: 600 }} className="grid grid-cols-2 gap-x-[16px] gap-y-[16px]" style={{ gridAutoRows: 'min-content' }}>
        {scanDocs.map((d) => (
          <DocCard key={d.id} doc={d} imageHeight={d.title ? 218 : 230} height={d.title ? 295 : 260} />
        ))}
      </Box>

      <Box rect={{ x: 0, y: 744, w: 375, h: 100 }} className="border-t" style={{ background: theme.paper, borderColor: theme.hairline }}>
        <TabBar
          items={libraryTabs.map((t) => ({ key: t.key, icon: t.icon, label: t.label }))}
          activeKey="library"
          className="pr-[2px] pl-[12px] pt-[15px]"
          renderItem={(item, active) => (
            <MonoTab
              icon={item.icon!}
              label={String(item.label)}
              color={active ? theme.ink : '#8f8d89'}
              gap={10}
              marker={active ? theme.accent : undefined}
            />
          )}
        />
      </Box>
    </div>
  )
}
