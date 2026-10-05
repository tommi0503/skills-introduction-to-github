import { KeyValueList, Pill } from '../../../ui'
import type { InfoRow } from '../data'

/** Label pill + value rows (운영시간 / 주소 …). */
export function InfoList({ rows, className }: { rows: InfoRow[]; className?: string }) {
  return (
    <KeyValueList
      className={className}
      items={rows.map((r) => ({ key: r.label, label: r.label, value: r.value }))}
      labelWidth={97}
      rowClassName="h-[36px] items-center"
      labelClassName="self-center flex"
      valueClassName="self-center text-[13.5px] leading-none font-medium text-[#3a3a3a] tracking-[-0.2px]"
      renderLabel={(item) => (
        <Pill className="h-[26px] rounded-[7px] bg-[#f7f6f2] px-[6px] text-[13px] leading-none font-bold text-[#222]">{item.label}</Pill>
      )}
    />
  )
}
