import { ImagePlaceholder } from '../../../ui'

/** One store logo, or two overlapping group-order avatars. */
export function AvatarStack({ count }: { count: 1 | 2 }) {
  if (count === 1) return <ImagePlaceholder className="my-[2px] rounded-full" style={{ width: 64, height: 64 }} label="store logo" />
  return (
    <div className="relative" style={{ width: 64, height: 66 }}>
      <ImagePlaceholder className="absolute rounded-full" style={{ left: 0, top: 0, width: 40, height: 40 }} label="avatar" />
      <ImagePlaceholder
        className="absolute rounded-full"
        style={{ left: 24, top: 26, width: 40, height: 40, outline: '2px solid #fff' }}
        label="avatar"
      />
    </div>
  )
}
