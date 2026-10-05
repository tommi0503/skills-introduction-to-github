import { ChevronRight, CircleHelp, Ellipsis, Globe, Heart, MapPin, Plus, Search, Star, ThumbsUp, Trophy, UserRoundPlus, X, type LucideIcon } from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { Pill } from '../components/Pill'
import { SectionHeader } from '../components/SectionHeader'
import { Tag } from '../components/Tag'
import { store } from '../data'
import { ue } from '../theme'

function HeroButton({ icon: Icon, x }: { icon: LucideIcon; x: number }) {
  return (
    <span
      className="absolute top-[72px] flex h-[46px] w-[46px] items-center justify-center rounded-full text-white"
      style={{ left: x, background: 'rgba(60,60,60,0.45)' }}
    >
      <Icon size={20} strokeWidth={1.8} />
    </span>
  )
}

export function StoreScreen() {
  const d = store.deal
  return (
    <AppScreen className="font-inter" background="#fff">
      <ImagePlaceholder className="absolute inset-x-0 top-0 h-[193px]" label="restaurant banner" />
      <div className="absolute inset-x-0 top-0">
        <StatusBar />
      </div>
      <HeroButton icon={X} x={10} />
      <HeroButton icon={Search} x={224} />
      <HeroButton icon={Heart} x={280} />
      <HeroButton icon={Ellipsis} x={335} />
      <div className="absolute top-[174px] left-[164px] flex h-[63px] w-[63px] items-center justify-center rounded-full bg-white shadow-[0_1px_8px_rgba(0,0,0,0.12)]">
        <ImagePlaceholder className="h-[42px] w-[42px] rounded-[6px]" label="brand logo" />
      </div>

      <div className="absolute inset-x-0 top-[243px] flex flex-col items-center">
        <h1 className="text-[20px] leading-[28px] font-semibold tracking-[-0.3px]">{store.name}</h1>
        <div className="mt-[1px] flex items-center gap-[3px] text-[12.5px]">
          <span>{store.rating}</span>
          <Star size={12} fill="#000" />
          <span style={{ color: ue.muted }}>{store.reviews} ·</span>
          <Globe size={12} strokeWidth={2.2} color={ue.teal} />
          <span className="font-medium" style={{ color: ue.teal }}>
            {store.membership}
          </span>
          <span style={{ color: ue.muted }}>· {store.distance}</span>
          <ChevronRight size={10} strokeWidth={2.2} color={ue.muted} />
        </div>
        <div className="mt-[2px] flex items-center gap-[3px] text-[12.5px]" style={{ color: ue.muted }}>
          <MapPin size={12} strokeWidth={1.8} />
          {store.address}
        </div>
        <Tag className="mt-[4px] h-[26px] px-[7px] text-[12.5px] font-medium" style={{ background: ue.greenBg, color: ue.green }}>
          {store.social}
        </Tag>
      </div>

      <div className="absolute inset-x-[17px] top-[355px] flex items-center justify-between">
        <div className="flex h-[36px] items-center rounded-full p-[3px]" style={{ background: ue.field }}>
          {store.modes.map((m) => (
            <span
              key={m}
              className="flex h-full items-center rounded-full px-[13px] text-[12.5px]"
              style={m === store.activeMode ? { background: '#fff', fontWeight: 600 } : { color: ue.muted, fontWeight: 500 }}
            >
              {m}
            </span>
          ))}
        </div>
        <Pill className="h-[36px] gap-[6px] px-[13px] text-[12.5px] font-semibold" style={{ background: ue.field }} leading={<UserRoundPlus size={14} strokeWidth={1.8} />}>
          {store.groupOrder}
        </Pill>
      </div>

      <div className="absolute inset-x-[17px] top-[405px] flex h-[68px] rounded-[8px] border border-[#efefef] text-[12px]">
        <div className="flex flex-1 flex-col items-center justify-center gap-[5px] font-medium" style={{ color: ue.teal }}>
          <span>{store.perk[0]}</span>
          <span className="flex items-center gap-[3px]">
            {store.perk[1]} <CircleHelp size={11} />
          </span>
        </div>
        <div className="w-px bg-[#efefef]" />
        <div className="flex flex-1 flex-col items-center justify-center gap-[5px]">
          <span className="font-semibold">{store.eta}</span>
          <span className="flex items-center gap-[3px]" style={{ color: ue.muted }}>
            {store.etaLabel} <CircleHelp size={11} />
          </span>
        </div>
      </div>

      <SectionHeader title={store.dealTitle} className="absolute inset-x-0 top-[515px]" />

      <div className="absolute inset-x-[17px] top-[565px] flex">
        <div className="w-[248px]">
          <div className="text-[15.5px] leading-[20px] font-medium">{d.title}</div>
          <div className="mt-[2px] flex items-center gap-[3px] text-[12.5px]">
            {d.price} · <ThumbsUp size={11} strokeWidth={1.8} /> {d.likes} · <span style={{ color: ue.muted }}>{d.calories}</span>
          </div>
          <p className="mt-[2px] line-clamp-2 text-[13px] leading-[20px]" style={{ color: ue.muted }}>
            {d.description}
          </p>
          <Tag className="mt-[1px] h-[19px] gap-[4px] text-[11.5px] text-white" style={{ background: ue.red }}>
            <Trophy size={10} fill="#fff" strokeWidth={1.5} />
            {d.promo}
          </Tag>
        </div>
        <div className="relative ml-[7px] h-[103px] flex-1">
          <ImagePlaceholder className="h-full w-full rounded-[6px]" label="meal photo" />
          <span className="absolute right-[3px] bottom-[5px] flex h-[34px] w-[34px] items-center justify-center rounded-full bg-white shadow-[0_1px_6px_rgba(0,0,0,0.16)]">
            <Plus size={16} strokeWidth={2.2} />
          </span>
        </div>
      </div>

      <div className="absolute inset-x-0 top-[681px] h-[3px]" style={{ background: '#f5f5f5' }} />
      <SectionHeader title={store.exploreTitle} className="absolute inset-x-0 top-[702px]" />
      <div className="absolute top-[740px] left-[17px] flex gap-[9px]">
        {store.menuChips.map((c) => {
          const Icon = c.icon
          return (
            <Pill
              key={c.key}
              className="h-[36px] gap-[8px] px-[13px] text-[13px] font-medium"
              style={c.active ? { background: '#000', color: '#fff' } : { background: ue.field }}
              leading={Icon && <Icon size={13} strokeWidth={2} fill={c.active ? '#fff' : 'none'} />}
            >
              {c.label}
            </Pill>
          )
        })}
      </div>
      <div className="absolute top-[790px] left-[20px] flex gap-[10px]">
        {[0, 1, 2].map((i) => (
          <div key={i} className="relative">
            <ImagePlaceholder className="h-[80px] w-[140px] rounded-[6px]" tone={i === 0 ? undefined : '#f3f4f6'} label="menu item photo" />
            {i === 0 && (
              <Tag className="absolute top-[12px] left-[6px] h-[19px] text-[11px] text-white" style={{ background: '#2e8b45' }}>
                {store.menuBadge}
              </Tag>
            )}
          </div>
        ))}
      </div>
    </AppScreen>
  )
}
