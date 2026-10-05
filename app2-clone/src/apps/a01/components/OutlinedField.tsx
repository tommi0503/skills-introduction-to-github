import { Eye } from 'lucide-react'

export interface OutlinedFieldProps {
  top: number
  placeholder: string
  value?: string
  /** Number of mask dots when this is a filled password field. */
  maskLength?: number
  revealable?: boolean
}

/** Rounded outlined text field; shows placeholder, value, or password dots. */
export function OutlinedField({ top, placeholder, value, maskLength, revealable }: OutlinedFieldProps) {
  return (
    <div
      className="absolute flex items-center rounded-[8px] border border-[#9d9da2] pr-[16px] pl-[16px]"
      style={{ left: 19, top, width: 351, height: 47 }}
    >
      <span className="flex-1 truncate text-[12.5px]">
        {maskLength ? (
          <span className="flex gap-[1.6px]">
            {Array.from({ length: maskLength }, (_, i) => (
              <span key={i} className="h-[11px] w-[11px] rounded-full bg-black" />
            ))}
          </span>
        ) : value ? (
          <span className="text-[#222]">{value}</span>
        ) : (
          <span className="text-[#b3b3b8]">{placeholder}</span>
        )}
      </span>
      {revealable && <Eye size={14} strokeWidth={2} color="#55555c" />}
    </div>
  )
}
