import { Ellipsis } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { FloatingNav } from '../components/FloatingNav'
import { LibraryHeader } from '../components/LibraryHeader'
import { PhotoTile } from '../components/PhotoTile'
import { library } from '../data'

export function LibraryScreen() {
  return (
    <AppScreen className="font-dm">
      <Chrome />
      <LibraryHeader initial={library.avatarInitial} />
      <div className="absolute inset-x-0 top-[130px] grid grid-cols-3 gap-[2px]">
        {library.photos.map((p) => (
          <PhotoTile key={p.key} photo={p} />
        ))}
      </div>
      <span className="absolute top-[128px] left-[137px] flex h-[36px] w-[114px] items-center justify-center rounded-full bg-white text-[15px] text-[#1f1f1f] shadow-[0_1px_6px_rgba(0,0,0,0.15)]">
        {library.dateChip}
      </span>
      <span className="absolute top-[126px] left-[341px] flex size-[40px] items-center justify-center rounded-full bg-white/90 text-[#1f1f1f] shadow-[0_1px_6px_rgba(0,0,0,0.12)]">
        <Ellipsis size={18} strokeWidth={2} />
      </span>
      <FloatingNav items={library.nav} activeKey={library.activeNav} widths={library.navWidths} />
    </AppScreen>
  )
}
