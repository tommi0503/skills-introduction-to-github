import { ImagePlaceholder, cn } from '../../../ui'

/** Claude asterisk brand mark → placeholder. */
export function ClaudeMark({ size = 36, className }: { size?: number; className?: string }) {
  return <ImagePlaceholder label="Claude logo" className={cn('rounded-full', className)} style={{ width: size, height: size }} />
}
