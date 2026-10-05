import { Plus, Search } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { favorites, myWork } from '../data'
import { gh } from '../theme'
import { GhStatusBar } from '../components/GhStatusBar'
import { HaloButton } from '../components/Halo'
import { GroupCard } from '../components/GroupCard'
import { ListRow } from '../components/ListRow'
import { SectionTitle } from '../components/SectionTitle'
import { FloatingTabBar } from '../components/FloatingTabBar'

export function HomeScreen() {
  return (
    <AppScreen background={gh.canvas}>
      <GhStatusBar />
      <ImagePlaceholder label="avatar" className="absolute top-[62px] left-[22px] h-[38px] w-[38px] rounded-full" />
      <div className="absolute top-[58px] right-[17px] flex gap-[12px]">
        <HaloButton icon={Plus} iconSize={24} />
        <HaloButton icon={Search} iconSize={22} />
      </div>
      <SectionTitle title="My Work" className="absolute inset-x-0 top-[124px]" />
      <GroupCard className="absolute top-[158px] left-[17px] w-[355px]">
        {myWork.map((w) => (
          <ListRow
            key={w.key}
            height={56.7}
            leading={
              <span className="flex h-[31px] w-[31px] items-center justify-center rounded-[7px] text-white" style={{ background: w.color }}>
                <w.icon size={17} strokeWidth={2.2} fill={w.filled ? 'currentColor' : 'none'} />
              </span>
            }
          >
            <span className="text-[16px] text-[#1f2328]">{w.label}</span>
          </ListRow>
        ))}
      </GroupCard>
      <SectionTitle title="Favorites" className="absolute inset-x-0 top-[587px]" />
      <GroupCard className="absolute top-[622px] left-[17px] w-[355px]">
        {favorites.map((r) => (
          <ListRow key={r.name} height={63} leading={<ImagePlaceholder label="avatar" className="h-[30px] w-[30px] rounded-full" />}>
            <div className="text-[13px] leading-[16px] text-[#6b7079]">{r.owner}</div>
            <div className="text-[16px] leading-[21px] font-medium text-[#1f2328]">{r.name}</div>
          </ListRow>
        ))}
      </GroupCard>
      <FloatingTabBar />
    </AppScreen>
  )
}
