import { cn } from '../../../ui'

export interface CodeBoxesProps {
  /** Box counts per group; groups are separated by `separator`. */
  groups: number[]
  boxClassName: string
  activeClassName?: string
  /** Index of the focused box. */
  active?: number
  gap: number
  separator?: string
  separatorClassName?: string
  caretColor?: string
  className?: string
}

/** Row of one-time-code input cells. */
export function CodeBoxes({
  groups,
  boxClassName,
  activeClassName,
  active = 0,
  gap,
  separator,
  separatorClassName,
  caretColor,
  className,
}: CodeBoxesProps) {
  let index = 0
  return (
    <div className={cn('flex items-center', className)} style={{ gap }}>
      {groups.map((count, g) => (
        <div key={g} className="contents">
          {g > 0 && separator && <span className={separatorClassName}>{separator}</span>}
          {Array.from({ length: count }, () => {
            const i = index++
            const isActive = i === active
            return (
              <div key={i} className={cn('flex items-center justify-center', boxClassName, isActive && activeClassName)}>
                {isActive && caretColor && <span className="h-[20px] w-[2px]" style={{ background: caretColor }} />}
              </div>
            )
          })}
        </div>
      ))}
    </div>
  )
}
