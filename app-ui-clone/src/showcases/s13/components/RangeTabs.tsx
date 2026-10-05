import { cn } from '../../../ui'

export interface RangeTabsProps {
  options: string[]
  active: string
}

/** Four equal pills; the active one is solid black. */
export function RangeTabs({ options, active }: RangeTabsProps) {
  return (
    <div className="flex gap-[3px]">
      {options.map((o) => (
        <div
          key={o}
          className={cn(
            'flex h-[34px] flex-1 items-center justify-center rounded-full text-[12.5px] font-medium',
            o === active ? 'bg-black text-white shadow-[0_3px_8px_rgba(0,0,0,0.25)]' : 'bg-[#e4e3df] text-[#2a2a2a]',
          )}
        >
          {o}
        </div>
      ))}
    </div>
  )
}
