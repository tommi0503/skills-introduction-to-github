import { cn } from '../../../ui'

export interface RadioProps {
  checked: boolean
  size?: number
  color?: string
  className?: string
}

/** iOS-style radio: filled ring with a white centre when checked, hairline ring otherwise. */
export function Radio({ checked, size = 24, color = '#222', className }: RadioProps) {
  return (
    <span
      className={cn('flex items-center justify-center rounded-full', className)}
      style={{
        width: size,
        height: size,
        background: checked ? color : 'transparent',
        border: checked ? 'none' : '1px solid #b0b0b0',
      }}
    >
      {checked && <span className="rounded-full bg-white" style={{ width: size * 0.33, height: size * 0.33 }} />}
    </span>
  )
}
