import { Bell, ChevronDown } from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { FloatingNav } from '../components/FloatingNav'
import { Pill } from '../components/Pill'
import { SectionHeader } from '../components/SectionHeader'
import { StoreCard } from '../components/StoreCard'
import { home } from '../data'
import { ue } from '../theme'

export function Home() {
  return (
    <AppScreen className="font-inter" background="#fff">
      <StatusBar />
      <header className="flex h-[62px] items-center justify-between pr-[22px] pl-[16px]">
        <span className="flex items-center gap-[8px] text-[16px] font-medium">
          {home.location}
          <ChevronDown size={14} strokeWidth={2.4} />
        </span>
        <Bell size={20} strokeWidth={1.8} />
      </header>
      <div className="-mt-[8px] flex gap-[7px] overflow-hidden pl-[20px]">
        {home.verticals.map((c) => (
          <Pill
            key={c.key}
            className="h-[34px] gap-[6px] px-[11px] text-[12.5px]"
            style={c.active ? { background: ue.chip, fontWeight: 600 } : { border: '1.5px solid #f1f1f1', color: '#444' }}
            leading={<ImagePlaceholder className="h-[16px] w-[16px] rounded-[3px]" label={`${c.label} icon`} />}
          >
            {c.label}
          </Pill>
        ))}
      </div>
      <div className="mt-[14px] flex pl-[13px]">
        {home.categories.map((c) => (
          <div key={c.key} className="flex w-[75.5px] flex-col items-center">
            <ImagePlaceholder className="h-[46px] w-[50px] rounded-[8px]" label={`${c.label} icon`} />
            <span className="mt-[11px] text-[12px]">{c.label}</span>
          </div>
        ))}
      </div>
      <div className="mt-[14px] flex gap-[9px] overflow-hidden pl-[16px]">
        {home.filters.map((c) => {
          const Icon = c.icon
          return (
            <Pill
              key={c.key}
              className="h-[35px] gap-[8px] px-[13px] text-[13px] font-medium"
              style={{ background: ue.field }}
              leading={Icon && <Icon size={14} strokeWidth={2} />}
            >
              {c.label}
            </Pill>
          )
        })}
      </div>
      <SectionHeader title={home.featuredTitle} arrow className="mt-[22px]" />
      <div className="mt-[8px] flex gap-[9px] pl-[16px]">
        {home.featured.map((s) => (
          <StoreCard key={s.key} store={s} width={235} />
        ))}
      </div>
      <div className="mt-[12px] h-[3px]" style={{ background: '#f5f5f5' }} />
      <SectionHeader title={home.topTitle} subtitle={home.topSubtitle} arrow className="mt-[7px]" />
      <div className="mt-[13px] flex gap-[25px] pl-[28px]">
        <ImagePlaceholder className="h-[200px] w-[171px] rounded-[10px]" label="promo photo" />
        <ImagePlaceholder className="h-[200px] w-[171px] rounded-[10px]" label="promo photo" />
      </div>
      <FloatingNav searchLabel={home.searchLabel} />
    </AppScreen>
  )
}
