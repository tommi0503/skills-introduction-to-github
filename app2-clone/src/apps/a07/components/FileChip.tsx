import { ArrowDown } from 'lucide-react'
import { theme } from '../theme'

export interface FileChipProps {
  name: string
  ext: string
  size: string
}

export function FileChip({ name, ext, size }: FileChipProps) {
  return (
    <div className="flex h-[55px] w-[204px] items-center gap-[10px] rounded-[16px] pl-[12px]" style={{ background: theme.bubble }}>
      <span className="flex h-[26px] w-[26px] items-center justify-center rounded-[6px] bg-[#e6e6e6] text-[10px] font-semibold text-[#999]">
        M<ArrowDown size={9} strokeWidth={2.5} />
      </span>
      <div className="leading-none">
        <div className="text-[14px] text-[#222]">
          {name}
          <span className="text-[#aaa]">{ext}</span>
        </div>
        <div className="mt-[6px] text-[10.5px] text-[#aaa]">{size}</div>
      </div>
    </div>
  )
}
