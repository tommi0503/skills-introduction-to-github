import { Bell } from 'lucide-react'
import { SearchField } from '../../../ui'
import { AskAiCard } from '../components/AskAiCard'
import { FoodTabBar } from '../components/TabBar'
import { TopBar } from '../components/TopBar'
import { TrendingCard } from '../components/TrendingCard'
import { exploreScreen as d } from '../data'
import { theme } from '../theme'

export function ExploreScreen() {
  return (
    <div className="absolute inset-0">
      <TopBar title={d.title} action={Bell} />
      <SearchField
        placeholder={d.search}
        iconSize={20}
        iconStrokeWidth={2}
        className="absolute top-[146px] right-[15.5px] left-[16px] h-[53px] gap-[10px] rounded-full bg-[#f3f3f5] pl-[15px] text-[#444]"
        textClassName="text-[12.5px] text-[#9a9aa2]"
      />
      <div className="absolute top-[222px] left-[15px] font-condensed text-[17.2px] font-bold text-[#111]">{d.askTitle}</div>
      <div className="absolute top-[262px] right-[15.5px] left-[16px]">
        <AskAiCard thumbs={d.askThumbs} text={d.askText} placeholder={d.askPlaceholder} />
      </div>

      <div className="absolute top-[537px] right-[15.5px] left-[16px] flex items-center justify-between">
        <span className="font-condensed text-[17px] font-bold text-[#111]">{d.trendingTitle}</span>
        <span className="text-[13.5px]" style={{ color: theme.muted }}>
          {d.trendingAction}
        </span>
      </div>
      <div className="absolute top-[578px] left-[17px] flex gap-[9px]">
        {d.trending.map((t) => (
          <TrendingCard key={t.key} item={t} />
        ))}
      </div>

      <div className="absolute right-0 bottom-0 left-0 h-[100px]" style={{ background: 'linear-gradient(180deg, rgba(255,255,255,0), #fff 14%)' }} />
      <FoodTabBar activeKey="explore" top={749} />
    </div>
  )
}
