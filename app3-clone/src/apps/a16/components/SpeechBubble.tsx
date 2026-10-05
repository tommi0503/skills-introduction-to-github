import { Volume2 } from 'lucide-react'
import type { PromptWord } from '../data'
import { palette as c } from '../theme'

/** Prompt bubble with a left tail; each word has a dotted "hint" underline. */
export function SpeechBubble({ words, speaker }: { words: PromptWord[]; speaker: boolean }) {
  return (
    <div className="relative flex h-[61px] w-[211px] items-center rounded-[14px] bg-white pl-[16px]" style={{ border: `2px solid ${c.line}` }}>
      <span
        className="absolute top-[18px] -left-[9px] h-[16px] w-[16px] rotate-45 bg-white"
        style={{ borderLeft: `2px solid ${c.line}`, borderBottom: `2px solid ${c.line}` }}
      />
      {speaker && <Volume2 size={22} strokeWidth={2.4} color={c.blue} fill={c.blue} className="mr-[13px]" />}
      <span className="flex gap-[5px] text-[16px]" style={{ color: c.text }}>
        {words.map((w, i) => (
          <span
            key={w.text}
            className={w.bold ? 'font-bold' : undefined}
            style={{ borderBottom: `2px dotted ${w.bold ? c.text : '#c8c8c8'}`, lineHeight: '22px' }}
          >
            {w.text}
            {i === words.length - 1 ? '.' : ''}
          </span>
        ))}
      </span>
    </div>
  )
}
