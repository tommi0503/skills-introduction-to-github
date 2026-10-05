import type { CSSProperties } from 'react'
import { cn } from '../core/cn'

export interface ImagePlaceholderProps {
  className?: string
  style?: CSSProperties
  /** Override the default light grey — keep it light, flat and single-colour. */
  tone?: string
  label?: string
}

/**
 * Flat light-grey block standing in for photos, illustrations, graphic backgrounds,
 * patterns, logos, QR codes and icons lucide can't express. Never draw the image.
 * Shape (radius / clip-path) can be set through className/style to keep the silhouette.
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
