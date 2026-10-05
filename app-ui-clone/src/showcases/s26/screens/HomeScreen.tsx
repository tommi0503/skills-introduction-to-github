import { Bell, ChevronRight, ShoppingBag } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { CuTabBar } from '../components/CuTabBar'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import {
  BenefitBadge,
  KeepingTileView,
  OutlinePill,
  SectionHeading,
  ServiceTileView,
  TrendingSearch,
} from '../components/HomeBlocks'
import { cuTabs, heroBanner, homeHeader, homeSections, keepingTile, popupTeaser, searchSuggestion, serviceTiles } from '../data'
import { cu } from '../theme'

function HeroBanner() {
  return (
    <div className="absolute overflow-hidden rounded-[18px]" style={{ left: 15.3, top: 293, width: 361.7, height: 160.3, background: cu.banner }}>
      <div className="absolute" style={{ left: 23, top: 22 }}>
        {heroBanner.title.map((l) => (
          <p key={l} className="text-[22px] leading-[29px] font-bold text-[#1d2a12]">
            {l}
          </p>
        ))}
        <div className="mt-[4px]">
          {heroBanner.body.map((l) => (
            <p key={l} className="text-[14.6px] leading-[21px] text-[#2d4a1d]">
              {l}
            </p>
          ))}
        </div>
      </div>
      <ImagePlaceholder label="flash popup illustration" className="absolute rounded-[12px]" style={{ left: 192, top: 9, width: 154, height: 122 }} />
      <div
        className="absolute flex h-[22px] items-center gap-[3px] rounded-full px-[9px] text-[12.5px] font-semibold text-white"
        style={{ left: 290.7, top: 124, background: 'rgba(30,50,20,0.55)' }}
      >
        {heroBanner.page}
        <span className="ml-[2px] text-[15px] leading-none font-normal">+</span>
      </div>
    </div>
  )
}

export function HomeScreen() {
  const large = serviceTiles.filter((t) => t.size === 'large')
  const small = serviceTiles.filter((t) => t.size === 'small')
  return (
    <div className="relative h-full overflow-hidden bg-white font-pretendard">
      <div className="absolute inset-x-0 top-0 h-[210px]" style={{ background: cu.headerWash }} />
      <HighlightStatusBar chipColor="#a4968b" />

      <ImagePlaceholder label="bread illustration" tone="#efd3c1" className="absolute rounded-l-[20px]" style={{ left: 252, top: 98.6, width: 141, height: 79.4 }} />
      <div className="absolute flex items-center gap-[14px]" style={{ left: 264, top: 68 }}>
        <BenefitBadge label={homeHeader.benefitBadge} />
        <Bell size={27} strokeWidth={1.4} className="text-[#222]" />
        <ShoppingBag size={28} strokeWidth={1.4} className="text-[#222]" />
      </div>
      <div className="absolute text-[20px] leading-[29px] font-semibold text-[#2a2a2a]" style={{ left: 25, top: 99.5, letterSpacing: -0.3 }}>
        <p>{homeHeader.promoTitle}</p>
        <p className="flex items-center">
          {homeHeader.promoBody}
          <ChevronRight size={20} strokeWidth={2} className="ml-[2px]" />
        </p>
      </div>

      <div className="absolute" style={{ left: 15.3, top: 176, width: 361.7 }}>
        <TrendingSearch {...searchSuggestion} />
      </div>

      <div className="absolute flex items-center" style={{ left: 24.8, right: 22, top: 235.6 }}>
        <ImagePlaceholder label="flash popup thumbnail" tone="#e8f3dc" className="h-[39px] w-[39px] rounded-full" />
        <div className="ml-[11px] flex-1">
          <p className="text-[12.5px] leading-[17px] text-[#8a8a8a]">{popupTeaser.caption}</p>
          <p className="text-[16px] leading-[21px] font-bold text-[#1a1a1a]">{popupTeaser.title}</p>
        </div>
        <ChevronRight size={18} strokeWidth={1.6} className="text-[#999]" />
      </div>

      <HeroBanner />

      <div className="absolute flex gap-[10.7px]" style={{ left: 15.3, top: 466, width: 361.7 }}>
        <div className="flex w-[214px] flex-col gap-[7.5px]">
          <div className="grid grid-cols-2 gap-[10.3px]">
            {large.map((t) => (
              <ServiceTileView key={t.key} tile={t} />
            ))}
          </div>
          <div className="grid grid-cols-3 gap-[11.5px]">
            {small.map((t) => (
              <ServiceTileView key={t.key} tile={t} />
            ))}
          </div>
        </div>
        <div className="flex-1">
          <KeepingTileView {...keepingTile} />
        </div>
      </div>

      <div className="absolute inset-x-0 bottom-0" style={{ top: 637.7, background: '#f9f9f9' }}>
        <div className="flex items-center justify-between pr-[16.5px] pl-[23.5px]" style={{ marginTop: 22 }}>
          <SectionHeading>{homeSections.favoriteStore}</SectionHeading>
          <OutlinePill label={homeSections.favoriteCta} />
        </div>
        <div className="absolute rounded-[18px] bg-white" style={{ left: 16.4, right: 16.4, top: 75, height: 120 }}>
          <SectionHeading className="absolute top-[22px] left-[20px]">{homeSections.services}</SectionHeading>
        </div>
      </div>

      <CuTabBar tabs={cuTabs} active="home" />
    </div>
  )
}
