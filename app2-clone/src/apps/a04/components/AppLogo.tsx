import { ImagePlaceholder, cn } from '../../../ui'

/** Notion Mail paper-plane mark (brand mark → placeholder). */
export function AppLogo({ className }: { className?: string }) {
  return <ImagePlaceholder label="Notion Mail logo" className={cn('rounded-[6px]', className)} />
}
