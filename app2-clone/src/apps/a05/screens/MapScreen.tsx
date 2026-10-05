import { Bell, Navigation, UserRoundPlus } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { categories, mapDots, mapFilters, mapPins, navItems } from '../data'
import { theme } from '../theme'
import { BottomNav } from '../components/BottomNav'
import { CategoryRail } from '../components/CategoryRail'
import { Chrome } from '../components/Chrome'
import { FilterChip } from '../components/FilterChip'
import { Floating } from '../components/Floating'
import { MapBackdrop } from '../components/MapBackdrop'
import { MapPin } from '../components/MapPin'

export function MapScreen() {
  return (
    <AppScreen className="font-archivo">
      <MapBackdrop />
      {mapDots.map(([x, y]) => (
        <span key={`${x}-${y}`} className="absolute h-[7px] w-[7px] rounded-full" style={{ left: x - 3.5, top: y - 3.5, background: theme.orange }} />
      ))}
      {mapPins.map((p) => (
        <MapPin key={p.key} pin={p} />
      ))}
      <div className="absolute inset-x-0 bottom-0 h-[180px]" style={{ background: 'linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.75) 45%, rgba(255,255,255,.85))' }} />
      <Chrome />
      <Floating className="absolute left-[19px] top-[58px] h-[44px] w-[44px]">
        <UserRoundPlus size={22} strokeWidth={1.6} />
      </Floating>
      <Floating className="absolute left-[280px] top-[58px] h-[44px] w-[95px] gap-[20px]">
        <Navigation size={21} strokeWidth={1.6} />
        <Bell size={21} strokeWidth={1.6} />
      </Floating>
      <Floating className="absolute left-[334px] top-[643px] h-[44px] w-[44px]">
        <Navigation size={20} fill="#000" strokeWidth={1.5} />
      </Floating>
      <div className="absolute left-[16px] top-[661px] flex gap-[12px]">
        {mapFilters.map((f) => (
          <FilterChip key={f.key} label={f.label} leading={f.leading} trailing={f.trailing} />
        ))}
      </div>
      <CategoryRail items={categories} className="absolute left-[13px] top-[697px]" />
      <BottomNav items={navItems} activeKey="map" />
    </AppScreen>
  )
}
