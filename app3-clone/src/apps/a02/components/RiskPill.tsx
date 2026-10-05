import { rf } from '../theme'

export function RiskPill({ label }: { label: string }) {
  return (
    <span
      className="flex h-[26px] items-center gap-[5px] rounded-full px-[9px] text-[11.5px] tracking-[-0.4px]"
      style={{ background: rf.riskBg, color: rf.riskText }}
    >
      <span className="h-[9px] w-[9px] rounded-full" style={{ background: rf.riskDot }} />
      {label}
    </span>
  )
}
