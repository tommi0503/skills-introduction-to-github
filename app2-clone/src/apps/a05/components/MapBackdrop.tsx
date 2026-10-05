import { ImagePlaceholder } from '../../../ui'

/** Map tiles (streets, parks, water, labels) → one flat placeholder. */
export function MapBackdrop({ className = 'absolute inset-0' }: { className?: string }) {
  return <ImagePlaceholder label="map" className={className} />
}
