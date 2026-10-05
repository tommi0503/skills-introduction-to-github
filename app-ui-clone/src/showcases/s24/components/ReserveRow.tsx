import { cn } from '../../../ui'
import type { IconLabel } from '../data'
import { theme } from '../theme'

export interface ReserveRowProps {
  title: string
  actions: IconLabel[]
  className?: string
}

/** "타다 예약하기" header with airport / hourly shortcuts. */
export function ReserveRow({ title, actions, className }: ReserveRowProps) {
  return (
    <div className={cn('flex h-[30px] items-center px-[26px] font-pretendard', className)}>
      <span className="text-[15.6px] font-bold tracking-[-0.3px]" style={{ color: theme.navy }}>
        {title}
      </span>
      <div className="ml-auto flex items-center">
        {actions.map(({ icon: Icon, label }, i) => (
          <div key={label} className="flex items-center">
            {i > 0 && <span className="mx-[15px] h-[12px] w-px bg-[#e3e3e8]" />}
            <Icon size={15} strokeWidth={1.6} color={i === 0 ? '#5aa2e6' : '#7a80a0'} />
            <span className="ml-[7px] text-[13.2px] tracking-[-0.2px]" style={{ color: theme.ink }}>
              {label}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
