import { ChevronLeft, Ellipsis, Play, Shuffle } from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { SpotifyTabBar } from '../components/SpotifyTabBar'
import { TrackRow } from '../components/TrackRow'
import { artist } from '../data'
import { sp } from '../theme'

export function Artist() {
  return (
    <AppScreen className="font-figtree" background={sp.bg}>
      <ImagePlaceholder tone={sp.heroTone} className="absolute inset-x-0 top-0 h-[315px]" label="artist photo" />
      <div className="relative text-white">
        <StatusBar color="#fff" />
        <ChevronLeft size={24} strokeWidth={1.6} className="mt-[3px] ml-[20px]" />
      </div>
      <h1 className="absolute top-[252px] left-[16px] text-[43px] leading-[60px] font-extrabold tracking-[-1px] text-white">{artist.name}</h1>

      <div className="absolute inset-x-[16px] top-[325px]">
        <p className="text-[11.5px]" style={{ color: sp.muted }}>
          {artist.listeners}
        </p>
        <div className="mt-[8px] flex items-center">
          <span className="flex h-[40px] w-[32px] items-center justify-center rounded-[5px] border-[1.5px] border-white/60">
            <ImagePlaceholder className="h-[32px] w-[24px] rounded-[2px]" label="artist pick" />
          </span>
          <span className="ml-[24px] flex h-[31px] items-center rounded-full border border-white/50 px-[15px] text-[12px] font-bold text-white">
            {artist.follow}
          </span>
          <Ellipsis size={20} color="#fff" className="ml-[25px]" />
          <span className="flex-1" />
          <Shuffle size={21} strokeWidth={1.8} color={sp.muted} className="mr-[30px]" />
          <span className="flex h-[48px] w-[48px] items-center justify-center rounded-full" style={{ background: sp.green }}>
            <Play size={19} fill="#000" strokeWidth={0} />
          </span>
        </div>
        <div className="mt-[10px] flex gap-[26px] text-[14.5px]">
          {artist.tabs.map((t) => {
            const on = t === artist.activeTab
            return (
              <div key={t} className="flex flex-col">
                <span style={{ color: on ? '#fff' : sp.muted, fontWeight: on ? 700 : 400 }}>{t}</span>
                <span className="mt-[6px] h-[2px] rounded-full" style={{ background: on ? sp.green : 'transparent' }} />
              </div>
            )
          })}
        </div>
      </div>

      <h2 className="absolute top-[458px] left-[16px] text-[17px] font-bold text-white">{artist.popular}</h2>
      <div className="absolute inset-x-0 top-[489px]">
        {artist.tracks.map((t, i) => (
          <TrackRow key={t.key} track={t} index={i + 1} />
        ))}
      </div>
      <SpotifyTabBar tabs={artist.navTabs} active={artist.activeNav} height={115} />
    </AppScreen>
  )
}
