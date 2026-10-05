import { Gift, Sun } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { AvatarKind } from '../data'

/** 60pt round avatar for inbox rows; photos/gradients/logos are placeholders. */
export function ThreadAvatar({ kind, size = 60 }: { kind: AvatarKind; size?: number }) {
  const box = { width: size, height: size }
  if (kind === 'gift')
    return (
      <div className="flex items-center justify-center rounded-full bg-[#f1f1f1] text-[#555]" style={box}>
        <Gift size={24} strokeWidth={1.8} />
      </div>
    )
  if (kind === 'sun')
    return (
      <div className="flex items-center justify-center rounded-full bg-[#f6bd2c] text-white" style={box}>
        <Sun size={28} strokeWidth={2.2} />
      </div>
    )
  if (kind === 'number')
    return (
      <div className="flex items-center justify-center rounded-full bg-[#f1f1f1]" style={box}>
        <ImagePlaceholder className="h-[24px] w-[42px] rounded-[5px]" label="number card" />
      </div>
    )
  return <ImagePlaceholder className="rounded-full" style={box} label={kind} />
}
