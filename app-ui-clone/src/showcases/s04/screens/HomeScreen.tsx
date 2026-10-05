import { ArrowUpRight, Bell, Map, MapPin, TextAlignStart } from 'lucide-react'
import { SearchField } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { CategoryTile } from '../components/CategoryTile'
import { GlassButton } from '../components/GlassButton'
import { RestaurantCard } from '../components/RestaurantCard'
import { categories, home, navItems, restaurants } from '../data'
import { fonts, theme } from '../theme'

function PromoHeader() {
  return (
    <div
      className="absolute inset-x-0 top-0 h-[322px] overflow-hidden rounded-b-[30px]"
      style={{ background: `radial-gradient(ellipse 70% 60% at 50% 45%, #2a2b2d 0%, ${theme.headerDark} 60%, #1a1a1b 100%)` }}
    >
      <GlassButton icon={TextAlignStart} className="absolute left-[16px] top-[51px] bg-white/20" />
      <GlassButton icon={Bell} className="absolute right-[19px] top-[51px] bg-white/20" />

      <div className="absolute inset-x-0 top-[55px] text-center">
        <p className="text-[12.5px] text-[#a9a9a9]">{home.locationLabel}</p>
        <p className="-mt-[1px] flex items-center justify-center gap-[5px] text-[14.5px] font-medium text-white">
          <MapPin size={14} fill={theme.accent} color={theme.accent} className="[&>circle]:fill-[#222] [&>circle]:stroke-none" />
          {home.address}
        </p>
      </div>

      <div className="absolute left-[100px] top-[129px] flex items-center gap-[10px]">
        <span className={`${fonts.numeric} text-[50px] leading-none font-medium tracking-[-3px]`} style={{ color: theme.accent }}>
          {home.promoValue}
        </span>
        <span className="text-[20px] leading-[22px] text-white">
          <b className="block font-semibold">{home.promoLines[0]}</b>
          <span className="block">{home.promoLines[1]}</span>
        </span>
      </div>

      <p className="absolute inset-x-0 top-[179px] text-center text-[19.5px] leading-[23px] text-white">
        {home.promoCopy.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </p>

      <SearchField
        placeholder={home.searchPlaceholder}
        iconSize={20}
        iconStrokeWidth={1.8}
        className="absolute left-[16px] top-[263px] h-[47px] w-[287px] rounded-full bg-white pl-[17px] text-[#444]"
        textClassName="text-[14px] text-[#aaa]"
      />
      <div className="absolute left-[311px] top-[262px] flex h-[49px] w-[49px] items-center justify-center rounded-full bg-white">
        <Map size={20} strokeWidth={1.8} color={theme.accent} />
      </div>
    </div>
  )
}

export function HomeScreen() {
  return (
    <div className={`absolute inset-0 bg-white ${fonts.ui}`}>
      <PromoHeader />

      <div className="absolute left-[17px] top-[347px] flex gap-[13.5px]">
        {categories.map((c) => (
          <CategoryTile key={c.key} category={c} />
        ))}
      </div>

      <div className="absolute inset-x-[16px] top-[449px] flex items-center justify-between">
        <h2 className="text-[19.5px] font-medium text-[#141414]">{home.sectionTitle}</h2>
        <span className="flex h-[36px] w-[36px] items-center justify-center rounded-full border border-[#f2f2f2] bg-white">
          <ArrowUpRight size={20} strokeWidth={1.8} color={theme.accent} />
        </span>
      </div>

      <div className="absolute left-[18px] top-[494px] flex gap-[9px]">
        {restaurants.map((r) => (
          <RestaurantCard key={r.key} restaurant={r} />
        ))}
      </div>

      <BottomNav items={navItems} activeKey="home" fabKey="cart" />
    </div>
  )
}
