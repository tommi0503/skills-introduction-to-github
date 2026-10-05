import { MonitorSpeaker, Play } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import { sp } from '../theme'

export interface MiniPlayerProps {
  title: string
  artist: string
  progress: number
  className?: string
}

export function MiniPlayer({ title, artist, progress, className }: MiniPlayerProps) {
  return (
    <div className={cn('relative flex h-[56px] items-center overflow-hidden rounded-[6px] pr-[16px] pl-[8px]', className)} style={{ background: sp.miniPlayer }}>
      <ImagePlaceholder tone="#3a4a57" className="h-[38px] w-[38px] rounded-[3px]" label="album art" />
      <div className="ml-[10px] flex-1">
        <div className="text-[12.5px] leading-[16px] font-semibold text-white">{title}</div>
        <div className="mt-[2px] text-[12.5px] leading-[16px]" style={{ color: sp.muted }}>
          {artist}
        </div>
      </div>
      <MonitorSpeaker size={21} strokeWidth={1.6} color="#fff" className="mr-[24px]" />
      <Play size={20} fill="#fff" strokeWidth={0} />
      <div className="absolute inset-x-[8px] bottom-0 h-[2px] bg-white/25">
        <div className="h-full bg-white" style={{ width: `${progress * 100}%` }} />
      </div>
    </div>
  )
}
