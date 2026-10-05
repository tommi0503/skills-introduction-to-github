import { Flame } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Macro } from '../data'
import { theme } from '../theme'

export interface FoodCardProps {
  name: string
  time: string
  calories: string
  macros: string[]
  macroDefs: Macro[]
}

export function FoodCard({ name, time, calories, macros, macroDefs }: FoodCardProps) {
  return (
    <div className="flex h-[124px] overflow-hidden rounded-[14px]" style={{ background: theme.foodCard }}>
      <ImagePlaceholder label="Fried chicken photo" className="h-full w-[124px] rounded-l-[14px]" />
      <div className="relative flex-1 pl-[15px] pt-[19px]">
        <div className="text-[13.5px] leading-none">{name}</div>
        <span className="absolute right-[16px] top-[15px] rounded-[6px] bg-white px-[5px] py-[4px] text-[10px] leading-none">{time}</span>
        <div className="mt-[18px] flex items-center gap-[8px] text-[15.5px] font-semibold leading-none">
          <Flame size={15} fill={theme.ink} />
          {calories}
        </div>
        <div className="mt-[17px] flex items-center gap-[10px] text-[11px] leading-none">
          {macros.map((v, i) => {
            const Icon = macroDefs[i].icon
            return (
              <span key={v} className="flex items-center gap-[5px]">
                <Icon size={11} color={macroDefs[i].color} fill={macroDefs[i].color} />
                {v}
              </span>
            )
          })}
        </div>
      </div>
    </div>
  )
}
