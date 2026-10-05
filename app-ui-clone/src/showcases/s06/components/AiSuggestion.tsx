import { Sparkle, Sparkles } from 'lucide-react'
import { theme } from '../theme'

export interface AiSuggestionProps {
  label: string
  timer: string
}

/** Pill with a gradient hairline border prompting an AI reply. */
export function AiSuggestion({ label, timer }: AiSuggestionProps) {
  return (
    <div className="rounded-[16px] p-[2px]" style={{ background: theme.aiBorder }}>
      <div className="flex h-[70px] items-center rounded-[14px] pr-[28px] pl-[18px]" style={{ background: '#f8f7f3' }}>
        <span className="flex h-[38px] w-[38px] items-center justify-center rounded-full bg-white">
          <Sparkles size={17} strokeWidth={1.7} color={theme.blue} />
        </span>
        <span className="ml-[10px] flex-1 text-[14px] font-medium text-[#222]">{label}</span>
        <span className="text-[13px] font-medium text-[#a593f7]">{timer}</span>
        <Sparkle size={14} strokeWidth={1.8} color="#8a7af5" className="ml-[6px]" />
      </div>
    </div>
  )
}
