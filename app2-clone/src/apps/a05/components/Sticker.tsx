import { cn } from '../../../ui'

/** Pink starburst "POPULAR #4 bakery" sticker. */
export function Sticker({ lines, className }: { lines: string[]; className?: string }) {
  const n = 14
  const pts = Array.from({ length: n * 2 }, (_, i) => {
    const a = (Math.PI * i) / n
    const r = i % 2 ? 41 : 50
    return `${50 + r * Math.cos(a)}% ${50 + r * Math.sin(a)}%`
  }).join(',')
  return (
    <div className={cn('absolute', className)} style={{ transform: 'rotate(-12deg)' }}>
      <div className="flex h-full w-full flex-col items-center justify-center bg-[#f4b3d8] text-center leading-none text-[#2b1525]" style={{ clipPath: `polygon(${pts})` }}>
        <span className="text-[10px] font-bold">{lines[0]}</span>
        <span className="a05-wide mt-[2px] text-[19px] font-extrabold">{lines[1]}</span>
        <span className="mt-[2px] text-[10.5px] font-semibold">{lines[2]}</span>
      </div>
    </div>
  )
}
