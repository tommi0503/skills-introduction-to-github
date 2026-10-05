import type { ReactNode } from 'react'
import { BadgeCheck, Ban, ChevronRight, Share, Star, ThumbsUp } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { CircleIcon, NavHeader } from '../components/NavHeader'
import { place } from '../data'
import { bond } from '../theme'

function PhotoStrip({ widths }: { widths: readonly number[] }) {
  return (
    <div className="absolute flex gap-[8px]" style={{ left: -2, top: 19.5, height: 120 }}>
      {widths.map((w, i) => (
        <ImagePlaceholder key={i} label="place photo" className="h-full rounded-[15px]" style={{ width: w }} />
      ))}
    </div>
  )
}

function ReactionChip() {
  return (
    <div
      className="absolute flex items-center gap-[12px] rounded-full bg-white pl-[9px]"
      style={{ left: 302.8, top: 134, width: 78, height: 52, boxShadow: '0 3px 12px rgba(0,0,0,0.08)' }}
    >
      <ImagePlaceholder label="avatar" className="h-[33px] w-[33px] rounded-full" />
      <ThumbsUp size={17} strokeWidth={1.5} fill="#111" className="text-white" />
    </div>
  )
}

function ActionButton({ label, primary, icon }: { label: string; primary?: boolean; icon?: ReactNode }) {
  return (
    <div
      className={cn(
        'flex h-[52px] flex-1 items-center justify-center gap-[9px] rounded-full text-[16px] font-medium',
        primary ? 'bg-[#0d0d0d] text-white' : 'bg-white text-[#111]',
      )}
      style={{ boxShadow: '0 6px 16px rgba(0,0,0,0.08)' }}
    >
      {icon}
      {label}
    </div>
  )
}

export function PlaceScreen() {
  return (
    <div className="relative h-full font-inter" style={{ background: bond.screen }}>
      <HighlightStatusBar />
      <NavHeader
        center={
          <div className="relative">
            <ImagePlaceholder label="avatar" className="h-[33px] w-[33px] rounded-full" />
            <span className="absolute -right-[2px] -bottom-[2px] h-[12px] w-[12px] rounded-full border-[1.5px] border-white bg-[#222]" />
          </div>
        }
        right={<CircleIcon icon={Share} iconSize={19} />}
      />
      <p className="absolute inset-x-0 text-center text-[15.5px] font-medium text-[#444]" style={{ top: 104, letterSpacing: -0.2 }}>
        {place.query}
      </p>

      <div
        className="absolute overflow-hidden rounded-[24px]"
        style={{ left: 16.5, top: 144.5, width: 358, height: 490, background: bond.card, boxShadow: '0 4px 18px rgba(0,0,0,0.05)' }}
      >
        <PhotoStrip widths={place.photos} />
        <div className="absolute" style={{ left: 19.5, right: 19.5, top: 172 }}>
          <div className="flex items-center">
            <h2 className="flex-1 pr-[6px] text-[22px] leading-[29px] font-medium text-[#0d0d0d]" style={{ letterSpacing: -0.45 }}>
              {place.name}
            </h2>
            <ChevronRight size={17} strokeWidth={1.6} className="shrink-0 text-[#666]" />
          </div>
          <div className="mt-[8px] flex items-start justify-between">
            <div className="text-[13.5px] leading-[20.5px] text-[#9a9a9a]">
              <div className="flex items-center gap-[4px]">
                {place.category} ·
                <Star size={14} fill="#2f7ff0" strokeWidth={0} />
                {place.rating}
              </div>
              <div>{place.address}</div>
            </div>
            <ImagePlaceholder label="map" className="-mt-[3px] h-[41px] w-[40px] rounded-[6px]" />
          </div>
          <div className="mt-[10px] h-px bg-[#e6e6e6]" />
          <p className="mt-[18px] text-[13.7px] leading-[17px] text-[#1a1a1a]" style={{ letterSpacing: -0.2 }}>
            {place.summary.map((s, i) => (
              <span key={i} className={s.bold ? 'font-semibold' : undefined}>
                {s.text}
              </span>
            ))}
            <span className="ml-[7px] text-[#9a9a9a]">{place.less}</span>
          </p>
          <div className="mt-[17px] inline-flex h-[27px] items-center gap-[5px] rounded-full bg-[#f0f0f0] pr-[8px] pl-[8px] text-[12px] text-[#9a9a9a]">
            <Ban size={13} strokeWidth={1.5} />
            {place.memories}
            <ChevronRight size={13} strokeWidth={1.6} className="ml-[4px]" />
          </div>
        </div>
      </div>
      <ReactionChip />

      <div className="absolute flex gap-[12px]" style={{ left: 24, right: 25.5, top: 774 }}>
        <ActionButton label={place.actions.secondary} icon={<BadgeCheck size={19} strokeWidth={1.6} />} />
        <ActionButton label={place.actions.primary} primary />
      </div>
    </div>
  )
}
