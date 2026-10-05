import { Mic } from 'lucide-react'
import { theme } from '../theme'
import { BotGlyph } from './BotGlyph'

/** Assistant's contextual hint with mic action. */
export function HintBox({ text }: { text: string }) {
  return (
    <div className="flex h-[72px] items-center rounded-[18px] border-[2.5px] bg-white pr-[16px] pl-[11px]" style={{ borderColor: theme.blue }}>
      <BotGlyph size={41} color={theme.bot} />
      <p className="ml-[10px] w-[220px] text-[13.5px] leading-[20.5px]" style={{ color: '#4a4a4f' }}>
        {text}
      </p>
      <span className="ml-auto h-[30px] w-px bg-[#e4e4e7]" />
      <Mic size={24} strokeWidth={2.4} className="ml-[18px]" />
    </div>
  )
}
