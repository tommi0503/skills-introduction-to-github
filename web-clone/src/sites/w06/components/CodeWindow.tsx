import { Copy } from 'lucide-react'
import { cn } from '../../../ui'
import type { CodeLine } from '../data'
import { syntax, theme } from '../theme'

export interface CodeWindowProps {
  lines: CodeLine[]
  className?: string
}

const dots = ['#ff5f57', '#febc2e', '#28c840']

/** White editor window with traffic lights, copy action and syntax-highlighted code. */
export function CodeWindow({ lines, className }: CodeWindowProps) {
  return (
    <div className={cn('overflow-hidden rounded-[12px] bg-white', className)}>
      <div className="flex h-10 items-center justify-between border-b border-[#f0f0f0] px-[16px]">
        <div className="flex gap-[7px]">
          {dots.map((c) => (
            <span key={c} className="size-[10px] rounded-full" style={{ background: c }} />
          ))}
        </div>
        <span className="flex items-center gap-[6px] text-[12px] font-[450] leading-4 text-black/60">
          <Copy size={13} strokeWidth={1.6} />
          Copy
        </span>
      </div>
      <pre className={cn('px-[12px] pt-[12px] text-[13px] leading-[24px]', theme.mono)}>
        {lines.map((line, i) => (
          <div key={i}>
            {line.map(([text, tok], j) => (
              <span key={j} style={{ color: syntax[tok] }}>
                {text}
              </span>
            ))}
          </div>
        ))}
      </pre>
    </div>
  )
}
