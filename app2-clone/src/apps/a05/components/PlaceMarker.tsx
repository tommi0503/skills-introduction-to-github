import { Star } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'

/** Selected-place marker: ringed bubble with pointer, favourite star and location dot. */
export function PlaceMarker({ className }: { className?: string }) {
  return (
    <div className={cn('absolute h-[80px] w-[56px]', className)}>
      <div className="absolute left-[30px] top-[38px] h-[14px] w-[14px] -translate-x-1/2 rotate-45 bg-black" style={{ left: 28 }} />
      <div className="absolute left-[2px] top-0 flex h-[52px] w-[52px] items-center justify-center rounded-full border-[2px] border-black bg-white">
        <ImagePlaceholder label="croissant" tone="#e9cf9e" className="h-[34px] w-[34px] rounded-full" />
      </div>
      <Star size={16} fill="#f6b82b" color="#f6b82b" className="absolute right-[-6px] top-[-4px]" />
      <span className="absolute left-[25px] top-[71px] h-[7px] w-[7px] rounded-full bg-black" />
    </div>
  )
}
