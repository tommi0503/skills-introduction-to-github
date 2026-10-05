import { Bell, MapPin, Plus, ScanFace } from 'lucide-react'
import { ChipGroup, SearchField } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { CircleIconButton, CountBadge } from '../components/CircleIconButton'
import { FeaturedShipmentCard } from '../components/FeaturedShipmentCard'
import { SectionHeader } from '../components/SectionHeader'
import { ShipmentListItem } from '../components/ShipmentListItem'
import { locationScreen as d } from '../data'
import { navItems } from '../nav'
import { theme } from '../theme'

export function LocationScreen() {
  return (
    <div className="absolute inset-0" style={{ color: theme.ink }}>
      {/* Header */}
      <div className="absolute top-[61px] left-[16px]">
        <div className="text-[24.5px] leading-[28px] font-medium tracking-[-0.5px]">{d.title}</div>
        <div className="mt-[3px] flex items-center gap-[3px] text-[13px]" style={{ color: theme.muted }}>
          <MapPin size={15} strokeWidth={1.6} />
          {d.place}
        </div>
      </div>
      <div className="absolute top-[60px] right-[15px] flex gap-[6px]">
        <CircleIconButton icon={Plus} size={50} iconSize={22} className="border border-[#e2e2e2]" />
        <CircleIconButton
          icon={Bell}
          size={50}
          iconSize={21}
          className="border border-[#e2e2e2]"
          badge={<CountBadge count={d.notifications} color={theme.orange} size={16} top={1} right={1} />}
        />
      </div>

      {/* Search */}
      <div className="absolute top-[126px] right-[14px] left-[16px] flex items-center gap-[8px]">
        <SearchField
          placeholder={d.search}
          iconSize={21}
          iconStrokeWidth={1.6}
          className="h-[54px] flex-1 gap-[9px] rounded-full bg-white pl-[19px] text-[#9a9a9a]"
          textClassName="text-[13px] text-[#b4b4b4]"
        />
        <CircleIconButton icon={ScanFace} size={55} iconSize={24} strokeWidth={1.7} className="bg-[#232323] text-white" />
      </div>

      {/* Segments */}
      <div className="absolute top-[200px] left-[16px] h-[46px] w-[359px] rounded-full bg-white p-[3px]">
        <ChipGroup
          items={d.segments}
          activeKey={d.activeSegment}
          className="h-full"
          gap={0}
          chipClassName="h-full rounded-full text-[13px] tracking-[-0.1px]"
          activeClassName="mr-[3px] w-[97px] bg-[#232323] text-white"
          inactiveClassName="px-[19.5px] text-[#3a3a3a]"
        />
      </div>

      <SectionHeader title={d.sectionTitle} action={d.sectionAction} className="absolute top-[264px] right-[16px] left-[16px]" />

      <div className="absolute top-[299px] right-0 left-0">
        <FeaturedShipmentCard data={d.featured} />
      </div>

      {/* Sheet */}
      <div
        className="absolute top-[503px] right-[16px] bottom-[24px] left-[16px] rounded-[22px] bg-white px-[16px]"
        style={{ boxShadow: '0 -4px 16px rgba(0,0,0,0.04)' }}
      >
        <div className="mx-auto mt-[13px] h-[5px] w-[46px] rounded-full bg-[#cfcfcf]" />
        <SectionHeader title={d.sectionTitle} action={d.sectionAction} className="mt-[14px]" />
        <div className="mt-[13px] flex flex-col gap-[11px]">
          {d.rows.map((r) => (
            <ShipmentListItem key={r.id} row={r} />
          ))}
        </div>
      </div>

      <BottomNav items={navItems} activeKey="home" />
    </div>
  )
}
