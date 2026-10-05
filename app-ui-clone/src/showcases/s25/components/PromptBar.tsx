import type { CSSProperties, ReactNode } from 'react'
import { Sparkles } from 'lucide-react'
import { cn } from '../../../ui'

export interface PromptBarProps {
  text: string
  /** Render the text as a greyed placeholder. */
  placeholder?: boolean
  trailing?: ReactNode
  className?: string
  style?: CSSProperties
}

/** White pill input with a sparkle glyph — the app's AI "discover" field. */
export function PromptBar({ text, placeholder, trailing, className, style }: PromptBarProps) {
  return (
    <div
      className={cn('flex h-[53px] items-center rounded-full bg-white pr-[8px] pl-[16px]', className)}
      style={{ boxShadow: '0 4px 16px rgba(0,0,0,0.07)', ...style }}
    >
      <Sparkles size={23} strokeWidth={1.4} className="shrink-0 text-[#8a8a8a]" />
      <span
        className={cn('ml-[10px] flex-1 truncate', placeholder ? 'text-[15.3px] text-[#b8b8b8]' : 'text-[16px] text-[#111]')}
        style={{ letterSpacing: -0.2 }}
      >
        {text}
      </span>
      {trailing}
    </div>
  )
}

export interface CountPillProps {
  count: string
  className?: string
}

/** Grey pill with a cloud glyph + count ("memories"). */
export function CountPill({ count, className }: CountPillProps) {
  return (
    <div className={cn('flex h-[34px] items-center gap-[6px] rounded-full bg-[#ececec] px-[12px]', className)}>
      <CloudGlyph />
      <span className="text-[14px] font-medium text-[#555]">{count}</span>
    </div>
  )
}

/** Small filled cloud built from circles (UI glyph, not a logo). */
export function CloudGlyph({ color = '#c9c9c9', size = 1 }: { color?: string; size?: number }) {
  return (
    <span className="relative inline-block" style={{ width: 20 * size, height: 14 * size }}>
      <span className="absolute rounded-full" style={{ background: color, left: 0, top: 5 * size, width: 10 * size, height: 9 * size }} />
      <span className="absolute rounded-full" style={{ background: color, left: 4 * size, top: 0, width: 11 * size, height: 11 * size }} />
      <span className="absolute rounded-full" style={{ background: color, left: 10 * size, top: 4 * size, width: 10 * size, height: 10 * size }} />
    </span>
  )
}
