import { Search, SlidersHorizontal } from 'lucide-react'
import { AppScreen, SearchField } from '../../../ui'
import { BottomFade } from '../components/BottomFade'
import { DeviceChrome } from '../components/DeviceChrome'
import { FilterChips } from '../components/FilterChips'
import { FloatingNav } from '../components/FloatingNav'
import { NoteCard } from '../components/NoteCard'
import { PageHeader } from '../components/PageHeader'
import { navItems, noteFilters, notes, notesHeader, searchPlaceholder } from '../data'
import { nd } from '../theme'

/** Notes & Docs: search, filters and a 2-column card grid. */
export function NotesScreen() {
  return (
    <AppScreen background={nd.bg} className="font-poppins" style={{ color: nd.text }}>
      <DeviceChrome />
      <PageHeader {...notesHeader} />
      <SearchField
        icon={Search}
        iconSize={18}
        iconStrokeWidth={1.5}
        placeholder={searchPlaceholder}
        className="absolute top-[126px] right-[19px] left-[18px] h-[50px] rounded-full bg-white pr-[5px] pl-[18px] text-[#555]"
        textClassName="text-[10px] text-[#b4b6ba]"
        trailing={
          <span className="flex h-[40px] w-[91px] items-center justify-center gap-[10px] rounded-full text-[12.5px] text-white" style={{ background: nd.navy }}>
            Filter
            <SlidersHorizontal size={15} strokeWidth={1.6} />
          </span>
        }
      />
      <FilterChips labels={noteFilters} active={noteFilters[0]} top={191} />
      <div className="absolute top-[248px] right-[20px] left-[20px] grid grid-cols-2 gap-x-[10px] gap-y-[11px]">
        {notes.map((n) => (
          <NoteCard key={n.key} note={n} />
        ))}
      </div>
      <BottomFade />
      <FloatingNav items={navItems} activeKey="search" activeLabel="Search" />
    </AppScreen>
  )
}
