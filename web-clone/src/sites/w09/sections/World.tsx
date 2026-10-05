import { Search } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Box } from '../components/Box'
import { Lines } from '../components/Lines'
import { SectionTitle } from '../components/SectionTitle'
import { worldSection as s } from '../data'
import { theme } from '../theme'

/** "Every search opens a new world." — sage panel with three photos and a floating search pill. */
export function World() {
  return (
    <>
      <div className="absolute left-0 top-[1020px] flex justify-center" style={{ width: theme.contentWidth }}>
        <SectionTitle text={s.title} lineHeight={71.28} />
      </div>
      <Box rect={s.panel} className="rounded-[12px]" style={{ background: theme.color.panel }} />
      {s.images.map((r, i) => (
        <Box key={i} rect={r}>
          <ImagePlaceholder className="h-full w-full" />
        </Box>
      ))}
      <Box
        rect={s.search}
        className="flex items-center rounded-full pl-[21px] text-[16px] font-medium text-white"
        style={{ background: theme.color.searchPill, letterSpacing: '-0.32px' }}
      >
        <Search size={16} strokeWidth={2} />
        <span className="ml-[10px]">{s.query}</span>
      </Box>
      <div className="absolute left-0 top-[1625px] flex justify-center" style={{ width: theme.contentWidth }}>
        <Lines lines={s.caption} className="text-center text-[26px] leading-[31.2px]" style={{ color: theme.color.muted }} />
      </div>
    </>
  )
}
