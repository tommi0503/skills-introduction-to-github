import { Mic, Send } from 'lucide-react'
import { theme } from '../theme'

/** Composer: mic, placeholder, detached black send button. */
export function ChatInput({ placeholder }: { placeholder: string }) {
  return (
    <div className="flex items-center gap-[11px]">
      <div className="flex h-[52px] w-[293px] items-center rounded-full bg-white pl-[5px]" style={{ boxShadow: '0 4px 20px rgba(0,0,0,0.06)' }}>
        <span className="flex h-[42px] w-[42px] items-center justify-center rounded-full" style={{ background: theme.soft }}>
          <Mic size={20} strokeWidth={2.3} />
        </span>
        <span className="ml-[12px] text-[14px] text-[#555]">{placeholder}</span>
      </div>
      <span className="flex h-[52px] w-[52px] items-center justify-center rounded-full bg-black text-white">
        <Send size={21} strokeWidth={1.8} fill="#fff" />
      </span>
    </div>
  )
}
