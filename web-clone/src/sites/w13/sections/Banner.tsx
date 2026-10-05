import { ImagePlaceholder } from '../../../ui'
import { banner } from '../data'
import { theme } from '../theme'

/** Gradient announcement strip. */
export function Banner() {
  return (
    <div className="absolute left-0 top-0 h-[40px] w-[1425px]">
      <ImagePlaceholder label="Gradient banner" tone={theme.tones.banner} className="absolute inset-0" />
      <span className="absolute left-[33px] top-[9px] flex h-[22px] items-center rounded-full bg-[#e9ebdf] px-[6px] font-geist text-[12px] tracking-[0.12px] text-[#151515]">
        {banner.badge}
      </span>
      <span className="absolute left-[179px] top-[9px] flex h-[22px] items-center rounded-full bg-[#151515] px-[6px] font-geist text-[12px] tracking-[0.12px] text-[#f7f8f4]">
        {banner.link}
        <span className="ml-[1px] text-[14px]">↗</span>
      </span>
    </div>
  )
}
