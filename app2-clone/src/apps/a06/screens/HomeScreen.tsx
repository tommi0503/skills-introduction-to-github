import { Bell, ChevronRight, Info, Search, ShoppingCart } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { brands, home, navItems, serviceGrid } from '../data'
import { theme } from '../theme'
import { BottomNav } from '../components/BottomNav'
import { BrandRail } from '../components/BrandRail'
import { Chrome } from '../components/Chrome'
import { ClubBadge } from '../components/ClubBadge'
import { DiscountBar } from '../components/DiscountBar'
import { ServiceGrid } from '../components/ServiceGrid'
import { UnderlineTabs } from '../components/UnderlineTabs'

export function HomeScreen() {
  return (
    <AppScreen className="font-pretendard" background={theme.mint}>
      {/* header on mint */}
      <ImagePlaceholder label="address (blurred)" tone="#9ff5e6" className="absolute left-[15px] top-[60px] h-[26px] w-[108px] rounded-[4px]" />
      <span className="absolute left-[124px] top-[72px] h-0 w-0 border-x-[4px] border-t-[5px] border-x-transparent border-t-[#222]" />
      <div className="absolute right-[13px] top-[63px] flex items-center gap-[17px]">
        <ClubBadge />
        <Bell size={23} strokeWidth={1.9} />
        <ShoppingCart size={24} strokeWidth={1.9} />
      </div>
      <div className="absolute left-[16px] right-[17px] top-[98px] flex h-[40px] items-center justify-between rounded-full border-[1.5px] border-[#1d1d1d] bg-white pl-[16px] pr-[14px]">
        <span className="text-[13.5px] text-[#8b8e93]">{home.searchPlaceholder}</span>
        <Search size={19} strokeWidth={2.2} />
      </div>
      <div className="absolute left-[17px] top-[153px] text-[15.5px] font-bold leading-[24px] text-[#111]">
        {home.promo.lines.map((l) => (
          <p key={l}>{l}</p>
        ))}
      </div>
      <div className="absolute left-[17px] top-[207px] flex h-[24px] items-center gap-[3px] rounded-[5px] bg-[#1b1b1f] px-[10px] text-[11.5px] font-semibold tracking-[-0.3px] text-white">
        {home.promo.cta}
        <ChevronRight size={12} strokeWidth={2.4} />
      </div>
      <ImagePlaceholder label="coupon pouch illustration" tone="#b9f7ea" className="absolute left-[256px] top-[146px] h-[112px] w-[120px] rounded-[40px]" />

      {/* white sheet */}
      <div className="absolute inset-x-0 top-[258px] bottom-0 rounded-t-[16px] bg-white">
        <UnderlineTabs
          items={home.tabs}
          active={home.tabs[0]}
          gap={16}
          className="h-[50px] pl-[17px]"
          itemClassName="text-[17px] tracking-[-0.4px]"
          activeClassName="font-bold text-[#111]"
          inactiveClassName="text-[#333]"
        />
        <ServiceGrid rows={serviceGrid} className="absolute left-[11px] top-[67px]" />
        <p className="absolute inset-x-0 top-[267px] flex items-center justify-center text-[13.5px] tracking-[-0.3px] text-[#222]">
          <b className="font-bold">{home.more.strong}</b>
          {home.more.rest}
          <ChevronRight size={14} strokeWidth={2} className="ml-[5px]" />
        </p>
        <div className="absolute inset-x-0 top-[292px] h-[10px]" style={{ background: theme.band }} />
        <BrandRail items={brands} className="absolute left-[15px] top-[317px]" />
        <div className="absolute inset-x-0 top-[411px] h-[10px]" style={{ background: theme.band }} />
        <p className="absolute left-[16px] top-[436px] flex items-center gap-[5px] text-[18px] font-bold tracking-[-0.5px] text-[#111]">
          {home.sectionTitle}
          <Info size={15} strokeWidth={1.6} color="#aaa" />
        </p>
        {[16, 214].map((x) => (
          <div key={x} className="absolute top-[475px] h-[122px] w-[188px] overflow-hidden rounded-[8px]" style={{ left: x }}>
            <ImagePlaceholder label="store photo" className="h-full w-full" />
            <DiscountBar label="2,000원 즉시할인" size="md" className="absolute inset-x-0 bottom-0 h-[20px]" />
          </div>
        ))}
      </div>
      <BottomNav items={navItems} activeKey="home" className="top-[763px]" />
      <Chrome chipClassName="!bg-[#6aa79b]/90" />
    </AppScreen>
  )
}
