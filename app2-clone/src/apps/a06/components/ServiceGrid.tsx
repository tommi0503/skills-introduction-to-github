import { ImagePlaceholder, cn } from '../../../ui'
import type { GridItem } from '../data'

/** 5-column grid of rounded icon tiles (3D art → placeholders) with captions and optional badges. */
export function ServiceGrid({ rows, className }: { rows: GridItem[][]; className?: string }) {
  return (
    <div className={cn('flex flex-col gap-[15px]', className)}>
      {rows.map((row, r) => (
        <div key={r} className="flex">
          {row.map((it) => (
            <div key={it.key} className="relative flex w-[73.5px] flex-col items-center">
              <div className="flex h-[60px] w-[60px] items-center justify-center rounded-[18px] bg-[#f5f6f8]">
                <ImagePlaceholder label={it.label} className="h-[46px] w-[46px] rounded-[12px]" />
              </div>
              {it.badge && (
                <span className="absolute -top-[9px] rounded-full border border-[#d9dcf5] bg-white px-[5px] text-[9.5px] leading-[15px] text-[#4b3ad6]">
                  {it.badge}
                </span>
              )}
              <span className="mt-[6px] whitespace-nowrap text-[12.5px] leading-none tracking-[-0.4px] text-[#222]">{it.label}</span>
            </div>
          ))}
        </div>
      ))}
    </div>
  )
}
