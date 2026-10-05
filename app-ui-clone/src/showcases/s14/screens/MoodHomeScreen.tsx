import { AlbumStack } from '../components/AlbumStack'
import { CategoryTabs } from '../components/CategoryTabs'
import { MoodPhone } from '../components/MoodPhone'
import { PlayButton } from '../components/PlayButton'
import { TrackCard } from '../components/TrackCard'
import { Waveform } from '../components/Waveform'
import { activeCategory, categories, peekTracks, tracks, waveformPattern, type LatestRelease } from '../data'
import type { MoodTheme } from '../theme'

export interface MoodHomeScreenProps {
  theme: MoodTheme
  latest: LatestRelease
}

/** Home template: latest release hero, waveform, categories and track rows. Skinned via `theme`. */
export function MoodHomeScreen({ theme, latest }: MoodHomeScreenProps) {
  return (
    <MoodPhone theme={theme}>
      <div className="absolute left-[16px] top-[66px]">
        <AlbumStack coverLabel={latest.coverLabel} tint={theme.stackTint} />
      </div>
      <div className="absolute left-[16px] top-[256px] text-[12.5px] text-white/75">{latest.eyebrow}</div>
      <h2 className="absolute left-[16px] top-[284px] m-0 text-[32px] font-medium leading-[37.5px] tracking-[-0.3px]">
        {latest.titleLines.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h2>
      <div className="absolute left-[318px] top-[293px]">
        <PlayButton />
      </div>
      <Waveform pattern={waveformPattern} width={359} height={62} barWidth={2} color="rgba(255,255,255,0.8)" className="absolute left-[15px] top-[379px]" />
      <CategoryTabs items={categories} active={activeCategory} className="absolute left-[16px] right-[16px] top-[474px]" />
      <div className="absolute left-[15px] top-[513px] flex flex-col gap-[8px]">
        {tracks.map((t, i) => (
          <div key={t.title} className="flex gap-[8px]">
            <TrackCard track={t} />
            <TrackCard track={peekTracks[i]} />
          </div>
        ))}
      </div>
    </MoodPhone>
  )
}
