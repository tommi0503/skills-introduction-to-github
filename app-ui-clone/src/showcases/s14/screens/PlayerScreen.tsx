import { RefreshCw, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { CategoryTabs } from '../components/CategoryTabs'
import { MoodPhone } from '../components/MoodPhone'
import { PlayButton } from '../components/PlayButton'
import { Waveform } from '../components/Waveform'
import { activeCategory, categories, waveformPattern, type Track } from '../data'
import { palette, type MoodTheme } from '../theme'

export interface PlayerScreenProps {
  theme: MoodTheme
  track: Track
  /** Number of waveform bars already played. */
  played: number
}

function GhostControl({ icon: Icon }: { icon: typeof X }) {
  return (
    <span className="flex h-[55px] w-[55px] items-center justify-center rounded-full border-[1.5px] border-dotted border-white/25 text-white">
      <Icon size={18} strokeWidth={1.8} />
    </span>
  )
}

/** Now-playing card: cover, title, progress waveform and transport controls. */
export function PlayerScreen({ theme, track, played }: PlayerScreenProps) {
  return (
    <MoodPhone theme={theme}>
      <CategoryTabs items={categories} active={activeCategory} className="absolute left-[16px] right-[16px] top-[69px]" />
      <div
        className="absolute left-[16px] top-[112px] h-[608px] w-[358px] rounded-[25px] p-[3.5px]"
        style={{ background: palette.playerCard }}
      >
        <ImagePlaceholder label={track.artLabel} className="h-[290px] w-full rounded-[22px]" />
        <div className="mt-[30px] text-center text-[31.5px] font-medium leading-[38px] tracking-[-0.3px]">{track.title}</div>
        <div className="mt-[9px] text-center text-[15px] tracking-[-0.1px] text-white/80">{track.description}</div>
        <Waveform
          pattern={waveformPattern}
          width={330}
          height={62}
          played={played}
          color="rgba(255,255,255,0.35)"
          playedColor="rgba(255,255,255,0.85)"
          className="mx-auto mt-[37px]"
        />
        <div className="mt-[39px] flex items-center justify-center gap-[16px]">
          <GhostControl icon={X} />
          <PlayButton />
          <GhostControl icon={RefreshCw} />
        </div>
      </div>
    </MoodPhone>
  )
}
