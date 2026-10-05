import { cn } from '../../../ui'
import type { TimetableEntry } from '../data'

export interface TimetableItemProps {
  entry: TimetableEntry
  titleColor: string
  lineColor: string
  className?: string
  titleClassName?: string
  lineClassName?: string
}

/** Centered programme block: bold name, then time/place and audience lines. */
export function TimetableItem({ entry, titleColor, lineColor, className, titleClassName, lineClassName }: TimetableItemProps) {
  return (
    <div className={cn('flex flex-col items-center text-center', className)}>
      <p className={cn('m-0', titleClassName)} style={{ color: titleColor }}>
        {entry.title}
      </p>
      {entry.lines.map((line) => (
        <p key={line} className={cn('m-0', lineClassName)} style={{ color: lineColor }}>
          {line}
        </p>
      ))}
    </div>
  )
}
