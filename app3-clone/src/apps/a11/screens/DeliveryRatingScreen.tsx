import { ChevronDown, Gift, Search, Star, User, X } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import { ChipRows } from '../components/Chip'
import { SheetScreen } from '../components/SheetScreen'
import { delivery as d } from '../data'

const yellow = '#ffc244'

function CategoryBubble({ label, x, y, size }: { label?: string; x: number; y: number; size: number }) {
  return (
    <div
      className="absolute flex flex-col items-center justify-end rounded-full bg-[#fff8e6] pb-[22px]"
      style={{ left: x - size / 2, top: y - size / 2, width: size, height: size }}
    >
      {label && (
        <>
          <ImagePlaceholder className="mb-[6px] h-[44px] w-[50px] rounded-[6px]" label={`${label} illustration`} />
          <span className="text-[14px] text-[#333]">{label}</span>
        </>
      )}
    </div>
  )
}

function HomeBackdrop() {
  return (
    <>
      <span className="absolute top-[49px] left-[13px] flex h-[38px] w-[38px] items-center justify-center rounded-full bg-[#ffd56e]">
        <User size={18} strokeWidth={2} className="text-[#222]" />
      </span>
      <div className="absolute top-[52px] left-[67px] flex h-[34px] w-[256px] items-center justify-center gap-[6px] rounded-full bg-[#ffd56e] text-[16px] text-[#5a4a1e]">
        <Search size={15} strokeWidth={2} />
        {d.searchPlaceholder}
      </div>
      <span className="absolute top-[49px] right-[14px] flex h-[38px] w-[38px] items-center justify-center rounded-full bg-[#ffd56e]">
        <Gift size={18} strokeWidth={2} className="text-[#222]" />
      </span>
      <p className="absolute inset-x-0 top-[103px] flex items-center justify-center gap-[4px] text-[17px] font-semibold text-[#111]">
        {d.address}
        <ChevronDown size={16} strokeWidth={2.4} />
      </p>
      <CategoryBubble label={d.categories[0]} x={134} y={273} size={110} />
      <CategoryBubble label={d.categories[1]} x={250} y={273} size={110} />
      <CategoryBubble x={58} y={370} size={110} />
      <CategoryBubble x={333} y={370} size={110} />
    </>
  )
}

export function DeliveryRatingScreen() {
  return (
    <SheetScreen
      className="font-jakarta"
      background={yellow}
      dim={0.6}
      sheetTop={329}
      sheetClassName="rounded-t-[22px] bg-white"
      backdrop={<HomeBackdrop />}
      status={{ color: '#fff' }}
    >
      <X size={24} strokeWidth={2.4} className="absolute top-[17px] right-[19px] text-[#111]" />
      <h2 className="absolute inset-x-0 top-[70px] text-center text-[24.5px] leading-[31px] font-extrabold text-[#111]">
        {d.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h2>
      <div className="absolute inset-x-0 top-[150px] flex justify-center gap-[16px]">
        {Array.from({ length: d.stars }, (_, i) => (
          <Star key={i} size={46} fill="#f6c143" strokeWidth={0} />
        ))}
      </div>
      <p className="absolute inset-x-0 top-[215px] text-center text-[13.5px] text-[#8a8a8a]">{d.prompt}</p>
      <ChipRows
        rows={d.options}
        selected={d.selected}
        className="absolute inset-x-0 top-[252px] flex flex-col gap-[13px]"
        rowClassName="justify-center gap-[11px]"
        chipClassName={cn('h-[34px] bg-[#f3f3f3] px-[12px] text-[14px] font-medium text-[#222]')}
        selectedClassName="!bg-[#f8c443]"
      />
      <button
        type="button"
        className="absolute top-[416px] right-[17px] left-[17px] h-[49px] rounded-full bg-[#3e9f80] text-[19px] font-bold text-white"
        style={{ boxShadow: '0 3px 10px rgba(0,0,0,0.12)' }}
      >
        {d.action}
      </button>
    </SheetScreen>
  )
}
