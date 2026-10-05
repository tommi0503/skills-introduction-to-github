import { ArrowLeft } from 'lucide-react'
import { Box } from '../../shared-canvas/Box'
import { CropFrame } from '../components/CropFrame'
import { FilterThumb } from '../components/FilterThumb'
import { MonoTab } from '../components/MonoTab'
import { editActions, filterPresets } from '../data'
import { theme } from '../theme'

/** Review & crop step after capture. */
export function ReviewScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.paper }}>
      <Box rect={{ x: 0, y: 0, w: 375, h: 97 }} className="border-b" style={{ borderColor: '#e2ded6' }}>
        <ArrowLeft size={22} strokeWidth={2.1} className="absolute top-[52px] left-[21px]" color={theme.ink} />
        <span
          className="absolute top-[51.5px] left-[120px] font-plexmono text-[13px] leading-[22px] font-semibold tracking-[0.1em] whitespace-nowrap"
          style={{ color: theme.ink }}
        >
          REVIEW &amp; CROP
        </span>
        <span className="absolute top-[51px] right-[22px] font-inter text-[14px] leading-[22px] font-medium" style={{ color: theme.accent }}>
          DONE
        </span>
      </Box>

      <Box rect={{ x: 0, y: 97, w: 375, h: 523 }} style={{ background: theme.canvas }} />
      <Box rect={{ x: 47, y: 172, w: 279, h: 372 }}>
        <CropFrame />
      </Box>

      <Box rect={{ x: 21, y: 643, w: 300, h: 90 }} className="flex gap-[15px]">
        {filterPresets.map((f, i) => (
          <FilterThumb key={f.key} label={f.label} selected={i === 0} size={60} />
        ))}
      </Box>

      <Box rect={{ x: 24, y: 755, w: 328, h: 50 }} className="flex">
        {editActions.map((a) => (
          <MonoTab key={a.key} icon={a.icon} label={a.label} color={a.destructive ? theme.danger : theme.ink} gap={8} iconSize={22} labelClassName="tracking-[0.06em]" />
        ))}
      </Box>
    </div>
  )
}
