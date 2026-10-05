import { ImagePlaceholder, cn } from '../../../ui'

export interface BrandMarkProps {
  size?: number
  tone?: string
  className?: string
  label?: string
}

/** ElevenReader / Apple / Google marks are brand artwork → flat placeholder. */
export function BrandMark({ size = 22, tone, className, label = 'logo' }: BrandMarkProps) {
  return <ImagePlaceholder label={label} tone={tone} className={cn('rounded-[4px]', className)} style={{ width: size, height: size * 0.8 }} />
}
