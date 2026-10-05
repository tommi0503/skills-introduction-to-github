import { ChevronRight, Gift, Tag } from 'lucide-react'
import type { ActionRow, CartItem, FeeRow } from '../data'
import { uber } from '../theme'

export function CartItemRow({ item }: { item: CartItem }) {
  return (
    <div className="flex h-[49px] items-center pb-[9px]">
      <span
        className="flex h-[23px] w-[24px] items-center justify-center text-[12px]"
        style={{ background: '#f3f3f3', color: uber.ink }}
      >
        {item.qty}
      </span>
      <span className="ml-[13px] flex-1 text-[15.5px] font-medium">{item.name}</span>
      <span className="text-[15px]">{item.price}</span>
    </div>
  )
}

const actionIcons = { gift: Gift, promo: Tag }

export function ActionListRow({ row, last }: { row: ActionRow; last?: boolean }) {
  const Icon = actionIcons[row.key]
  return (
    <div className="flex h-[84px] items-center">
      <div className="flex w-[68px] justify-start pl-[24px]">
        <Icon size={20} strokeWidth={2.4} fill={row.key === 'promo' ? 'currentColor' : 'none'} />
      </div>
      <div
        className="flex h-full flex-1 items-center pr-[18px]"
        style={{ borderBottom: last ? 'none' : `1px solid ${uber.hairline}` }}
      >
        <div className="flex-1">
          <div className="text-[15px] leading-[20px] font-medium">{row.title}</div>
          <div className="mt-[3px] text-[13px] leading-[17px]" style={{ color: row.accent ? uber.green : uber.muted }}>
            {row.subtitle}
          </div>
        </div>
        <ChevronRight size={18} strokeWidth={2} color="#9a9a9a" />
      </div>
    </div>
  )
}

export function FeeLine({ row }: { row: FeeRow }) {
  const color = row.total ? uber.ink : row.accent ? uber.green : uber.muted
  return (
    <div
      className="flex h-[34.5px] items-center justify-between"
      style={{ fontSize: row.total ? 17 : 15, fontWeight: row.total ? 700 : 400 }}
    >
      <span className="flex items-center gap-[7px]" style={{ color: row.total ? uber.ink : uber.muted }}>
        {row.label}
        {row.info && (
          <span className="flex h-[15px] w-[15px] items-center justify-center rounded-full bg-[#a6a6a6] text-[10px] font-bold text-white">
            i
          </span>
        )}
      </span>
      <span style={{ color }}>{row.value}</span>
    </div>
  )
}
