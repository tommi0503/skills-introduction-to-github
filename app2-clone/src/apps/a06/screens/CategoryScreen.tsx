import { ArrowDownUp, ArrowLeft, ChevronDown, Info, MapPin, RotateCw, Search, Star, Utensils, Zap } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { category, navItems, shops } from '../data'
import { theme } from '../theme'
import { BottomNav } from '../components/BottomNav'
import { CartButton } from '../components/CartButton'
import { Chrome } from '../components/Chrome'
import { ClubBadge } from '../components/ClubBadge'
import { DeliveryInfo } from '../components/DeliveryInfo'
import { FilterChips, type FilterChipData } from '../components/FilterChips'
import { MenuStrip } from '../components/MenuStrip'
import { Tag } from '../components/Tag'
import { UnderlineTabs } from '../components/UnderlineTabs'

const filters: FilterChipData[] = [
  { key: 'sort', label: '주문 많은 순', icon: ArrowDownUp },
  { key: 'reset', label: '초기화', icon: RotateCw },
  { key: 'club', label: '배민클럽', club: true, active: true },
  { key: 'instant', label: '즉시할인·쿠폰', icon: Zap },
]

export function CategoryScreen() {
  const [first, second] = shops
  return (
    <AppScreen className="font-pretendard">
      <ArrowLeft size={24} strokeWidth={1.9} className="absolute left-[25px] top-[70px]" />
      <p className="absolute left-[72px] top-[69px] flex items-center gap-[3px] text-[20px] font-extrabold tracking-[-0.6px] text-[#111]">
        {category.title}
        <Utensils size={18} color="#2ec9b6" strokeWidth={2.6} />
      </p>
      <div className="absolute right-[26px] top-[70px] flex items-center gap-[16px]">
        <ClubBadge />
        <Search size={23} strokeWidth={2} />
        <CartButton count={category.cartCount} />
      </div>
      <UnderlineTabs
        items={category.tabs}
        active={category.active}
        gap={19}
        className="absolute inset-x-0 top-[112px] h-[39px] pl-[21px]"
        itemClassName="text-[16px] tracking-[-0.3px]"
        activeClassName="font-bold text-[#111]"
        inactiveClassName="text-[#9a9da2]"
      />
      <span className="absolute left-[350px] top-[115px] flex h-[32px] w-[32px] items-center justify-center rounded-full border border-[#e2e4e7] bg-white">
        <ChevronDown size={18} strokeWidth={2} />
      </span>
      <FilterChips items={filters} className="absolute left-[-5px] top-[163px]" />
      <p className="absolute left-[15px] top-[218px] flex items-center gap-[3px] text-[12px] font-medium text-[#333]">
        {category.sortLabel}
        <Info size={12} strokeWidth={1.6} color="#999" />
      </p>

      <MenuStrip menus={first.menus} discount={first.discount} className="absolute left-[16px] top-[248px] w-[400px]" />
      <div className="absolute left-[15px] right-[20px] top-[416px] flex items-center justify-between">
        <p className="flex items-center gap-[3px] text-[16px] tracking-[-0.4px]">
          <b className="font-bold text-[#111]">{first.name}</b>
          <Star size={14} fill={theme.star} color={theme.star} className="ml-[3px]" />
          <b className="text-[13px] font-bold">{first.rating}</b>
          <span className="text-[13px] text-[#8a8d92]">{first.reviews}</span>
        </p>
        <span className="flex items-center gap-[2px] text-[10.5px] text-[#a6a9ad]">
          광고 <Info size={10} />
        </span>
      </div>
      <DeliveryInfo
        eta={first.eta}
        etaIcon="blue"
        className="absolute left-[15px] top-[440px] h-[20px] text-[13px]"
        extra={
          <>
            <MapPin size={14} strokeWidth={1.8} className="ml-[10px] mr-[2px]" color="#444" />
            <span className="text-[#333]">{first.distance}</span>
            <span className="ml-[6px] text-[#8a8d92]">최소주문</span>
            <span className="ml-[3px] text-[#333]">{first.minOrder}</span>
          </>
        }
      />
      <div className="absolute left-[15px] top-[464px] flex gap-[4px] whitespace-nowrap">
        {first.tags.map((t) => (
          <Tag key={t.label} tag={t} />
        ))}
      </div>
      <div className="absolute inset-x-0 top-[494px] h-[8px]" style={{ background: theme.band }} />
      <div className="absolute left-[16px] right-[15px] top-[513px] h-[50px] overflow-hidden rounded-[12px]" style={{ background: theme.mint }}>
        <p className="absolute left-[21px] top-[14px] text-[16.5px] font-bold tracking-[-0.5px] text-[#111]">{category.coupon}</p>
        <ImagePlaceholder label="coupon illustration" tone="#fbf6e9" className="absolute left-[246px] top-[-6px] h-[62px] w-[82px] rounded-[30px]" />
      </div>
      <div className="absolute inset-x-0 top-[576px] h-[8px]" style={{ background: theme.band }} />
      <MenuStrip menus={second.menus} discount={second.discount} className="absolute left-[16px] top-[594px] w-[400px]" />
      <p className="absolute left-[15px] top-[764px] text-[16px] font-bold tracking-[-0.4px] text-[#111]">{second.name}</p>
      <BottomNav items={navItems} activeKey="home" className="top-[769px]" />
      <Chrome />
    </AppScreen>
  )
}
