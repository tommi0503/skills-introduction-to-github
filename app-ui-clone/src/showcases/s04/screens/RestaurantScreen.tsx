import { Bike, ChevronLeft, PersonStanding, Heart, Share2 } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { GlassButton } from '../components/GlassButton'
import { OfferCard } from '../components/OfferCard'
import { ProductCard } from '../components/ProductCard'
import { Rating } from '../components/Rating'
import { UnderlineTabs } from '../components/UnderlineTabs'
import { menuTabs, offers, products, restaurantDetail as d } from '../data'
import { fonts, theme } from '../theme'

function DeliveryInfo() {
  return (
    <div className="absolute left-[13px] top-[283px] flex h-[61px] w-[347px] items-center rounded-full bg-[#f7f7f7] pl-[12px]">
      <div className="flex h-[44px] items-center gap-[12px] rounded-full bg-white pr-[14px] pl-[5px]">
        <span className="flex h-[32px] w-[32px] items-center justify-center rounded-full text-white" style={{ background: theme.accent }}>
          <Bike size={17} strokeWidth={2} />
        </span>
        <PersonStanding size={17} strokeWidth={2} className="text-[#1c1c1c]" />
      </div>
      <div className="ml-[14px] leading-[19px]">
        <p className="text-[14.5px] font-semibold text-[#1c1c1c]">{d.deliveryTitle}</p>
        <p className="flex items-center gap-[5px] text-[14px] text-[#9a9a9a]">
          {d.deliveryMeta[0]}
          <span className="text-[9px]">•</span>
          {d.deliveryMeta[1]}
        </p>
      </div>
    </div>
  )
}

export function RestaurantScreen() {
  return (
    <div className={`absolute inset-0 bg-white ${fonts.ui}`}>
      <ImagePlaceholder label="restaurant banner photo" tone="#c4c8ce" className="absolute inset-x-0 top-0 h-[178px]" />
      <GlassButton icon={ChevronLeft} size={44} className="absolute left-[14px] top-[50px] bg-white/30" />
      <GlassButton icon={Heart} size={44} className="absolute left-[264px] top-[50px] bg-white/30" />
      <GlassButton icon={Share2} size={44} className="absolute left-[315px] top-[50px] bg-white/30" />

      <div className="absolute left-[151px] top-[149px] h-[58px] w-[58px] rounded-full bg-white p-[2px]">
        <ImagePlaceholder label="McDonald's logo" className="h-full w-full rounded-full" />
      </div>

      <div className="absolute left-0 top-[220px] w-[360px] text-center">
        <h2 className="text-[20px] font-medium text-[#141414]">{d.name}</h2>
        <p className="mt-0 flex items-center justify-center gap-[5px] text-[13.5px] text-[#9a9a9a]">
          <Rating value={d.rating} count={d.reviews} size={13} />
          <span className="text-[9px]">•</span>
          <span style={{ color: theme.accent }}>{d.tier}</span>
          <span className="text-[9px]">•</span>
          <span>{d.distance}</span>
        </p>
      </div>

      <DeliveryInfo />

      <div className="absolute left-[13px] top-[359px] flex gap-[12px]">
        {offers.map((o) => (
          <OfferCard key={o.key} offer={o} />
        ))}
      </div>

      <UnderlineTabs tabs={menuTabs} active="Popular" className="absolute inset-x-[14px] top-[467px] gap-[30px]" />

      <div className="absolute left-[14px] top-[513px] grid grid-cols-2 gap-x-[14px] gap-y-[11px]">
        {products.map((p) => (
          <ProductCard key={p.key} product={p} />
        ))}
      </div>
    </div>
  )
}
