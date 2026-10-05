import { Plus, Search } from 'lucide-react'
import { TabBar } from '../../../ui'
import { BondWordmark } from '../components/BondWordmark'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { CircleIcon } from '../components/NavHeader'
import { CountPill, PromptBar } from '../components/PromptBar'
import { StoryTile } from '../components/StoryTile'
import { bondTabs, home, splash, stories } from '../data'
import { bond } from '../theme'

export function HomeScreen() {
  return (
    <div className="relative h-full font-inter" style={{ background: bond.screen }}>
      <HighlightStatusBar />
      <div className="absolute inset-x-0 flex justify-center" style={{ top: 67 }}>
        <BondWordmark text={splash.brand} size={31} />
      </div>
      <Plus className="absolute text-black" size={31} strokeWidth={1.6} style={{ left: 337.5, top: 65.5 }} />

      <div className="absolute grid grid-cols-3" style={{ left: 23, top: 240, rowGap: 16 }}>
        {stories.map((s) => (
          <StoryTile key={s.id} story={s} />
        ))}
      </div>

      <div className="absolute flex items-center justify-between" style={{ left: 36, right: 38, top: 611, height: 40 }}>
        <span className="text-[20.6px] text-[#2a2a2a]" style={{ letterSpacing: -0.4 }}>
          {home.friendsTitle}
        </span>
        <CircleIcon icon={Search} size={40} iconSize={20} strokeWidth={1.8} />
      </div>

      <PromptBar
        text={home.discoverPlaceholder}
        placeholder
        className="absolute"
        style={{ left: 16.5, width: 359, top: 706.5 }}
        trailing={<CountPill count={home.memoryCount} className="w-[52px] justify-center px-0" />}
      />

      <div className="absolute inset-x-0" style={{ top: 788 }}>
      <TabBar
        items={bondTabs}
        activeKey="home"
        className="justify-center gap-[27px]"
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <Icon
              size={30}
              strokeWidth={1.4}
              fill={active ? '#3a3a3a' : 'none'}
              className={active ? 'text-[#3a3a3a]' : 'text-[#555]'}
            />
          )
        }}
      />
      </div>
    </div>
  )
}
