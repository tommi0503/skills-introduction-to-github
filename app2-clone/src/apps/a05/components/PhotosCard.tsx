import { Camera, Plus, Trash2 } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'

export interface PhotosCardProps {
  uploaded: number
  suggestions: number
  label: string
  className?: string
}

/** Uploaded photos (deletable), "add photos" row and a grid of suggestions. */
export function PhotosCard({ uploaded, suggestions, label, className }: PhotosCardProps) {
  return (
    <div className={cn('rounded-[14px] bg-white px-[12px] pt-[12px]', className)}>
      <div className="flex gap-[2px]">
        {Array.from({ length: uploaded }, (_, i) => (
          <div key={i} className="relative h-[119px] w-[109px]">
            <ImagePlaceholder label="uploaded photo" className="h-full w-full rounded-[4px]" />
            <span className="absolute bottom-[8px] right-[8px] flex h-[29px] w-[29px] items-center justify-center rounded-full bg-white">
              <Trash2 size={16} strokeWidth={1.6} color="#d8453e" />
            </span>
          </div>
        ))}
      </div>
      <div className="mt-[12px] flex items-center gap-[8px] pl-[3px] text-[15px] font-semibold text-[#222]">
        <Camera size={17} strokeWidth={1.6} color="#555" />
        {label}
      </div>
      <div className="mt-[11px] flex gap-[3px]">
        <div className="flex h-[99px] w-[108px] items-center justify-center rounded-[4px] bg-[#f5f4f6]">
          <Plus size={20} strokeWidth={1.6} color="#222" />
        </div>
        {Array.from({ length: suggestions }, (_, i) => (
          <ImagePlaceholder key={i} label="suggested screenshot" tone="#eceef0" className="h-[99px] w-[109px] rounded-[2px]" />
        ))}
      </div>
    </div>
  )
}
