import { ArrowUpRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { SearchResult } from '../data'
import { zip } from '../theme'

/** One merchant suggestion: logo, name, (Ad) url, outbound arrow. */
export function ResultRow({ item }: { item: SearchResult }) {
  return (
    <div className="flex h-[53px] items-center border-b pr-[18px] pl-[16px]" style={{ borderColor: zip.divider }}>
      <ImagePlaceholder label={item.title} className="h-[25px] w-[25px] rounded-full" />
      <div className="ml-[15px] min-w-0 flex-1">
        <div className="text-[15px] leading-[19px] font-[560]">{item.title}</div>
        <div className="flex items-center gap-[4px] text-[13px] leading-[17px] text-[#7a7a7f]">
          {item.ad && (
            <span className="rounded-[3px] px-[3px] text-[12px] leading-[15px] text-[#3a3340]" style={{ background: zip.adTag }}>
              Ad
            </span>
          )}
          {item.subtitle}
        </div>
      </div>
      <ArrowUpRight size={24} strokeWidth={1.6} />
    </div>
  )
}
