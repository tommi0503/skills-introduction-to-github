import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

/** Detected document outline with four draggable round handles. */
export function CropFrame({ handle = 22 }: { handle?: number }) {
  const pos = [
    { left: 0, top: 0 },
    { left: '100%', top: 0 },
    { left: 0, top: '100%' },
    { left: '100%', top: '100%' },
  ]
  return (
    <div className="relative h-full w-full">
      <ImagePlaceholder label="captured document" className="absolute inset-0" />
      <div className="absolute inset-0" style={{ boxShadow: `inset 0 0 0 1.2px ${theme.accent}aa` }} />
      {pos.map((p, i) => (
        <span
          key={i}
          className="absolute -translate-x-1/2 -translate-y-1/2 rounded-full"
          style={{ ...p, width: handle, height: handle, border: `3px solid ${theme.accent}`, background: 'rgba(255,255,255,0.25)' }}
        />
      ))}
    </div>
  )
}
