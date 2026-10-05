import { ArrowLeft, Info, X } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { results, search } from '../data'
import { theme } from '../theme'
import { CartButton } from '../components/CartButton'
import { Chrome } from '../components/Chrome'
import { ResultItem } from '../components/ResultItem'
import { UnderlineTabs } from '../components/UnderlineTabs'

export function SearchScreen() {
  return (
    <AppScreen className="font-pretendard">
      <ArrowLeft size={24} strokeWidth={1.9} className="absolute left-[10px] top-[71px]" />
      <div className="absolute left-[45px] top-[63px] flex h-[40px] w-[297px] items-center justify-between rounded-full pl-[17px] pr-[16px]" style={{ background: theme.field }}>
        <span className="text-[16px] text-[#111]">{search.query}</span>
        <span className="flex h-[18px] w-[18px] items-center justify-center rounded-full bg-[#bfc2c6]">
          <X size={12} color="#fff" strokeWidth={3} />
        </span>
      </div>
      <span className="absolute left-[353px] top-[71px]">
        <CartButton />
      </span>
      <div className="absolute left-[17px] top-[117px] flex gap-[16px] whitespace-nowrap text-[14px] leading-[20px] tracking-[-0.3px]">
        <span className="text-[#333]">{search.relatedLabel}</span>
        {search.related.map((r) => (
          <span key={r} style={{ color: theme.blue }}>{r}</span>
        ))}
      </div>
      <UnderlineTabs
        items={search.tabs}
        active={search.tabs[0]}
        gap={32}
        bleed={4}
        className="absolute inset-x-0 top-[152px] h-[38px] pl-[23px]"
        itemClassName="text-[16px] tracking-[-0.3px]"
        activeClassName="font-bold text-[#111]"
        inactiveClassName="text-[#9a9da2]"
      />
      <p className="absolute left-[13px] top-[207px] text-[20px] font-bold tracking-[-0.5px] text-[#111]">{search.section}</p>
      <p className="absolute left-[13px] top-[253px] flex items-center gap-[3px] text-[12px] text-[#333]">
        {search.sort}
        <Info size={12} strokeWidth={1.6} color="#999" />
      </p>
      <div className="absolute inset-x-0 top-[270px]">
        {results.map((r) => (
          <ResultItem key={r.key} item={r} />
        ))}
      </div>
      <Chrome />
    </AppScreen>
  )
}
