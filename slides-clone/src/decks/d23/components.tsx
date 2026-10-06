import { Abs, ImagePlaceholder } from '../../ui'
import { Gem } from 'lucide-react'
import type { PillData } from './data'

export function Brand({ name }: { name: string }) {
  return (
    <div className="flex items-center gap-2 text-white">
      <Gem size={22} strokeWidth={1.6} className="opacity-70" />
      <span className="text-[22px] font-medium">{name}</span>
    </div>
  )
}

export function Pill({ label, x, y, w }: PillData) {
  return (
    <Abs x={x} y={y - 24} w={w} h={50}>
      <div className="flex h-full items-center gap-3 rounded-full bg-white px-3 shadow-[0_6px_24px_rgba(0,0,0,0.35)]">
        <ImagePlaceholder className="size-7 rounded-full" tone="#d1d5db" />
        <span className="font-manrope text-[16px] font-bold tracking-wide text-[#222]">{label}</span>
      </div>
    </Abs>
  )
}
