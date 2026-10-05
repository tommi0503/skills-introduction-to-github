import { ImagePlaceholder } from '../../../ui'

/** The iridescent assistant orb — rendered as a round placeholder. */
export function AiOrb({ size }: { size: number }) {
  return <ImagePlaceholder className="rounded-full" style={{ width: size, height: size }} label="AI orb" />
}
