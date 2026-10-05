import { ChevronLeft, ChevronRight, EllipsisVertical, Heart, House, Share } from 'lucide-react'
import { AppScreen, Avatar, ImagePlaceholder } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { EmojiGlyph } from '../components/EmojiGlyph'
import { MannerTemp } from '../components/MannerTemp'
import { article, seller } from '../data'
import { kr } from '../theme'

function PhotoHeader() {
  return (
    <div className="absolute inset-x-0 top-0 h-[390px]">
      <ImagePlaceholder tone={kr.photoUnderWhite} className="h-full w-full" label="product photo" />
      <div className="absolute inset-x-0 top-[62px] flex items-center pr-[12px] pl-[14px] text-white">
        <ChevronLeft size={26} strokeWidth={1.8} />
        <House size={23} strokeWidth={1.8} className="ml-[13px]" />
        <Share size={21} strokeWidth={1.8} className="mr-[30px] ml-auto" />
        <EllipsisVertical size={20} strokeWidth={2.2} />
      </div>
    </div>
  )
}

function SellerRow() {
  return (
    <div className="absolute inset-x-[15px] top-[406px] flex h-[63px] items-start border-b pb-[10px]" style={{ borderColor: kr.line }}>
      <Avatar size={47} />
      <div className="ml-[9px] flex-1 pt-[2px]">
        <p className="text-[14.5px] font-bold">{seller.name}</p>
        <p className="mt-[6px] text-[12.5px]" style={{ color: kr.sub }}>
          {seller.town}
        </p>
      </div>
      <MannerTemp value={seller.temp} level={seller.tempLevel} label={seller.tempLabel} />
    </div>
  )
}

function Article() {
  return (
    <div className="absolute inset-x-[15px] top-[482px]">
      <h2 className="pr-[14px] text-[19.5px] leading-[28px] font-bold tracking-[-0.2px]">
        <EmojiGlyph size={20} className="mr-[6px]" />
        {article.title}
      </h2>
      <p className="mt-[10px] text-[12.5px]" style={{ color: kr.faint }}>
        <span className="underline">{article.category}</span> · {article.meta}
      </p>
      <div className="mt-[22px] text-[16px] leading-[24px]">
        {article.body.map((line) => (
          <div key={line.text}>
            {line.text}
            {Array.from({ length: line.emoji ?? 0 }, (_, i) => (
              <EmojiGlyph key={i} round size={20} className="ml-[2px]" />
            ))}
          </div>
        ))}
      </div>
      <div className="mt-[13px] flex items-center justify-between text-[15px]">
        <span className="font-bold">{article.placeLabel}</span>
        <span className="flex items-center gap-[2px]" style={{ color: '#4d5159' }}>
          {article.place}
          <ChevronRight size={18} strokeWidth={1.8} />
        </span>
      </div>
      <ImagePlaceholder className="mt-[12px] h-[24px] w-full rounded-[4px]" label="map" />
    </div>
  )
}

function PurchaseBar() {
  return (
    <div className="absolute inset-x-0 top-[742px] bottom-0 flex items-start border-t bg-white px-[16px] pt-[16px]" style={{ borderColor: kr.line }}>
      <Heart size={24} strokeWidth={1.6} className="mt-[7px] text-[#4d5159]" />
      <span className="mx-[16px] h-[44px] w-px" style={{ background: kr.line }} />
      <div className="-mt-[5px] flex-1">
        <div className="flex items-center gap-[10px]">
          <span className="text-[15.5px] font-bold">{article.price}</span>
          <ImagePlaceholder className="h-[18px] w-[42px] rounded-[3px]" label="pay logo" />
        </div>
        <p className="mt-[7px] text-[12.5px]" style={{ color: kr.sub }}>
          {article.priceNote}
        </p>
      </div>
      <span className="flex h-[38px] w-[80px] items-center justify-center rounded-[6px] text-[14px] font-bold text-white" style={{ background: kr.orange }}>
        {article.cta}
      </span>
    </div>
  )
}

/** Listing detail: hero photo, seller + manner temperature, description and purchase bar. */
export function DetailScreen() {
  return (
    <AppScreen className="font-pretendard" style={{ color: kr.text }}>
      <PhotoHeader />
      <Chrome />
      <SellerRow />
      <Article />
      <PurchaseBar />
    </AppScreen>
  )
}
