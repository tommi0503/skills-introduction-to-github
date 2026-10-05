import { ChipGroup } from '../../../ui'

export interface FilterChipsProps {
  labels: string[]
  active: string
  top: number
}

/** Pill filters that run off the right edge; active pill in the accent blue. */
export function FilterChips({ labels, active, top }: FilterChipsProps) {
  return (
    <div className="absolute left-[18px]" style={{ top }}>
      <ChipGroup
        items={labels.map((l) => ({ key: l, label: l }))}
        activeKey={active}
        gap={8}
        chipClassName="h-[40px] rounded-full px-[23px] text-[12.5px]"
        activeClassName="bg-[#4f8ef0] text-white"
        inactiveClassName="bg-white text-[#3a3a3a]"
      />
    </div>
  )
}
