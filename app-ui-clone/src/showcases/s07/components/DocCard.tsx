import { Scan } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { ScanDoc } from '../data'
import { theme } from '../theme'

/** Library grid tile: scan thumbnail + optional title / meta footer. */
export function DocCard({ doc, imageHeight, height }: { doc: ScanDoc; imageHeight: number; height: number }) {
  return (
    <div className="relative overflow-hidden rounded-[6px] bg-white" style={{ height, boxShadow: '0 0 0 1px #ece9e3' }}>
      <ImagePlaceholder label={`${doc.id} scan`} style={{ height: imageHeight }} className="w-full" />
      <Scan size={13} strokeWidth={2.4} className="absolute top-[8px] right-[8px]" style={{ color: theme.accent }} />
      {doc.title && (
        <div className="px-[13px] pt-[13px]">
          <div className="font-inter text-[13.6px] leading-[18px] font-[580] tracking-[-0.01em]" style={{ color: theme.ink }}>
            {doc.title}
          </div>
          <div className="mt-[4px] font-plexmono text-[9.5px] leading-[15.5px] tracking-[0.04em]" style={{ color: theme.muted }}>
            <div>{doc.meta}</div>
            <div>{doc.date}</div>
          </div>
        </div>
      )}
    </div>
  )
}
