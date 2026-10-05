import { Zap } from 'lucide-react'
import { cn } from '../../../ui'
import type { TagData, TagKind } from '../data'
import { theme } from '../theme'

const styles: Record<TagKind, { className: string; style?: React.CSSProperties }> = {
  mint: { className: 'font-medium', style: { background: theme.tagMint, color: theme.tagMintText } },
  club: { className: 'font-medium', style: { border: `1px solid ${theme.club}`, color: theme.club, background: '#f3fbfa' } },
  grey: { className: '', style: { background: theme.field, color: '#4a4d52' } },
  greyMuted: { className: '', style: { background: theme.field, color: '#62666b' } },
  new: { className: '', style: { background: '#fdeef6', color: theme.pink } },
}

/** Small rounded label chip used under listings. */
export function Tag({ tag, className }: { tag: TagData; className?: string }) {
  const s = styles[tag.kind]
  return (
    <span
      className={cn('inline-flex h-[18px] shrink-0 items-center gap-[2px] rounded-[4px] px-[5px] text-[10px] leading-none tracking-[-0.3px]', s.className, className)}
      style={s.style}
    >
      {tag.kind === 'club' && <ClubMark size={11} />}
      {tag.label}
    </span>
  )
}

/** 배민클럽 mark (simple teal glyph). */
export function ClubMark({ size = 12, color = theme.club }: { size?: number; color?: string }) {
  return (
    <span className="inline-flex items-center justify-center rounded-[2px]" style={{ width: size, height: size, background: color }}>
      <Zap size={size * 0.7} color="#fff" fill="#fff" strokeWidth={1} />
    </span>
  )
}

export function TagRows({ rows, className }: { rows: TagData[][]; className?: string }) {
  return (
    <div className={cn('flex flex-col gap-[3.5px]', className)}>
      {rows.map((row, i) => (
        <div key={i} className="flex gap-[4px] whitespace-nowrap">
          {row.map((t) => (
            <Tag key={t.label} tag={t} />
          ))}
        </div>
      ))}
    </div>
  )
}
