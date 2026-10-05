import { ArrowLeft, Check, Gem, Heart, Share } from 'lucide-react'
import { AppScreen, Avatar, Button, HomeIndicator, ImagePlaceholder, StatusBar, cn } from '../../../ui'
import { listing } from '../data'
import { Divider } from '../components/Divider'
import { FloatingIcon } from '../components/FloatingIcon'
import { ListingStats } from '../components/ListingStats'
import { FONT, palette as c } from '../theme'

export function ListingScreen() {
  return (
    <AppScreen className={cn(FONT)}>
      <ImagePlaceholder className="absolute inset-x-0 top-0" style={{ height: 372 }} tone="#b4b4bb" label="room photo" />
      <div className="relative">
        <StatusBar paddingX={34} paddingTop={18} fontSize={16} color="#fff" />
      </div>
      <FloatingIcon icon={ArrowLeft} className="top-[63px] left-[11px]" />
      <FloatingIcon icon={Share} className="top-[63px] left-[290px]" />
      <FloatingIcon icon={Heart} className="top-[63px] left-[337px]" />
      <span className="absolute top-[308px] left-[323px] rounded-[6px] bg-black/55 px-[7px] py-[3px] text-[11px] leading-[16px] font-semibold text-white">
        {listing.counter}
      </span>
      <div className="absolute inset-x-0 top-[347px] bottom-0 rounded-t-[22px] bg-white">
        <h1 className="mt-[22px] text-center text-[22px] leading-[30px] font-semibold tracking-[-0.3px]" style={{ color: c.text }}>
          {listing.title.map((t) => (
            <span key={t} className="block">
              {t}
            </span>
          ))}
        </h1>
        <p className="mt-[16px] text-center text-[13.5px] leading-[20px]" style={{ color: c.muted }}>
          {listing.subtitle.map((t) => (
            <span key={t} className="block">
              {t}
            </span>
          ))}
        </p>
        <div className="mt-[40px] flex pl-[10px]">
          <ListingStats rating={listing.rating} badge={listing.badge} reviews={listing.reviews} reviewsLabel={listing.reviewsLabel} />
        </div>
        <Divider className="mx-[22px] mt-[37px]" />
        <div className="flex items-center gap-[17px] px-[23px] py-[20.5px]">
          <Avatar
            size={40}
            badge={<span className="block h-[13px] w-[11px] rounded-[3px]" style={{ background: c.brand, boxShadow: '0 0 0 2px #fff' }} />}
          />
          <div>
            <div className="text-[13.5px] leading-[19px] font-medium" style={{ color: c.text }}>
              {listing.host.title}
            </div>
            <div className="text-[13px] leading-[19px]" style={{ color: c.muted }}>
              {listing.host.sub}
            </div>
          </div>
        </div>
        <Divider className="mx-[22px]" />
        <div className="mt-[16px] flex h-[35px] items-center justify-center gap-[7px] bg-[#f0f0f0] text-[11.5px] font-medium" style={{ color: c.text }}>
          <Gem size={12} strokeWidth={2} />
          {listing.rare}
        </div>
      </div>
      <div className="absolute top-[747px] left-[23px]" style={{ color: c.text }}>
        <div className="text-[16px] leading-[22px] font-semibold underline underline-offset-2">{listing.price}</div>
        <div className="mt-[4px] text-[11.5px] leading-[14px]" style={{ color: c.muted }}>
          {listing.priceSub}
        </div>
      </div>
      <span
        className="absolute top-[792px] left-[16px] flex h-[22px] items-center gap-[5px] rounded-full px-[9px] text-[11.5px]"
        style={{ background: c.chip, color: c.text }}
      >
        <Check size={11} strokeWidth={2.6} />
        {listing.freeCancel}
      </span>
      <Button
        className="absolute top-[754px] left-[222px] h-[49px] w-[143px] rounded-full text-[14.5px] font-semibold text-white"
        style={{ background: '#d70a63' }}
      >
        {listing.cta}
      </Button>
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
