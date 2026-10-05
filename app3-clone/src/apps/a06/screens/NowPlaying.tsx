import {
  ChevronDown,
  CirclePlus,
  Ellipsis,
  AlignJustify,
  Maximize2,
  MonitorSpeaker,
  Pause,
  Repeat,
  Share,
  Shuffle,
  SkipBack,
  SkipForward,
  X,
} from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { player } from '../data'
import { sp } from '../theme'

/** Transport controls keyed by their horizontal centre (as laid out in the app). */
const transport = [
  { x: 36, node: <Shuffle size={23} strokeWidth={1.8} /> },
  { x: 111, node: <SkipBack size={26} fill="#fff" strokeWidth={2} /> },
  {
    x: 195,
    node: (
      <span className="flex h-[63px] w-[63px] items-center justify-center rounded-full bg-white">
        <Pause size={26} fill="#000" strokeWidth={0} />
      </span>
    ),
  },
  { x: 277, node: <SkipForward size={26} fill="#fff" strokeWidth={2} /> },
  { x: 352, node: <Repeat size={21} strokeWidth={1.8} /> },
]

export function NowPlaying() {
  return (
    <AppScreen className="font-figtree" background={sp.canvasTone}>
      <ImagePlaceholder tone={sp.canvasTone} className="absolute inset-0" label="song canvas video" />
      <div className="relative text-white">
        <StatusBar color="#fff" />
        <div className="mt-[22px] flex items-center justify-between px-[24px]">
          <ChevronDown size={22} strokeWidth={2} />
          <span className="text-[11.5px] font-bold">{player.context}</span>
          <Ellipsis size={20} />
        </div>
      </div>

      <div className="absolute inset-x-[25px] top-[547px] flex items-center text-white">
        <ImagePlaceholder className="h-[46px] w-[46px] rounded-[3px]" label="cover art" />
        <div className="ml-[13px] flex-1">
          <div className="text-[20.5px] leading-[24px] font-bold">{player.title}</div>
          <div className="mt-[4px] flex items-center gap-[6px] text-[13px] text-white/75">
            <span className="flex h-[11px] w-[11px] items-center justify-center rounded-[2px] bg-white/60 text-[7px] font-bold text-black">E</span>
            {player.artist}
          </div>
        </div>
        <X size={24} strokeWidth={1.6} className="mr-[22px]" />
        <CirclePlus size={28} strokeWidth={1.6} />
      </div>

      <div className="absolute inset-x-[25px] top-[620px] text-white">
        <div className="relative h-[4px] rounded-full bg-white/30">
          <div className="h-full rounded-full bg-white" style={{ width: `${player.progress * 100}%` }} />
          <span className="absolute top-1/2 h-[11px] w-[11px] -translate-y-1/2 rounded-full bg-white" style={{ left: `calc(${player.progress * 100}% - 5px)` }} />
        </div>
        <div className="mt-[6px] flex justify-between text-[9.5px] text-white/75">
          <span>{player.elapsed}</span>
          <span>{player.remaining}</span>
        </div>
      </div>

      <div className="absolute inset-x-0 top-[694px] text-white">
        {transport.map(({ x, node }) => (
          <span key={x} className="absolute flex -translate-x-1/2 -translate-y-1/2 items-center justify-center" style={{ left: x }}>
            {node}
          </span>
        ))}
      </div>

      <div className="absolute inset-x-[27px] top-[744px] flex items-center text-white">
        <MonitorSpeaker size={19} strokeWidth={1.6} />
        <span className="flex-1" />
        <Share size={19} strokeWidth={1.6} className="mr-[26px]" />
        <AlignJustify size={20} strokeWidth={1.6} />
      </div>

      <div className="absolute inset-x-[16px] top-[795px] flex h-[70px] items-start justify-between rounded-[10px] px-[16px] pt-[13px] text-white" style={{ background: sp.lyrics }}>
        <span className="mt-[4px] text-[12.5px] font-bold">{player.lyrics}</span>
        <div className="flex gap-[17px]">
          {[Share, Maximize2].map((Icon, i) => (
            <span key={i} className="flex h-[28px] w-[28px] items-center justify-center rounded-full bg-black/25">
              <Icon size={13} strokeWidth={2} />
            </span>
          ))}
        </div>
      </div>
    </AppScreen>
  )
}
