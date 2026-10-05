import { Play } from 'lucide-react'

/** White disc with a filled black play glyph. */
export function PlayButton({ size = 56, iconSize = 20 }: { size?: number; iconSize?: number }) {
  return (
    <span
      className="flex shrink-0 items-center justify-center rounded-full bg-white text-[#111]"
      style={{ width: size, height: size }}
    >
      <Play size={iconSize} strokeWidth={2.4} fill="currentColor" className="ml-[3px] rounded-[2px]" />
    </span>
  )
}
