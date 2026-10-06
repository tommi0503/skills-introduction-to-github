import type { CSSProperties } from 'react'
import { cn } from '../core/cn'

export interface ImagePlaceholderProps {
  className?: string
  style?: CSSProperties
  /** Override the default light grey (keep it a flat, light, single colour). */
  tone?: string
  /** Accessible label describing what image would go here. */
  label?: string
}

/**
 * Flat light-grey block standing in for photos, illustrations, logos and any
 * graphic lucide can't express. Intentionally plain — never draw the image.
 */
export function ImagePlaceholder({ className, style, tone, label }: ImagePlaceholderProps) {
  return (
    <div
      role="img"
      aria-label={label ?? 'image'}
      className={cn('shrink-0 bg-placeholder', className)}
      style={{ ...(tone ? { background: tone } : null), ...style }}
    />
  )
}
