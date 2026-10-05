import { Search } from 'lucide-react'
import { Avatar, Placed } from '../../../ui'
import { AppStatusBar } from '../components/AppStatusBar'
import { ChipRow } from '../components/Chips'
import { PillNav } from '../components/PillNav'
import { ProductCard } from '../components/ProductCard'
import { homeCategories, navItems, potatoChips, user } from '../data'
import { featuredCard } from '../metrics'
import { theme } from '../theme'

/** Phone 2 — home feed with greeting, search, categories and featured card. */
export function HomeScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.screen }}>
      <AppStatusBar />

      <Placed x={20} y={60}>
        <div className="text-[21px] leading-[28px] font-bold">{user.greeting}</div>
        <div className="mt-[2px] text-[13.5px] text-[#777]">{user.subtitle}</div>
      </Placed>
      <Placed x={321} y={62}>
        <Avatar size={48} ring="3px solid #fff" />
      </Placed>

      <Placed x={20} y={132} width={350}>
        <div className="flex h-[52px] items-center gap-[8px] rounded-full bg-white px-[15px] text-[#8a8a8a]">
          <Search size={19} strokeWidth={2} className="text-[#555]" />
          <span className="text-[14.5px]">Search</span>
        </div>
      </Placed>

      <Placed x={20} y={202}>
        <ChipRow labels={homeCategories} active="Chips" />
      </Placed>

      <Placed x={20} y={274} width={350}>
        <div className="flex items-center justify-between">
          <span className="text-[17px] font-bold">Chips Collections</span>
          <span className="text-[13.5px] text-[#777]">See all</span>
        </div>
      </Placed>

      <Placed x={20} y={314}>
        <ProductCard
          product={potatoChips}
          metrics={featuredCard}
          stack={[
            { color: '#fdeba6', offset: 15, inset: 7 },
            { color: '#fef4cd', offset: 34, inset: 15 },
          ]}
        />
      </Placed>

      <Placed x={19} y={752}>
        <PillNav items={navItems} activeKey="home" />
      </Placed>
    </div>
  )
}
