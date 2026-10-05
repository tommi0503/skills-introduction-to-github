import { ImagePlaceholder } from '../../../ui'
import { BottomFade } from '../components/BottomFade'
import { BrandHeader } from '../components/BrandHeader'
import { CarouselCard } from '../components/CarouselCard'
import { FloatingNav } from '../components/FloatingNav'
import { HeroCopy } from '../components/HeroCopy'
import { brand, carousel, hero, navTabs } from '../data'

/** Rentique home: full-bleed hero photo, arrivals carousel and floating nav. */
export function HomeScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white">
      <ImagePlaceholder className="absolute inset-x-0 top-0 h-[492px]" tone="#c3c8ce" label="hero photo" />
      <div className="absolute inset-x-[17px] top-[58px]">
        <BrandHeader {...brand} />
      </div>
      <div className="absolute left-[26px] top-[305px]">
        <HeroCopy {...hero} />
      </div>
      <div className="absolute left-[-43px] top-[448px] flex gap-[11px]">
        {carousel.map((p) => (
          <CarouselCard key={p.id} product={p} />
        ))}
      </div>
      <div className="absolute left-[19px] top-[740px] text-[19px] font-semibold text-[#1c1c1c]">Featured</div>
      <div className="absolute left-[19px] top-[784px] flex gap-[11px]">
        <ImagePlaceholder className="h-[120px] w-[164px] rounded-[6px]" />
        <ImagePlaceholder className="h-[120px] w-[164px] rounded-[6px]" />
      </div>
      <BottomFade height={100} />
      <div className="absolute left-[27px] top-[727px] z-40">
        <FloatingNav items={navTabs} activeKey="home" />
      </div>
    </div>
  )
}
