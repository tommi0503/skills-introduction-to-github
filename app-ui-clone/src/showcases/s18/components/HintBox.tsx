import { Mic } from 'lucide-react'
import { theme } from '../theme'
import { BotGlyph } from './BotGlyph'

/** Assistant's contextual hint with mic action. */
export function HintBox({ text }: { text: string }) {
  return (
    <div className="flex h-[72px] items-center rounded-[18px] border-[1.5px] bg-white pr-[16px] pl-[18px]" style={{ borderColor: theme.blue }}>
      <BotGlyph size={41} color={theme.bot} />
      <p className="ml-[14px] w-[210px] text-[13.5px] leading-[20.5px]" style={{ color: theme.text }}>
        {text}
      </p>
      <span className="ml-auto h-[30px] w-px bg-[#e4e4e7]" />
      <Mic size={22} strokeWidth={2} className="ml-[20px]" />
    </div>
  )
}
