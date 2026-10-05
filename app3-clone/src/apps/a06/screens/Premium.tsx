import { AppScreen, StatusBar } from '../../../ui'
import { MiniPlayer } from '../components/MiniPlayer'
import { PlanCard, PlanTag } from '../components/PlanCard'
import { SpotifyTabBar } from '../components/SpotifyTabBar'
import { premium } from '../data'
import { sp } from '../theme'

export function Premium() {
  return (
    <AppScreen className="font-figtree" background={sp.bg}>
      <StatusBar color="#fff" />
      <div className="mt-[17px] text-center text-[14.5px] font-bold text-white">{premium.header}</div>
      <h1 className="mt-[25px] px-[16px] text-[21.5px] leading-[28px] font-bold text-white">{premium.title}</h1>
      <div className="mt-[23px] flex flex-col gap-[25px] px-[16px]">
        {premium.plans.map((p) => (
          <PlanCard key={p.key} plan={p} brand={premium.brand} />
        ))}
        <div className="h-[200px] overflow-hidden rounded-[8px]" style={{ background: sp.card }}>
          <PlanTag label={premium.nextTag.label} color={premium.nextTag.color} />
        </div>
      </div>
      <div className="absolute inset-x-[8px] top-[701px] z-30">
        <MiniPlayer title={premium.nowPlaying.title} artist={premium.nowPlaying.artist} progress={premium.nowPlaying.progress} />
      </div>
      <SpotifyTabBar tabs={premium.tabs} active={premium.activeTab} height={110} />
    </AppScreen>
  )
}
