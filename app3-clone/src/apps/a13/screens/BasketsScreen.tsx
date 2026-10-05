import { ReceiptText } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { activeNav, baskets, header, navItems } from '../data'
import { BasketCard } from '../components/BasketCard'
import { BottomNav } from '../components/BottomNav'

export function BasketsScreen() {
  return (
    <AppScreen className="font-inter text-black">
      <StatusBar paddingX={40} paddingTop={20} fontSize={17} timeClassName="pl-[14px]" />
      <header className="flex items-center justify-between px-[16px] pt-[9px]">
        <h1 className="text-[22px] font-bold tracking-[-0.3px]">{header.title}</h1>
        <div className="flex items-center gap-[9px] pr-[12px] text-[14px] font-medium">
          <ReceiptText size={17} strokeWidth={2} />
          {header.action}
        </div>
      </header>
      <div className="mt-[24px] flex flex-col gap-[17px] px-[17px]">
        {baskets.map((b) => (
          <BasketCard key={b.id} basket={b} />
        ))}
      </div>
      <BottomNav items={navItems} active={activeNav} />
      <HomeIndicator width={138} bottom={5} />
    </AppScreen>
  )
}
