import { ImagePlaceholder, cn } from '../../../ui'

export function TeamLogo({ size = 14, tone, className }: { size?: number; tone?: string; className?: string }) {
  return <ImagePlaceholder label="team logo" tone={tone} className={cn('rounded-full', className)} style={{ width: size, height: size }} />
}
