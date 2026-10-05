import type { CSSProperties, ReactNode } from 'react'
import { BookOpen, CupSoda, NotebookText, PersonStanding, Smartphone, Sunrise, Wind, type LucideIcon } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import type { TaskIcon, TaskTile as Tile } from '../data'

/** Rounded panel on the journey timeline; dashed while the day is in progress. */
export function JourneyPanel({
  dashed,
  className,
  style,
  children,
}: {
  dashed?: boolean
  className?: string
  style?: CSSProperties
  children?: ReactNode
}) {
  return (
    <div
      className={cn('absolute overflow-hidden rounded-[12px] bg-[#f2f2f2]', dashed && 'border-[1.5px] border-dashed border-[#555]', className)}
      style={{ width: 139, ...style }}
    >
      {children}
    </div>
  )
}

const taskIcons: Record<TaskIcon, LucideIcon> = {
  meditate: PersonStanding,
  notebook: NotebookText,
  phone: Smartphone,
  glass: CupSoda,
  wind: Wind,
  book: BookOpen,
  sunrise: Sunrise,
}

/** Square habit glyph tile (grey = pending, orange = done). */
export function TaskTile({ tile }: { tile: Tile }) {
  const Icon = taskIcons[tile.icon]
  return (
    <div
      className="flex h-[36px] w-[36px] items-center justify-center rounded-[8px] border-2 border-[#151515] text-white"
      style={{ background: tile.active ? '#e8792f' : '#8a8a8a', boxShadow: '0 2px 0 #151515' }}
    >
      <Icon size={20} strokeWidth={1.8} />
    </div>
  )
}

/** Emoji in a ring (emoji glyph itself is an image placeholder). */
export function EmojiFace({ size, ring = '#d8d8d8', border, className }: { size: number; ring?: string; border?: boolean; className?: string }) {
  return (
    <div
      className={cn('flex shrink-0 items-center justify-center rounded-full', border && 'border-[1.5px] border-[#151515]', className)}
      style={{ width: size, height: size, background: ring }}
    >
      <ImagePlaceholder tone="#f2cf5b" label="emoji" className="rounded-full" style={{ width: size * 0.66, height: size * 0.66 }} />
    </div>
  )
}

/** Day marker square + date + title. */
export function DayHeader({ date, title, current, top }: { date: string; title: string; current: boolean; top: number }) {
  return (
    <>
      <div
        className="absolute left-[18px] flex h-[45px] w-[45px] items-center justify-center rounded-[10px]"
        style={{
          top,
          background: current ? '#e8792f' : '#555',
          boxShadow: current ? '0 2px 10px rgba(232,121,47,0.45)' : '0 0 0 2px rgba(0,0,0,0.08)',
        }}
      >
        {current && <ImagePlaceholder tone="#fbe3d0" label="logo" className="h-[14px] w-[24px] rounded-[3px]" />}
      </div>
      <div className="absolute left-[88px] text-[8px] text-[#8a8a8a]" style={{ top: top + 4 }}>
        {date}
      </div>
      <div className="absolute left-[88px] text-[17px] font-bold tracking-[-0.3px]" style={{ top: top + 16 }}>
        {title}
      </div>
    </>
  )
}
