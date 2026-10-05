import { ChartNoAxesColumn, ChevronRight, CreditCard, Search } from 'lucide-react'
import { AppScreen, Avatar, HomeIndicator, StatusBar } from '../../../ui'
import { CircleAction } from '../components/CircleAction'
import { RevolutTabBar } from '../components/RevolutTabBar'
import { TransactionRow } from '../components/TransactionRow'
import { home } from '../data'
import { rv } from '../theme'

export function Home() {
  return (
    <AppScreen className="font-inter" background={rv.black} style={{ background: rv.homeGradient }}>
      <StatusBar color="#fff" />
      <div className="mt-[8px] flex items-center gap-[8px] px-[16px] text-white">
        <Avatar size={34} />
        <div className="flex h-[34px] flex-1 items-center gap-[10px] rounded-full bg-white/20 px-[12px] text-[13.5px] text-white/75">
          <Search size={17} strokeWidth={2.2} color="#fff" />
          {home.search}
        </div>
        {[ChartNoAxesColumn, CreditCard].map((Icon, i) => (
          <span key={i} className="flex h-[36px] w-[36px] items-center justify-center rounded-full bg-white/20">
            <Icon size={17} strokeWidth={2.4} />
          </span>
        ))}
      </div>

      <div className="mt-[80px] flex flex-col items-center text-white">
        <span className="text-[13px] text-white/85">{home.account}</span>
        <div className="mt-[4px] flex items-baseline font-bold">
          <span className="text-[40px] leading-[46px] tracking-[-0.5px]">{home.balanceMajor}</span>
          <span className="text-[20px]">{home.balanceMinor}</span>
        </div>
        <span className="mt-[11px] flex h-[36px] items-center rounded-full bg-white/25 px-[16px] text-[13px] font-medium">{home.accounts}</span>
        <div className="mt-[64px] flex gap-[3px]">
          {Array.from({ length: home.pages }, (_, i) => (
            <span key={i} className="h-[4px] w-[4px] rounded-full" style={{ background: i === home.page ? '#fff' : 'rgba(255,255,255,0.45)' }} />
          ))}
        </div>
      </div>

      <div className="mt-[39px] flex justify-between px-[15px]">
        {home.actions.map((a) => (
          <CircleAction key={a.key} icon={a.icon} label={a.label} />
        ))}
      </div>

      <div className="mx-[16px] mt-[14px] rounded-[16px] pt-[2px] pb-[14px]" style={{ background: rv.txCard }}>
        {home.transactions.map((t) => (
          <TransactionRow key={t.key} tx={t} />
        ))}
        <div className="mt-[11px] text-center text-[14px] font-medium text-white">{home.seeAll}</div>
      </div>

      <div className="mx-[16px] mt-[17px] h-[70px] rounded-[16px] px-[16px] pt-[16px]" style={{ background: rv.txCard }}>
        <span className="flex items-center gap-[2px] text-[12.5px] font-medium text-white/80">
          {home.products} <ChevronRight size={13} strokeWidth={2.4} />
        </span>
      </div>

      <RevolutTabBar tabs={home.tabs} active={home.activeTab} />
      <HomeIndicator tone="light" />
    </AppScreen>
  )
}
