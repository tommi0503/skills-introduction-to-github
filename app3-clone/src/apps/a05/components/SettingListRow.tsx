import { Pencil } from 'lucide-react'
import type { SettingRow } from '../data'
import { ue } from '../theme'

export function SettingListRow({ row }: { row: SettingRow }) {
  const Icon = row.icon
  return (
    <div className="flex h-[65.5px] items-center">
      <div className="flex w-[64px] justify-start pl-[22px]">
        <Icon size={18} strokeWidth={1.9} />
      </div>
      <div className="flex h-full flex-1 items-center pr-[22px]" style={{ borderBottom: `1px solid ${ue.hairline}` }}>
        <div className="flex-1">
          <div className="text-[15px] leading-[19px] font-medium">{row.title}</div>
          <div className="mt-[3px] text-[12.5px]" style={{ color: ue.muted }}>
            {row.value}
          </div>
        </div>
        <Pencil size={20} strokeWidth={1.6} color={ue.pencil} />
      </div>
    </div>
  )
}
