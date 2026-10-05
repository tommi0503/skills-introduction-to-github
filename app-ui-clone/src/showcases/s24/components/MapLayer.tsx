import { LocateFixed, Menu } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { theme } from '../theme'

export interface MapLayerProps {
  /** Visible height of the map (it continues under the sheet). */
  height: number
  showLocate?: boolean
  className?: string
}

/** Map (placeholder) with the hamburger button and optional locate FAB. */
export function MapLayer({ height, showLocate = true, className }: MapLayerProps) {
  return (
    <div className={cn('absolute inset-x-0 top-0', className)} style={{ height }}>
      <ImagePlaceholder label="지도" className="absolute inset-0" />
      <Menu size={25} strokeWidth={2.4} color="#111" className="absolute top-[64px] left-[20px]" />
      {showLocate && (
        <div
          className="absolute top-[263px] left-[335px] flex h-[37px] w-[37px] items-center justify-center rounded-full bg-white"
          style={{ boxShadow: '0 1px 6px rgba(0,0,0,0.15)' }}
        >
          <LocateFixed size={22} strokeWidth={2.2} color={theme.navy} />
        </div>
      )}
    </div>
  )
}
