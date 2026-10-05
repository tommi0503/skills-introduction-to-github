import { ImagePlaceholder } from '../../../ui'
import type { DocItem } from '../data'
import { gn } from '../theme'
import { FolderShape } from './FolderShape'

/** Renders the preview of a grid item: folder UI, page UI or image placeholder. */
export function DocThumb({ thumb }: { thumb: DocItem['thumb'] }) {
  const style = { left: thumb.x, top: thumb.y, width: thumb.w, height: thumb.h, borderRadius: thumb.radius }
  switch (thumb.kind) {
    case 'folder':
      return <FolderShape back={gn.folderBack} front={gn.folderFront} className="absolute" style={style} />
    case 'greenFolder':
      return <FolderShape back={gn.greenFolderBack} front={gn.greenFolderFront} paper className="absolute" style={style} />
    case 'blank':
      return (
        <div className="absolute bg-white shadow-[0_2px_6px_rgba(0,0,0,0.14)]" style={style}>
          <span className="absolute left-[7px] top-[7px] text-[5px] text-[#aaa]">Untitled</span>
        </div>
      )
    default:
      return <ImagePlaceholder className="absolute shadow-[0_1px_3px_rgba(0,0,0,0.12)]" style={style} label="document thumbnail" />
  }
}
