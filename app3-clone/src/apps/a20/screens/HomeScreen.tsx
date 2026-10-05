import { ChevronRight, CircleDollarSign, Search, ShoppingBag } from 'lucide-react'
import { AppScreen, HomeIndicator, ImagePlaceholder, cn } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { PhoneStatus } from '../components/PhoneStatus'
import { hero, homeTabs, navTabs, promo, shortcuts } from '../data'
import { theme } from '../theme'

export function HomeScreen() {
  return (
    <AppScreen className="font-pretendard">
      <PhoneStatus />
      <ImagePlaceholder tone="#1a1a1a" label="ZIGZAG logo" className="absolute top-[64px] left-[17px] h-[20px] w-[91px] rounded-[2px]" />
      <div className="absolute top-[62px] right-[17px] flex items-center gap-[21px] text-[#111]">
        <CircleDollarSign size={23} strokeWidth={1.7} />
        <Search size={22} strokeWidth={2} />
        <ShoppingBag size={22} strokeWidth={1.8} />
      </div>
      <div className="absolute top-[115px] left-[20px] flex gap-[26px] text-[15.5px] font-semibold whitespace-nowrap">
        {homeTabs.map((t) => (
          <span key={t.key} className={cn('relative', t.active ? 'text-[#111]' : t.accent ? '' : 'text-[#c4c4c8]')} style={t.accent ? { color: theme.violet } : undefined}>
            {t.active && <span className="absolute top-[-7px] left-1/2 h-[4px] w-[4px] -translate-x-1/2 rounded-full bg-[#111]" />}
            {t.label}
          </span>
        ))}
      </div>
      <div className="absolute top-[152px] left-[17px] flex h-[58px] w-[356px] items-center rounded-[10px] border border-[#f1dcf3] pr-[10px] pl-[10px]" style={{ background: theme.pinkSoft }}>
        <ImagePlaceholder label="promo thumbnail" className="h-[38px] w-[36px] rounded-[6px]" />
        <div className="ml-[11px] flex flex-1 flex-col">
          <span className="text-[14.5px] leading-[19px] font-bold text-[#222]">{promo.title}</span>
          <span className="text-[11.5px] leading-[16px] text-[#8a8a8e]">{promo.sub}</span>
        </div>
        <span className="flex h-[23px] items-center rounded-[5px] px-[7px] text-[11px] font-bold text-white" style={{ background: '#e286e8' }}>
          {promo.cta}
        </span>
      </div>
      <div className="absolute top-[222px] left-[17px] h-[358px] w-[357px] overflow-hidden rounded-[12px]">
        <ImagePlaceholder tone="#a3a3a8" label="hero model photo" className="absolute inset-0" />
        <span className="absolute top-[9px] left-[9px] rounded-[5px] bg-black/40 px-[8px] text-[11px] leading-[22px] text-white">{hero.tag}</span>
        <h2 className="absolute inset-x-0 top-[221px] text-center text-[21px] leading-[36px] font-semibold whitespace-pre-line text-white">{hero.title}</h2>
        <p className="absolute inset-x-0 top-[298px] text-center text-[12.5px] font-medium text-white">{hero.sub}</p>
        <span className="absolute right-[9px] bottom-[10px] flex items-center gap-[5px] rounded-full bg-black/25 py-[2px] pr-[5px] pl-[8px] text-[11px] font-medium text-white">
          {hero.page}
          <span className="h-[9px] w-px bg-white/60" />
          {hero.total}
          <ChevronRight size={11} strokeWidth={2.4} />
        </span>
      </div>
      <div className="absolute top-[595px] left-[17px] flex gap-[15px]">
        {shortcuts.map((s) => (
          <div key={s.key} className="relative flex w-[62px] flex-col items-center">
            <div className="flex h-[62px] w-[62px] items-center justify-center rounded-full bg-[#f3f5f5]">
              <ImagePlaceholder label={s.label} tone="#dcdde0" className="h-[40px] w-[40px] rounded-[8px]" />
            </div>
            {s.dot && <span className="absolute top-[7px] right-[3px] h-[7px] w-[7px] rounded-full bg-[#f0474f]" />}
            <span className="mt-[9px] text-[12px] whitespace-nowrap text-[#333]">{s.label}</span>
          </div>
        ))}
      </div>
      <div className="absolute top-[726px] left-[17px] flex w-[356px] items-center justify-between">
        <span className="text-[17px] font-bold text-[#111]">첫 구매 한정 특가</span>
        <span className="flex items-center gap-[3px] text-[12.5px] text-[#444]">
          전체보기 <ChevronRight size={15} strokeWidth={1.8} />
        </span>
      </div>
      <BottomNav tabs={navTabs} active="home" />
      <HomeIndicator width={140} bottom={6} />
    </AppScreen>
  )
}
