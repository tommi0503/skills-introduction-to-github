import { Camera, ChevronLeft } from 'lucide-react'
import { AppScreen, HomeIndicator, ImagePlaceholder } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { ProductCard } from '../components/ProductCard'
import { similar } from '../data'
import { theme } from '../theme'

const hotspots = [
  { x: 132, y: 164 },
  { x: 240, y: 310 },
]

export function LensScreen() {
  return (
    <AppScreen background={theme.lensBg} className="font-pretendard">
      <PhoneStatus color="#8a8a8a" />
      <ChevronLeft size={26} strokeWidth={1.6} color="#dcdcdc" className="absolute top-[56px] left-[13px]" />
      <span className="absolute inset-x-0 top-[59px] text-center text-[15px] font-semibold text-[#dcdcdc]">직잭 렌즈</span>
      <Camera size={23} strokeWidth={1.7} color="#dcdcdc" className="absolute top-[57px] right-[17px]" />
      <ImagePlaceholder tone="#7c7c7c" label="flat-lay outfit photo" className="absolute top-[98px] left-[84px] h-[391px] w-[220px]" />
      <div className="absolute top-[221px] left-[95px] h-[190px] w-[98px] rounded-[8px] border-[3px] border-white">
        <ImagePlaceholder label="selected skirt" className="h-full w-full rounded-[5px]" />
      </div>
      {hotspots.map((p) => (
        <span key={p.x} className="absolute h-[16px] w-[16px] rounded-full border-[4px] border-white" style={{ left: p.x, top: p.y }} />
      ))}
      <div className="absolute inset-x-0 top-[489px] bottom-0 overflow-hidden rounded-t-[18px] bg-white">
        <span className="absolute top-[8px] left-[175px] h-[4px] w-[40px] rounded-full bg-[#d0d0d4]" />
        <h3 className="absolute top-[32px] left-[15px] text-[16.5px] font-semibold text-[#111]">이미지와 비슷한 상품</h3>
        <div className="absolute top-[71px] left-0 flex gap-[2px]">
          {similar.map((p) => (
            <ProductCard key={p.key} product={p} width={128.7} imageHeight={154} textInset={8} />
          ))}
        </div>
        <div className="absolute top-[337px] left-0 flex gap-[2px]">
          {similar.map((p) => (
            <ImagePlaceholder key={p.key} label="product photo" className="h-[60px] w-[128.7px]" />
          ))}
        </div>
      </div>
      <HomeIndicator width={140} bottom={6} />
    </AppScreen>
  )
}
