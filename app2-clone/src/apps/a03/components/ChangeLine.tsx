import { ArrowUpRight, Info } from 'lucide-react'
import { theme } from '../theme'

/** "↗ $0.04 (0.23%) today" daily change line. */
export function ChangeLine({ value, top, info, todayColor = '#6a6a70' }: { value: string; top: number; info?: boolean; todayColor?: string }) {
  return (
    <div className="absolute flex items-center gap-[4px] text-[14px]" style={{ left: 15, top }}>
      <ArrowUpRight size={15} strokeWidth={2.2} color={theme.green} />
      <span className="font-semibold" style={{ color: theme.green }}>
        {value}
      </span>
      <span style={{ color: todayColor }}>today</span>
      {info && <Info size={12} strokeWidth={1.6} color="#9a9aa0" />}
    </div>
  )
}
