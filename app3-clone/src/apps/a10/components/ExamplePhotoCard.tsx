import { CircleCheck, CircleX } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { ExamplePhoto } from '../data'
import { theme } from '../theme'

/** Verdict icon above a photo example. */
export function ExamplePhotoCard({ photo }: { photo: ExamplePhoto }) {
  const Icon = photo.verdict === 'good' ? CircleCheck : CircleX
  return (
    <div className="flex w-[165px] flex-col items-center">
      <Icon size={16} strokeWidth={1.8} style={{ color: photo.verdict === 'good' ? theme.ok : theme.bad }} />
      <ImagePlaceholder className="mt-[11px] h-[234px] w-full" label={photo.label} />
    </div>
  )
}
