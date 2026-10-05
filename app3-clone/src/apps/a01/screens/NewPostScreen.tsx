import { ChevronRight, Copy, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { GalleryGrid } from '../components/GalleryGrid'
import { IgStatusBar } from '../components/IgStatusBar'
import { galleryTiles, newPost } from '../data'
import { ig } from '../theme'

/** Instagram "New post" media picker (dark). */
export function NewPostScreen() {
  return (
    <AppScreen background={ig.dark} className="font-inter text-white">
      <IgStatusBar color="#fff" />
      <div className="absolute inset-x-0 top-[66px] flex h-[28px] items-center justify-between px-[15px]">
        <X size={26} strokeWidth={1.7} />
        <span className="absolute left-1/2 -translate-x-1/2 text-[15px] font-semibold tracking-[-0.2px]">{newPost.title}</span>
        <span className="text-[15px] font-semibold" style={{ color: ig.link }}>
          {newPost.next}
        </span>
      </div>
      <ImagePlaceholder className="absolute inset-x-0 top-[198px] h-[220px]" label="selected photo" />
      <div className="absolute inset-x-0 top-[515px] flex h-[32px] items-center justify-between pr-[17px] pl-[15px]">
        <span className="flex items-center gap-[4px] text-[15px] font-semibold tracking-[-0.2px]">
          {newPost.album}
          <ChevronRight size={17} strokeWidth={2.4} />
        </span>
        <span className="flex h-[32px] w-[32px] items-center justify-center rounded-full bg-white text-black">
          <Copy size={16} strokeWidth={2.2} className="-scale-x-100" />
        </span>
      </div>
      <div className="absolute inset-x-0 top-[560px]">
        <GalleryGrid tiles={galleryTiles} />
      </div>
    </AppScreen>
  )
}
