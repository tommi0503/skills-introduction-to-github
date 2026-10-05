import { ChevronLeft, Ellipsis, Maximize2, PictureInPicture2, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Quote } from '../data'
import { ChangeLine } from './ChangeLine'
import { FloatingPill } from './FloatingPill'
import { TopBar } from './TopBar'

export interface AssetHeaderProps {
  ticker: string
  name: string
  quote: Quote
  starred?: boolean
}

/** Crypto asset header: artwork band, floating nav pills, name and live quote. */
export function AssetHeader({ ticker, name, quote, starred }: AssetHeaderProps) {
  return (
    <>
      <ImagePlaceholder className="absolute inset-x-0 top-0 h-[239px] border-b border-[#e3e3e5]" label="circuit artwork" />
      <TopBar />
      <FloatingPill left={14} top={58} height={44} width={44}>
        <ChevronLeft size={20} strokeWidth={2.2} />
      </FloatingPill>
      <span className="absolute text-[14px] font-semibold" style={{ left: 78, top: 72 }}>
        {ticker}
      </span>
      <FloatingPill left={226} top={59} height={42} width={147} className="justify-between px-[16px]">
        <PictureInPicture2 size={17} strokeWidth={2.1} />
        <Star size={17} strokeWidth={2.1} fill={starred ? '#111' : 'none'} />
        <Ellipsis size={18} strokeWidth={2.6} />
      </FloatingPill>
      <ImagePlaceholder tone="#cfd2d8" className="absolute rounded-full" style={{ left: 15, top: 136, width: 31, height: 31 }} label="bitcoin icon" />
      <ImagePlaceholder tone="#cfd2d8" className="absolute rounded-[4px]" style={{ left: 304, top: 139, width: 69, height: 24 }} label="public logo" />
      <div className="absolute text-[28px] font-semibold tracking-[-0.4px]" style={{ left: 15, top: 185 }}>
        {name}
      </div>
      <div className="absolute text-[23px] font-semibold tracking-[-0.3px]" style={{ left: 15, top: 257 }}>
        {quote.price}
      </div>
      <span className="absolute flex h-[30px] w-[30px] items-center justify-center rounded-full border border-[#e8e8ea] text-[#9a9aa0]" style={{ left: 341, top: 256 }}>
        <Maximize2 size={13} strokeWidth={1.8} />
      </span>
      <ChangeLine value={quote.change} top={294} className="[&>span:last-of-type]:text-[#111]" />
    </>
  )
}
