import { Search } from 'lucide-react'
import { Placed } from '../../../ui'
import { AppStatusBar } from '../components/AppStatusBar'
import { AddFilterRow } from '../components/Chips'
import { CollectionCard } from '../components/CollectionCard'
import { PillNav } from '../components/PillNav'
import { collections, exploreFilters, navItems } from '../data'
import { theme } from '../theme'

/** Phone 3 — explore collections list. */
export function ExploreScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.screen }}>
      <AppStatusBar />

      <Placed x={21} y={61}>
        <h1 className="text-[32px] leading-[40px] font-[550] tracking-[-0.01em]">
          Explore
          <br />
          Collections
        </h1>
      </Placed>
      <Placed x={323} y={67}>
        <div className="flex h-[72px] w-[47px] items-center justify-center rounded-full bg-white text-[#555]">
          <Search size={18} strokeWidth={2} />
        </div>
      </Placed>

      <Placed x={21} y={166}>
        <AddFilterRow labels={exploreFilters} />
      </Placed>

      <Placed x={21} y={231} width={349}>
        <div className="flex flex-col gap-[15px]">
          {collections.map((c) => (
            <CollectionCard key={c.title} collection={c} />
          ))}
        </div>
      </Placed>

      <Placed x={19} y={751}>
        <PillNav items={navItems} activeKey="explore" />
      </Placed>
    </div>
  )
}
