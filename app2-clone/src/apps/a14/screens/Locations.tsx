import { ChevronDown, ChevronLeft, ListFilter } from 'lucide-react'
import { AppScreen, ChipGroup } from '../../../ui'
import { Flag } from '../components/Flag'
import { NavBar } from '../components/NavBar'
import { SearchPill } from '../components/SearchPill'
import { StatusRow } from '../components/StatusRow'
import { locations as d, navTabs, type Country } from '../data'
import { nord } from '../theme'

function CountryRow({ c }: { c: Country }) {
  return (
    <div className="mx-[15px] flex h-[69.5px] items-center border-b border-[#ebebed] pr-[13px]">
      <Flag size={24} label={c.name} />
      <div className="ml-[12px] flex-1">
        <div className="text-[14px] leading-[18px] font-semibold text-[#333]">{c.name}</div>
        <div className="mt-[3px] text-[12px] leading-[16px] text-[#8a8a8f]">{c.sub}</div>
      </div>
      {c.expandable && <ChevronDown size={20} strokeWidth={1.5} className="text-[#444]" />}
    </div>
  )
}

export function Locations() {
  return (
    <AppScreen className="font-inter" background={nord.bgList} style={{ color: nord.ink }}>
      <StatusRow />
      <ChevronLeft size={28} strokeWidth={1.3} className="absolute top-[76px] left-[12px] text-[#444]" />
      <SearchPill label={d.search} className="top-[67px] left-[49px] w-[323px] pl-[20px]" />
      <ChipGroup
        items={d.tabs}
        activeKey={d.activeTab}
        className="absolute top-[129px] left-[22px]"
        chipClassName="h-[37px] rounded-full border px-[15px] text-[13.5px]"
        activeClassName="border-[1.5px] border-[#5a6ce8] bg-white font-semibold px-[16px]"
        inactiveClassName="border-[#d2d2d6] text-[#333]"
      />
      <div className="absolute top-[194px] left-[30px] text-[13.5px] text-[#77777b]">{d.sectionTitle}</div>
      <ListFilter size={18} strokeWidth={1.4} className="absolute top-[195px] left-[330px] text-[#77777b]" />
      <div className="absolute top-[226px] left-[15px] h-[600px] w-[357px] rounded-[16px] bg-white pt-[0px]">
        {d.countries.map((c) => (
          <CountryRow key={c.key} c={c} />
        ))}
      </div>
      <NavBar tabs={navTabs} activeKey="globe" top={763} className="border-t-0 bg-[#f6f6f7]" />
    </AppScreen>
  )
}
