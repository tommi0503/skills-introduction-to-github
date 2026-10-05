import { ImagePlaceholder } from '../../../ui'

export interface AlbumStackProps {
  coverLabel: string
  tint: string
  /** How many ghost covers fan out behind the front one. */
  layers?: number
}

/** Front cover (placeholder) with progressively fainter covers peeking out on the right. */
export function AlbumStack({ coverLabel, tint, layers = 3 }: AlbumStackProps) {
  return (
    <div className="relative h-[163px] w-[162px]">
      {Array.from({ length: layers }, (_, i) => layers - i).map((depth) => (
        <span
          key={depth}
          className="absolute top-0 h-[163px] w-[162px] rounded-[20px]"
          style={{
            left: depth * 20,
            transform: `scale(${1 - depth * 0.085})`,
            transformOrigin: 'right center',
            background: tint,
            opacity: 0.85 - depth * 0.2,
          }}
        />
      ))}
      <div className="absolute inset-0 rounded-[20px] border-[2px] border-white p-0 overflow-hidden">
        <ImagePlaceholder label={coverLabel} className="h-full w-full" />
      </div>
    </div>
  )
}
