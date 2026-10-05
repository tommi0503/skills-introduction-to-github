import { ArrowRight } from 'lucide-react'
import { Triangle } from './Triangle'
import type { timeSlot } from '../data'
import { theme } from '../theme'

function TimeField({ caption, value }: { caption: string; value: string }) {
  return (
    <div
      className="flex h-[41px] flex-1 items-center gap-[6px] rounded-[12px] pl-[8px] pr-[8px]"
      style={{ background: theme.fieldBg }}
    >
      <span className="text-[10px] text-[#8b8a86]">{caption}</span>
      <span className="flex-1 text-[14px] font-medium">{value}</span>
      <span className="flex flex-col gap-[2px] text-[#4a4944]">
        <Triangle dir="up" size={4} />
        <Triangle dir="down" size={4} />
      </span>
    </div>
  )
}

export interface TimeSlotPickerProps {
  slot: typeof timeSlot
  saveLabel: string
}

/** Start → End time fields plus the save action. */
export function TimeSlotPicker({ slot, saveLabel }: TimeSlotPickerProps) {
  return (
    <div className="px-[10px] pt-[12px]">
      <div className="text-[9.5px] text-[#77766f]">{slot.label}</div>
      <div className="mt-[6px] flex items-center gap-[8px]">
        <TimeField {...slot.start} />
        <ArrowRight size={15} strokeWidth={1.8} />
        <TimeField {...slot.end} />
      </div>
      <button type="button" className="mt-[9px] h-[42px] w-full rounded-[14px] bg-white text-[13px] font-medium">
        {saveLabel}
      </button>
    </div>
  )
}
