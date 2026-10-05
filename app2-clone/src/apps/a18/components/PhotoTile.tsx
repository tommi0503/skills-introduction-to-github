import { CloudCheck } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { GridPhoto } from '../data'

/** Square library thumbnail with the "backed up" cloud badge. */
export function PhotoTile({ photo }: { photo: GridPhoto }) {
  return (
    <div className="relative aspect-square">
      <ImagePlaceholder label={photo.key} className="absolute inset-0" />
      <CloudCheck size={17} strokeWidth={1.6} className="absolute right-[12px] bottom-[6px] text-white drop-shadow-[0_0_1px_rgba(0,0,0,0.7)]" />
    </div>
  )
}
