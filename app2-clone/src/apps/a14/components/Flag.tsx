import { ImagePlaceholder, cn } from '../../../ui'

/** Round country flag stand-in. */
export function Flag({ size, className, label }: { size: number; className?: string; label?: string }) {
  return <ImagePlaceholder label={label ?? 'flag'} className={cn('rounded-full', className)} style={{ width: size, height: size }} />
}
