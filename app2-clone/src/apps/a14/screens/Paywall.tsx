import { X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { StatusRow } from '../components/StatusRow'
import { paywall as d } from '../data'
import { nord } from '../theme'

function PriceBox() {
  return (
    <div className="absolute top-[280px] left-[15px] w-[358px] overflow-hidden rounded-[12px] border border-[#ececf0] bg-white/60">
      <div className="flex h-[71px] flex-col items-center justify-center gap-[5px] pt-[12px] text-[16px]">
        <div className="font-medium" style={{ color: nord.blueText }}>
          {d.monthly}
        </div>
        <div>
          <s className="text-[#8a8a8f]">{d.oldPrice}</s> <span className="font-semibold">{d.newPrice}</span>
        </div>
      </div>
      <div className="flex h-[64px] flex-col items-center justify-center text-[13px] leading-[15px] text-[#a0a0b0]" style={{ background: nord.savings }}>
        {d.savings.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
    </div>
  )
}

export function Paywall() {
  return (
    <AppScreen className="font-figtree" background={nord.bgPaywall} style={{ color: nord.ink }}>
      <StatusRow />
      <span className="absolute top-[63px] left-[341px] flex h-[24px] w-[24px] items-center justify-center rounded-full bg-[#dedee0]">
        <X size={15} strokeWidth={2} className="text-[#555]" />
      </span>
      <ImagePlaceholder label="NordVPN logo" className="absolute top-[109px] left-[164px] h-[47px] w-[60px] rounded-t-full" />
      <h1 className="absolute inset-x-0 top-[188px] text-center text-[27.5px] font-semibold tracking-[-0.3px]">{d.title}</h1>
      <p className="absolute inset-x-0 top-[244px] text-center text-[15px] text-[#3a3a3e]">{d.subtitle}</p>
      <PriceBox />
      <ul className="absolute top-[438px] left-[34px]">
        {d.features.map(({ key, label, icon: Icon, filled }) => (
          <li key={key} className="flex h-[43px] items-center">
            {filled ? (
              <Icon size={23} strokeWidth={2} className="text-white" fill="#6a7cf0" />
            ) : (
              <Icon size={22} strokeWidth={2} className="text-[#6a7cf0]" />
            )}
            <span className="ml-[18px] text-[13.5px] tracking-[-0.25px] text-[#2a2a2e]">{label}</span>
          </li>
        ))}
      </ul>
      <button
        className="absolute top-[618px] left-[22px] h-[43px] w-[342px] rounded-[8px] text-[16px] font-semibold text-white"
        style={{ background: nord.blue }}
      >
        {d.cta}
      </button>
      <div className="absolute inset-x-0 top-[683px] text-center text-[16px] font-medium" style={{ color: nord.blueText }}>
        {d.plans}
      </div>
      <div className="absolute inset-x-0 top-[730px] text-center text-[13px] leading-[15.3px] text-[#5a5a5e]">
        {d.fine.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <div className="absolute inset-x-0 top-[791px] text-center text-[13px] text-[#8a8a8f] underline">{d.link}</div>
    </AppScreen>
  )
}
