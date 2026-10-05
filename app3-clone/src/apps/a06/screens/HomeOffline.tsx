import { AppScreen, Avatar, ImagePlaceholder, StatusBar } from '../../../ui'
import { Chip } from '../components/Chip'
import { MediaCard } from '../components/MediaCard'
import { ShortcutTile } from '../components/ShortcutTile'
import { SpotifyTabBar } from '../components/SpotifyTabBar'
import { home } from '../data'
import { sp } from '../theme'

export function HomeOffline() {
  return (
    <AppScreen className="font-figtree" background={sp.bg}>
      <StatusBar color="#fff" />
      <div className="mt-[24px] flex items-center gap-[8px] pl-[16px]">
        <Avatar size={32} className="mr-[4px]" badge={<span className="block h-[8px] w-[8px] rounded-full border border-black" style={{ background: sp.blue }} />} />
        {home.filters.map((f) => (
          <Chip key={f} label={f} active={f === home.activeFilter} />
        ))}
      </div>
      <div className="mt-[16px] grid grid-cols-2 gap-x-[9px] gap-y-[8px] px-[16px]">
        {home.shortcuts.map((s) => (
          <ShortcutTile key={s.key} item={s} />
        ))}
      </div>
      <section className="mt-[20px] px-[16px]">
        <h2 className="text-[17px] leading-[22px] font-bold text-white">{home.offlineTitle}</h2>
        <p className="mt-[2px] w-[310px] text-[12px] leading-[18px]" style={{ color: sp.muted }}>
          {home.offlineBody}
        </p>
      </section>
      <h2 className="mt-[21px] px-[16px] text-[20.5px] leading-[26px] font-bold text-white">{home.showsTitle}</h2>
      <div className="mt-[19px] flex gap-[20px] pl-[18px]">
        {home.shows.map((s) => (
          <MediaCard key={s.key} item={s} />
        ))}
      </div>
      <h2 className="mt-[23px] px-[16px] text-[20.5px] leading-[26px] font-bold text-white">{home.stationsTitle}</h2>
      <div className="mt-[19px] flex gap-[20px] pl-[18px]">
        {home.stations.map((c) => (
          <div key={c} className="relative h-[144px] w-[144px] shrink-0 overflow-hidden rounded-[3px]">
            <ImagePlaceholder className="h-full w-full" label="station cover" />
            <span className="absolute top-[7px] right-[8px] text-[8.5px] font-bold tracking-[1px] text-black/80">{home.stationLabel}</span>
          </div>
        ))}
      </div>
      <SpotifyTabBar
        tabs={home.tabs}
        active={home.activeTab}
        height={125}
        rowBottom={51}
        footer={<div className="absolute inset-x-0 top-[89px] text-center text-[11.5px] text-white">{home.offline}</div>}
      />
    </AppScreen>
  )
}
