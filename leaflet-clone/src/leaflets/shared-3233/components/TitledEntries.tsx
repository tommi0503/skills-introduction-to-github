import { cn } from '../../../ui'

export interface TitledEntry {
  title: string
  body: string
}

export interface TitledEntriesProps {
  entries: TitledEntry[]
  className?: string
  titleClassName?: string
  bodyClassName?: string
  /** Vertical gap between entries (px). */
  gap?: number
}

/** "bold title / small body" blocks (Mission, Vision 2030, 비용 절감 …). */
export function TitledEntries({ entries, className, titleClassName, bodyClassName, gap = 24 }: TitledEntriesProps) {
  return (
    <div className={cn('flex flex-col', className)} style={{ rowGap: gap }}>
      {entries.map((e) => (
        <div key={e.title}>
          <p className={cn('m-0 font-bold', titleClassName)}>{e.title}</p>
          <p className={cn('m-0 whitespace-pre-line', bodyClassName)}>{e.body}</p>
        </div>
      ))}
    </div>
  )
}
