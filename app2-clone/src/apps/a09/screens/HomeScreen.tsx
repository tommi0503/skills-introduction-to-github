import { Search } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { home } from '../data'
import { fv } from '../theme'
import { FvStatusBar } from '../components/FvStatusBar'
import { DotGrid } from '../components/DotGrid'
import { SectionHeader } from '../components/SectionHeader'
import { ServiceCard } from '../components/ServiceCard'
import { OfferCard } from '../components/OfferCard'
import { FiverrTabBar } from '../components/FiverrTabBar'

export function HomeScreen() {
  const order = home.orders.items[0]
  return (
    <AppScreen background={fv.canvas} className="font-figtree">
      <div className="absolute inset-x-0 top-0 h-[166px]" style={{ background: fv.header }} />
      <FvStatusBar />
      <ImagePlaceholder label="fiverr logo" className="absolute top-[75px] left-[155px] h-[26px] w-[80px] rounded-[3px]" />
      <DotGrid className="absolute top-[75px] right-[19px] text-[#222]" />
      <div
        className="absolute top-[115px] left-[16px] flex h-[38px] w-[356px] items-center justify-center gap-[7px] rounded-[7px] bg-white text-[15.5px] text-[#74767e]"
        style={{ boxShadow: '0 2px 6px rgba(0,0,0,0.06)' }}
      >
        <Search size={16} strokeWidth={2} />
        {home.search}
      </div>

      <SectionHeader title={home.popular.title} action={home.seeAll} className="absolute inset-x-0 top-[180px]" />
      <div className="absolute top-[220px] left-[15px] flex gap-[10px]">
        {home.popular.items.map((s) => (
          <ServiceCard key={s} label={s} />
        ))}
      </div>

      <SectionHeader title={home.offers.title} action={home.seeAll} className="absolute inset-x-0 top-[415px]" />
      <div className="absolute top-[450px] left-[16px] flex gap-[11px]">
        {home.offers.items.map((o, i) => (
          <OfferCard key={i} offer={o} />
        ))}
      </div>

      <SectionHeader title={home.orders.title} action={home.seeAll} className="absolute inset-x-0 top-[678px]" />
      <div className="absolute top-[714px] left-[16px] flex h-[120px] w-[356px] gap-[11px] rounded-[8px] bg-white px-[9px] pt-[10px]">
        <ImagePlaceholder label="gig thumbnail" className="h-[59px] w-[79px] rounded-[2px]" />
        <div>
          <div className="text-[15px] font-semibold text-[#222325]">{order.price}</div>
          <p className="mt-[8px] text-[14px] leading-[17px] text-[#62646a]">{order.title}</p>
        </div>
      </div>
      <FiverrTabBar active="home" showBadges />
    </AppScreen>
  )
}
