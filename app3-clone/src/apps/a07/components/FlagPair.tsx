import { ImagePlaceholder } from '../../../ui'

/** Two overlapping round currency flags (flags are imagery → placeholders). */
export function FlagPair({ size = 26 }: { size?: number }) {
  return (
    <div className="relative" style={{ width: size + 10, height: size + 12 }}>
      <ImagePlaceholder tone="#f3f4f6" className="absolute top-0 left-0 rounded-full" style={{ width: size, height: size }} label="SGD flag" />
      <ImagePlaceholder
        className="absolute right-0 bottom-0 rounded-full border-2"
        style={{ width: size + 4, height: size + 4, borderColor: '#1e2038' }}
        label="USD flag"
      />
    </div>
  )
}
