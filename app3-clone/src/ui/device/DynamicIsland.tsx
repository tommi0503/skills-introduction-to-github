import { cn } from '../core/cn'

export interface DynamicIslandProps {
  width?: number
  height?: number
  top?: number
  className?: string
}

/** iPhone dynamic island pill, centred horizontally (logical units). */
export function DynamicIsland({ width = 124, height = 36, top = 11, className }: DynamicIslandProps) {
  return (
    <div
      className={cn('absolute left-1/2 z-50 -translate-x-1/2 rounded-full bg-black', className)}
      style={{ width, height, top }}
    />
  )
}
