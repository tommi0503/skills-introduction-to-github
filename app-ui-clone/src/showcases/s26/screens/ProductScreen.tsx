import { House, Handbag } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { CtaButton, NavBar } from '../components/Primitives'
import { product } from '../data'

export function ProductScreen() {
  return (
    <div className="relative h-full overflow-hidden bg-white font-pretendard">
      <HighlightStatusBar />
      <NavBar actions={[House, Handbag]} />

      <ImagePlaceholder label="product package" className="absolute" style={{ left: 112.5, top: 154.4, width: 169.5, height: 315.6 }} />

      <div className="absolute" style={{ left: 16.6, top: 549 }}>
        <p className="text-[17px] leading-[24px] font-semibold text-[#1a1a1a]">{product.name}</p>
        <p className="mt-[1px] flex items-baseline font-bold text-[#1a1a1a]">
          <span className="text-[33px] leading-[40px]" style={{ letterSpacing: -0.5 }}>
            {product.price}
          </span>
          <span className="ml-[1px] text-[19px]">{product.currency}</span>
        </p>
      </div>

      <div className="absolute grid grid-cols-2" style={{ left: 16.6, right: 16, top: 644 }}>
        {product.methods.map((m) => (
          <span key={m} className="flex items-center gap-[6px] text-[12.5px] text-[#333]">
            <span className="h-[3px] w-[3px] rounded-full bg-[#333]" />
            {m}
          </span>
        ))}
      </div>

      <div className="absolute inset-x-0 h-[16px] bg-[#f7f7f7]" style={{ top: 695 }} />

      <CtaButton className="absolute" style={{ left: 16, right: 15, top: 754.8 }}>
        {product.cta}
      </CtaButton>
    </div>
  )
}
