import type { CSSProperties, ReactNode } from 'react'
import { Apple } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface DownloadButtonProps {
  children: ReactNode
  variant?: 'light' | 'dark'
  size?: 'sm' | 'lg'
  className?: string
  style?: CSSProperties
}

/** "Download for …" button with an Apple glyph. */
export function DownloadButton({ children, variant = 'light', size = 'sm', className, style }: DownloadButtonProps) {
  const lg = size === 'lg'
  const light = variant === 'light'
  return (
    <span
      className={cn('inline-flex items-center whitespace-nowrap font-medium', lg ? 'h-16 gap-[12px] rounded-[8px] px-[24px] text-[18px]' : 'h-11 gap-[10px] rounded-[9px] px-[17px] text-[14px]', className)}
      style={{
        background: light ? `linear-gradient(to bottom, ${theme.cream}, #d9d6cf)` : '#2a2a2a',
        color: light ? theme.buttonInk : '#fff',
        boxShadow: light ? '0 1px 2px rgba(0,0,0,0.4)' : 'inset 0 0 0 1px #4a4a4a, 0 1px 2px rgba(0,0,0,0.5)',
        ...style,
      }}
    >
      <Apple size={lg ? 16 : 14} fill="currentColor" strokeWidth={1.5} />
      {children}
    </span>
  )
}
