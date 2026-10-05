import { Infinity as InfinityIcon, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { palette as c } from '../theme'

export function LessonHeader({ progress, color }: { progress: number; color: string }) {
  return (
    <div className="flex h-[30px] items-center pr-[24px] pl-[16px]">
      <X size={28} strokeWidth={1.8} color={c.muted} />
      <div className="relative mr-[14px] ml-[18px] h-[15px] flex-1 rounded-full" style={{ background: c.line }}>
        <div className="absolute inset-y-0 left-0 rounded-full" style={{ width: `${progress * 100}%`, background: color }}>
          <div className="mx-[8px] mt-[3px] h-[4px] rounded-full bg-white/25" />
        </div>
      </div>
      <ImagePlaceholder className="rounded-[4px]" style={{ width: 26, height: 18 }} label="energy" />
      <InfinityIcon size={22} strokeWidth={3} color={c.infinity} className="ml-[8px]" />
    </div>
  )
}
