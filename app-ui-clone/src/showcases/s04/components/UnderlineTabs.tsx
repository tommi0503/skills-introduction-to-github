import { cn } from '../../../ui'

export interface UnderlineTabsProps {
  tabs: string[]
  active: string
  className?: string
}

/** Horizontally scrolling text tabs; the active one is dark and underlined. */
export function UnderlineTabs({ tabs, active, className }: UnderlineTabsProps) {
  return (
    <div className={cn('flex border-b border-[#eeeeee]', className)}>
      {tabs.map((t) => (
        <span
          key={t}
          className={cn(
            'relative whitespace-nowrap pb-[9px] text-[14.5px]',
            t === active ? 'text-[#1c1c1c]' : 'text-[#7a7a7a]',
          )}
        >
          {t}
          {t === active && <span className="absolute -inset-x-[1px] -bottom-[1px] h-[2px] bg-[#1c1c1c]" />}
        </span>
      ))}
    </div>
  )
}
