import { Abs, ImagePlaceholder } from '../../ui'
import { Plus } from 'lucide-react'
import { theme } from './theme'
import type { Question } from './data'

export function QuestionCard({ q, lines, x, y, accent, img }: Question) {
  return (
    <Abs x={x} y={y} w={235} h={269} style={{ border: `1.5px solid ${theme.blue}`, background: '#fff' }}>
      <div
        className="absolute left-1/2 top-[-17px] flex h-[34px] w-[70px] -translate-x-1/2 items-center justify-center rounded-full text-[17px] font-bold"
        style={{ background: accent === 'blue' ? theme.blue : theme.yellow, color: accent === 'blue' ? '#fff' : '#555' }}
      >{q}</div>
      <ImagePlaceholder className={img.round ? 'absolute rounded-full' : 'absolute'} style={{ left: img.x, top: img.y, width: img.w, height: img.h }} />
      <div className="absolute inset-x-0 text-center text-[20px] leading-[30px]" style={{ top: 170, color: theme.ink }}>
        {lines.map((l) => <div key={l}>{l}</div>)}
      </div>
    </Abs>
  )
}

export function NoticeBar({ text }: { text: string }) {
  return (
    <Abs x={133} y={566} w={1014} h={53}>
      <div className="flex h-full items-center justify-center gap-3 rounded-full text-[21px]" style={{ background: theme.soft, border: `1.5px solid ${theme.blue}`, color: theme.ink }}>
        <span className="flex size-5 items-center justify-center rounded-full text-white" style={{ background: theme.blue }}><Plus size={14} strokeWidth={3} /></span>
        {text}
      </div>
    </Abs>
  )
}
