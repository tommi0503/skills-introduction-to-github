import { ChevronDown, SlidersHorizontal } from 'lucide-react'
import { AppScreen, HomeIndicator, ImagePlaceholder } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { ProductCard } from '../components/ProductCard'
import { SearchHeader } from '../components/SearchHeader'
import { banner, gridIcon as GridIcon, results, resultsHeader as h } from '../data'

export function ResultsScreen() {
  return (
    <AppScreen className="font-pretendard">
      <PhoneStatus />
      <SearchHeader query={h.query} />
      <div className="absolute top-[106px] left-[17px] flex w-[357px] items-center">
        <span className="text-[16.5px] font-bold text-[#111]">상품</span>
        <span className="ml-[5px] flex-1 text-[15px] text-[#b0b0b4]">{h.count}</span>
        <span className="flex items-center gap-[4px] text-[12.5px] text-[#777]">
          {h.sort} <ChevronDown size={15} strokeWidth={1.6} />
        </span>
        <GridIcon size={18} strokeWidth={1.6} className="ml-[23px] text-[#666]" />
      </div>
      <span className="absolute top-[117px] left-[384px] h-[34px] w-[3px] rounded-full bg-[#c8c8cc]" />
      <div className="absolute top-[146px] left-[14px] flex gap-[7px]">
        {h.filters.map((f) => (
          <span key={f} className="flex h-[31px] items-center gap-[3px] rounded-full border border-[#e6e6e8] bg-white px-[12px] text-[12.5px] whitespace-nowrap text-[#333]">
            {f}
            {h.dropdown.includes(f) && <ChevronDown size={13} strokeWidth={1.6} className="text-[#aaa]" />}
          </span>
        ))}
      </div>
      <div className="absolute top-[146px] right-[0px] flex h-[31px] w-[58px] items-center justify-end bg-gradient-to-r from-white/0 to-white to-30% pr-[16px]">
        <span className="flex h-[30px] w-[30px] items-center justify-center rounded-full bg-[#f2f2f4]">
          <SlidersHorizontal size={14} strokeWidth={1.8} />
        </span>
      </div>
      <div className="absolute top-[193px] inset-x-0 h-[146px] overflow-hidden" style={{ background: 'linear-gradient(90deg,#1a0b1e 0%,#24112b 60%,#3a1b40 100%)' }}>
        <h3 className="absolute top-[34px] left-[20px] text-[19.5px] leading-[28px] font-bold whitespace-pre-line text-white">{banner.title}</h3>
        <span className="absolute top-[94px] left-[20px] text-[12.5px] text-[#d8cfe0]">{banner.sub}</span>
        <ImagePlaceholder tone="#6b3d77" label="100 won 3D art" className="absolute top-[30px] left-[225px] h-[90px] w-[140px] rounded-[12px]" />
      </div>
      <div className="absolute top-[364px] left-0 flex gap-[3px]">
        {results.map((p) => (
          <ProductCard key={p.key} product={p} width={193.5} imageHeight={232} size="regular" textInset={15} />
        ))}
      </div>
      <div className="absolute top-[762px] left-0 flex gap-[3px]">
        <ImagePlaceholder label="product photo" className="h-[120px] w-[193.5px]" />
        <ImagePlaceholder label="product photo" className="h-[120px] w-[193.5px]" />
      </div>
      <HomeIndicator width={140} bottom={6} />
    </AppScreen>
  )
}
