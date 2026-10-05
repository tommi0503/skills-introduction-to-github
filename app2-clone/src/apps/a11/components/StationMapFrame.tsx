import type { ReactNode } from 'react'
import { ListFilter, Navigation, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import type { Pin } from '../data'
import { GlassButton } from './GlassButton'
import { MapPin } from './MapPin'
import { StatusOverlay } from './StatusOverlay'

export interface StationMapFrameProps {
  pins: Pin[]
  /** extra overlay (attribution, selected-station card...) */
  children?: ReactNode
}

/** Modal map sheet: map placeholder, title, close / filter / locate buttons and station pins. */
export function StationMapFrame({ pins, children }: StationMapFrameProps) {
  return (
    <AppScreen background="#000" className="font-inter text-white">
      <StatusOverlay />
      <div className="absolute inset-x-0 top-[58px] bottom-[4px] overflow-hidden rounded-t-[38px] rounded-b-[40px]">
        <ImagePlaceholder tone="#121a3a" label="satellite map" className="absolute inset-0" />
      </div>
      <div className="absolute top-[85px] left-0 w-full text-center text-[16px] font-semibold">Station Map</div>
      <GlassButton className="top-[74px] left-[329px]">
        <X size={22} strokeWidth={1.8} />
      </GlassButton>
      <GlassButton size={42} className="top-[134px] left-[331px]">
        <span className="flex h-[19px] w-[19px] items-center justify-center rounded-full border-[1.6px] border-white">
          <ListFilter size={11} strokeWidth={2.6} />
        </span>
      </GlassButton>
      <GlassButton className="top-[183px] left-[330px]">
        <Navigation size={18} strokeWidth={2} fill="#fff" className="-rotate-0" />
      </GlassButton>
      {pins.map((p) => (
        <MapPin key={p.id} pin={p} />
      ))}
      {children}
    </AppScreen>
  )
}
