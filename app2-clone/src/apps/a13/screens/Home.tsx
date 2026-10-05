import { ArrowRight, Search } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { ArrowLink } from '../components/ArrowLink'
import { BottomNav } from '../components/BottomNav'
import { Card } from '../components/Card'
import { StatusRow } from '../components/StatusRow'
import { home as d } from '../data'
import { fonts, zip } from '../theme'

function SpendingPill() {
  return (
    <Card className="absolute top-[80px] left-[205px] flex h-[56px] w-[167px] items-center justify-between pr-[18px] pl-[12px]">
      <div>
        <div className="text-[13.5px] leading-[17px]" style={{ color: zip.purpleText }}>
          {d.spendingLabel}
        </div>
        <div className="text-[16.5px] leading-[21px] font-semibold">{d.spendingValue}</div>
      </div>
      <ArrowRight size={21} strokeWidth={1.6} />
    </Card>
  )
}

function NoticeCard() {
  const n = d.notice
  return (
    <Card className="absolute top-[158px] left-[15px] h-[107px] w-[357px] px-[15px] pt-[9px]">
      <div className="text-[15px] leading-[20px] font-semibold">{n.title}</div>
      <div className="mt-[3px] text-[15.5px] leading-[21px] text-[#3a3340]">
        {n.body.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <ArrowLink label={n.link} className="mt-[3px] text-[15px]" />
      <span
        className="absolute -top-[11px] -right-[7px] flex h-[22px] w-[22px] items-center justify-center rounded-full text-[13px] font-semibold text-white"
        style={{ background: zip.purple }}
      >
        {n.badge}
      </span>
    </Card>
  )
}

function ChipsRow() {
  return (
    <div className="absolute top-[383px] left-[15px] flex gap-[9px] whitespace-nowrap">
      {d.chips.map(({ key, label, icon: Icon }) => (
        <div
          key={key}
          className="flex h-[38px] items-center gap-[10px] rounded-full bg-white px-[13px] text-[15px]"
          style={{ color: zip.purpleText }}
        >
          <Icon size={19} strokeWidth={1.5} />
          {label}
        </div>
      ))}
    </div>
  )
}

function BrandCircles() {
  return (
    <div className="absolute top-[504px] left-[15px] flex gap-[13.5px]">
      {d.brands.map((b) => (
        <div key={b.key} className="flex w-[62px] flex-col items-center">
          <ImagePlaceholder label={b.label} className="h-[62px] w-[62px] rounded-full" />
          <span className="mt-[12px] text-[12.5px] leading-none text-[#3a3340]">{b.label}</span>
        </div>
      ))}
    </div>
  )
}

function PromoCarousel() {
  return (
    <div className="absolute top-[635px] left-[15px] flex gap-[11px]">
      {d.promos.map((p, i) => (
        <Card key={p.key} className="relative h-[140px] w-[291px] shrink-0 rounded-[16px] pt-[24px] pl-[16px]">
          <div className={`${fonts.display} text-[19px] leading-[17px] font-extrabold tracking-[-0.5px]`}>
            {p.title.map((l) => (
              <div key={l}>{l}</div>
            ))}
          </div>
          <ArrowLink label={p.cta} className="mt-[13px] text-[15.5px]" iconSize={14} />
          {i === 0 && <ImagePlaceholder label="gift card" className="absolute top-[36px] left-[170px] h-[60px] w-[95px]" />}
        </Card>
      ))}
    </div>
  )
}

export function Home() {
  return (
    <AppScreen className={fonts.body} background={zip.lavender} style={{ color: zip.ink }}>
      <StatusRow />
      <h1 className="absolute top-[76px] left-[14px] text-[26px] font-medium tracking-[-0.3px]">{d.greeting}</h1>
      <ImagePlaceholder label="name (blurred)" tone="#cfc2f0" className="absolute top-[115px] left-[14px] h-[19px] w-[131px] rounded-[3px]" />
      <SpendingPill />
      <NoticeCard />

      <div className="absolute inset-x-0 top-[300px] bottom-0 rounded-t-[24px]" style={{ background: zip.page }} />
      <div className="absolute top-[316px] left-[15px] flex h-[54px] w-[357px] items-center gap-[14px] rounded-[14px] bg-white pl-[17px] shadow-[0_2px_6px_rgba(0,0,0,0.05)]">
        <Search size={23} strokeWidth={1.3} className="text-[#6d6d72]" />
        <span className="text-[17px] text-[#55555a]">{d.search}</span>
      </div>
      <ChipsRow />
      <div className="absolute top-[434px] left-[14px] text-[12.5px]" style={{ color: zip.purpleText }}>
        {d.disclosure}
      </div>
      <div className="absolute top-[471px] left-[14px] text-[15px] font-semibold">{d.brandsTitle}</div>
      <div className="absolute top-[471px] right-[18px] text-[15px] text-[#55555a]">{d.viewAll}</div>
      <BrandCircles />
      <PromoCarousel />
      <BottomNav items={d.nav} activeKey={d.activeNav} />
    </AppScreen>
  )
}
