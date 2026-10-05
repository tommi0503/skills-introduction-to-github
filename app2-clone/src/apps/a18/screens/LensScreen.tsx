import { ChevronLeft, Ellipsis, Tag } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { CropFrame } from '../components/CropFrame'
import { lens } from '../data'
import { theme } from '../theme'

export function LensScreen() {
  return (
    <AppScreen background={theme.dark}>
      <Chrome color="#fff" chipClassName="bg-[#5e5e5e]/95!" />
      <div className="absolute inset-x-0 top-[62px] flex h-[36px] items-center px-[17px] text-white">
        <ChevronLeft size={26} strokeWidth={2} />
        <h1 className="flex-1 text-center font-outfit text-[23px] tracking-[-0.2px]">{lens.title}</h1>
        <Ellipsis size={20} strokeWidth={2.2} />
      </div>
      {/* dimmed full-bleed photo with the highlighted selection */}
      <ImagePlaceholder label="dimmed photo" tone={theme.lensDim} className="absolute inset-x-0 top-[169px] bottom-0" />
      <ImagePlaceholder label="selected T-shirt" className="absolute top-[284px] left-[47px] h-[255px] w-[299px] rounded-[10px]" />
      <CropFrame className="top-[284px] left-[47px] h-[255px] w-[299px]" arm={20} thickness={3} radius={12} />
      <section className="absolute inset-x-0 top-[551px] bottom-0 overflow-hidden rounded-t-[26px] bg-white">
        <span className="absolute top-[11px] left-1/2 h-[4px] w-[26px] -translate-x-1/2 rounded-full bg-[#dadce0]" />
        <div className="absolute top-[23px] left-[16px] h-[171px] w-[170px] rounded-[18px] bg-[#f4f4f4]">
          <ImagePlaceholder label="product photo" className="absolute inset-x-[8px] top-[10px] bottom-[10px] rounded-[10px]" />
          <span className="absolute top-[14px] left-[12px] flex h-[25px] items-center gap-[4px] rounded-full bg-white px-[8px] text-[13px] text-[#1f1f1f]">
            <Tag size={13} strokeWidth={1.8} />
            {lens.price}
          </span>
        </div>
        <div className="absolute top-[204px] left-[19px] flex items-center gap-[7px] text-[12px] tracking-[0.5px] text-[#5f6368]">
          <ImagePlaceholder label="GOAT favicon" className="size-[12px] rounded-[2px]" />
          {lens.source}
        </div>
        <p className="absolute top-[27px] left-[199px] text-[16px] font-medium text-[#1f1f1f]">{lens.relatedTitle}</p>
        {lens.related.map((r) => (
          <div key={r.key} className="absolute top-[61px] left-[200px] flex h-[60px] w-[172px] items-center justify-between rounded-[14px] bg-[#f4f4f4] pr-[10px] pl-[11px]">
            <span className="text-[14px] text-[#1f1f1f]">{r.label}</span>
            <ImagePlaceholder label={`${r.label} thumbnail`} className="size-[30px] rounded-[4px]" />
          </div>
        ))}
        <div className="absolute top-[138px] left-[200px] h-[120px] w-[172px] rounded-[16px] bg-[#f2f2f2]">
          <ImagePlaceholder label="related result" className="absolute inset-x-[16px] top-[16px] bottom-0 rounded-[8px]" />
        </div>
        <div className="absolute inset-x-0 bottom-0 flex h-[80px] items-start justify-center gap-[14px] bg-[#f2f2f2] pt-[10px] pr-[30px]">
          {lens.modes.map((m) => (
            <span
              key={m}
              className={cn(
                'flex h-[31px] items-center rounded-full px-[14px] text-[14.5px]',
                m === lens.activeMode ? 'bg-[#1a5ad8] text-white' : 'text-[#1f1f1f]',
              )}
            >
              {m}
            </span>
          ))}
        </div>
      </section>
    </AppScreen>
  )
}
