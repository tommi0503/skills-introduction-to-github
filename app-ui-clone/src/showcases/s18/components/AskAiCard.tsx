import { Mic, Plus, Search, Send, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

export interface AskAiCardProps {
  thumbs: number
  text: string
  placeholder: string
}

/** Prompt suggestion card: liked dishes, suggestion copy and an input row. */
export function AskAiCard({ thumbs, text, placeholder }: AskAiCardProps) {
  return (
    <div className="relative h-[250px] rounded-[22px] px-[14px] pt-[44px]" style={{ background: theme.soft }}>
      <span className="absolute top-[14px] right-[10px] flex h-[34px] w-[34px] items-center justify-center rounded-full bg-white">
        <X size={16} strokeWidth={2.4} />
      </span>
      <div className="flex gap-[8.7px]">
        {Array.from({ length: thumbs }, (_, i) => (
          <ImagePlaceholder key={i} className="h-[63px] w-[63px] rounded-[12px]" label="liked dish" />
        ))}
      </div>
      <p className="mt-[16px] w-[310px] text-[13px] leading-[18px] text-[#6b6b72]">{text}</p>
      <div className="mt-[26px] -mx-[2px] flex h-[46px] items-center rounded-[14px] bg-white pr-[8px] pl-[8px]">
        {[Plus, Mic].map((Icon, i) => (
          <span key={i} className="mr-[6px] flex h-[28px] w-[28px] items-center justify-center rounded-[8px]" style={{ background: theme.soft }}>
            <Icon size={14} strokeWidth={2.2} />
          </span>
        ))}
        <Search size={15} strokeWidth={2} className="ml-[21px] text-[#444]" />
        <span className="ml-[8px] flex-1 text-[12.5px] text-[#8b8b93]">{placeholder}</span>
        <span className="flex h-[30px] w-[30px] items-center justify-center rounded-[8px] bg-black text-white">
          <Send size={14} strokeWidth={2} fill="#fff" className="-rotate-0" />
        </span>
      </div>
    </div>
  )
}
