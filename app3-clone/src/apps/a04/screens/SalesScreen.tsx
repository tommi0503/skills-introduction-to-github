import { ChevronLeft, Ellipsis } from 'lucide-react'
import { AppScreen, Avatar, cn } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { ListingRow } from '../components/ListingRow'
import { sales } from '../data'
import { kr } from '../theme'

function RowActions() {
  return (
    <div className="mt-[17px] flex gap-[7px]">
      {sales.actions.map((a) => (
        <span key={a} className="flex h-[35px] flex-1 items-center justify-center rounded-[4px] text-[13px] font-semibold" style={{ background: kr.chip }}>
          {a}
        </span>
      ))}
      <span className="flex h-[35px] w-[35px] items-center justify-center rounded-[4px]" style={{ background: kr.chip }}>
        <Ellipsis size={16} strokeWidth={2} />
      </span>
    </div>
  )
}

function SegmentTabs() {
  return (
    <div className="absolute inset-x-0 top-[202px] flex h-[42px] border-b" style={{ borderColor: kr.line }}>
      {sales.tabs.map((t, i) => (
        <span
          key={t}
          className={cn('flex flex-1 items-center justify-center text-[13px]', i === 0 ? 'border-b-2 border-black font-bold' : '')}
          style={i === 0 ? undefined : { color: kr.sub }}
        >
          {t}
        </span>
      ))}
    </div>
  )
}

/** "My sales" list: header with avatar, write button, status tabs and items with bump/promote actions. */
export function SalesScreen() {
  return (
    <AppScreen className="font-pretendard" style={{ color: kr.text }}>
      <Chrome />
      <ChevronLeft size={27} strokeWidth={1.7} className="absolute top-[62px] left-[12px]" />
      <h1 className="absolute top-[108px] left-[15px] text-[19px] font-bold">{sales.title}</h1>
      <div className="absolute top-[108px] right-[17px]">
        <Avatar size={64} />
      </div>
      <span
        className="absolute top-[150px] left-[15px] flex h-[35px] w-[63px] items-center justify-center rounded-[4px] text-[13.5px] font-semibold"
        style={{ background: kr.orangeSoft, color: kr.orange }}
      >
        {sales.write}
      </span>
      <SegmentTabs />
      <div className="absolute top-[257px] left-[15px] flex items-center gap-[8px] text-[12px]" style={{ color: '#4d5159' }}>
        <span className="h-[18px] w-[18px] rounded-full border" style={{ borderColor: '#dcdee3' }} />
        {sales.filter}
      </div>
      <div className="absolute inset-x-0 top-[287px]">
        {sales.items.map((it) => (
          <ListingRow key={it.key} item={it} showCounters={false} footer={<RowActions />} />
        ))}
      </div>
    </AppScreen>
  )
}
