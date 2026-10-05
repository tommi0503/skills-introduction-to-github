import { ImagePlaceholder } from '../../../ui'
import { concertTheme as t } from '../../shared-1516/theme'
import type { GuideItem } from '../data'

/** Guide pictogram: a lucide icon when one exists, otherwise a placeholder of the pictogram's silhouette. */
export function GuideIcon({ item, size }: { item: GuideItem; size: number }) {
  if (item.icon) {
    const Icon = item.icon
    return <Icon size={size} strokeWidth={2.4} color={t.heading} />
  }
  const shape = item.iconShape === 'pin' ? { borderRadius: '50% 50% 50% 0', transform: 'rotate(-45deg) scale(0.8)' } : { borderRadius: 6 }
  return <ImagePlaceholder style={{ width: size - 4, height: size - 4, ...shape }} label={`${item.title} icon`} />
}
