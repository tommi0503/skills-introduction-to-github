import { cn } from '../../../ui'

export interface InfoEntry {
  title: string
  /** Pre-broken lines of the description. */
  lines: string[]
}

export interface InfoBlockListProps {
  items: InfoEntry[]
  className?: string
  titleClassName?: string
  bodyClassName?: string
  /** Gap between the title and its description, and between entries (px). */
  titleGap: number
  itemGap: number
}

/** Stack of "title + description" entries (주소 / 버스 이용 시, booth & programme lists). */
export function InfoBlockList({ items, className, titleClassName, bodyClassName, titleGap, itemGap }: InfoBlockListProps) {
  return (
    <div className={cn('flex flex-col', className)} style={{ gap: itemGap }}>
      {items.map((item) => (
        <div key={item.title} className="flex flex-col" style={{ gap: titleGap }}>
          <div className={titleClassName}>{item.title}</div>
          <div className={bodyClassName}>
            {item.lines.map((line) => (
              <div key={line}>{line}</div>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}
