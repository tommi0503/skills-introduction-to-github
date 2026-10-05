import { CircleUserRound, Search } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { BrandMark } from '../components/BrandMark'
import { Chrome } from '../components/Chrome'
import { CircleButton } from '../components/CircleButton'
import { CollectionCard } from '../components/CollectionCard'
import { FilterChips } from '../components/FilterChips'
import { FloatingTabBar } from '../components/FloatingTabBar'
import { MiniBookCard } from '../components/MiniBookCard'
import { UploadTile } from '../components/UploadTile'
import { home } from '../data'

export function HomeScreen() {
  return (
    <AppScreen>
      <Chrome chipClassName="bg-[#a9a9ab]/95!" />
      <div className="absolute inset-x-0 top-[66px] pl-[18px]">
        <div className="flex h-[40px] items-center pr-[24px]">
          <BrandMark size={24} />
          <h1 className="ml-[8px] flex-1 text-[31px] font-medium tracking-[-0.4px] text-[#111]">{home.title}</h1>
          <CircleButton icon={Search} className="mr-[12px]" iconSize={18} />
          <CircleButton icon={CircleUserRound} iconSize={20} />
        </div>
        <div className="mt-[25px]" />
        <FilterChips items={home.filters} activeKey={home.activeFilter} />
        <h2 className="mt-[24px] text-[19px] font-medium text-[#111]">{home.uploadTitle}</h2>
        <div className="mt-[15px] flex gap-[12px]">
          {home.uploads.map((u) => (
            <UploadTile key={u.key} item={u} />
          ))}
        </div>
        <h2 className="mt-[34px] text-[19px] font-medium text-[#111]">{home.collectionsTitle}</h2>
        <div className="mt-[14px] flex gap-[12px]">
          {home.collections.map((c) => (
            <CollectionCard key={c.key} item={c} />
          ))}
        </div>
        <div className="mt-[30px] grid w-[345px] grid-cols-2 gap-x-[8px] gap-y-[10px] pl-[4px]">
          {home.mini.map((b) => (
            <MiniBookCard key={b.key} book={b} />
          ))}
        </div>
      </div>
      <FloatingTabBar items={home.tabs} activeKey={home.activeTab} className="absolute bottom-[18px] left-[19px] w-[348px]" />
    </AppScreen>
  )
}
