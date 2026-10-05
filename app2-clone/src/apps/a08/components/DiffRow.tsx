import { Rocket, UnfoldVertical } from 'lucide-react'
import type { DiffLine, Token } from '../data'
import { gh } from '../theme'

export const DIFF_ROW = 23.6
const EXPANDABLE_HUNK = 32
const GUTTER = 38

const palette = {
  del: { row: gh.diff.delRow, gutter: gh.diff.delGutter, mark: gh.diff.delMark, sign: '-' },
  add: { row: gh.diff.addRow, gutter: gh.diff.addGutter, mark: gh.diff.addMark, sign: '+' },
  ctx: { row: '#ffffff', gutter: gh.diff.ctxGutter, mark: 'transparent', sign: ' ' },
} as const

function TokenSpan({ token, mark }: { token: Token; mark: string }) {
  switch (token.role) {
    case 'heading':
      return <span style={{ color: gh.diff.heading }}>{token.t}</span>
    case 'link':
      return <span className="underline decoration-[#8a93a6] underline-offset-[2px]" style={{ color: '#3d4a6b' }}>{token.t}</span>
    case 'mark':
      return <span style={{ background: mark }}>{token.t}</span>
    case 'icon':
      return <Rocket size={14} strokeWidth={2} className="inline -translate-y-[1px] text-[#d0453a]" />
    default:
      return <span>{token.t}</span>
  }
}

/** One unified-diff line: tinted gutter with line number + monospace code. */
export function DiffRow({ line }: { line: DiffLine }) {
  if (line.kind === 'hunk') {
    return (
      <div className="flex items-center" style={{ height: line.expandable ? EXPANDABLE_HUNK : DIFF_ROW, background: gh.diff.hunk, color: gh.diff.hunkText }}>
        <span className="flex justify-center" style={{ width: GUTTER }}>
          {line.expandable && <UnfoldVertical size={15} strokeWidth={2} />}
        </span>
        <span className="pl-[9px]">{line.tokens[0].t}</span>
      </div>
    )
  }
  const p = palette[line.kind]
  return (
    <div className="flex items-center whitespace-pre" style={{ height: DIFF_ROW, background: p.row }}>
      <span
        className="flex h-full shrink-0 items-center justify-center"
        style={{ width: GUTTER, background: p.gutter, color: gh.diff.lineNo }}
      >
        {line.no}
      </span>
      <span className="pl-[5px] text-[#1f2328]">
        {(line.kind !== 'ctx' || line.tokens.length > 0) && p.sign}
        {line.tokens.map((t, i) => (
          <TokenSpan key={i} token={t} mark={p.mark} />
        ))}
      </span>
    </div>
  )
}
