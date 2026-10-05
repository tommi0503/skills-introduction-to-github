import { palette as c } from '../theme'

/** Collapsed search step: label on the left, call-to-action value on the right. */
export function FieldCard({ label, value }: { label: string; value: string }) {
  return (
    <div
      className="flex h-[58px] items-center justify-between rounded-[16px] bg-white px-[20px]"
      style={{ boxShadow: '0 4px 14px rgba(0,0,0,0.07)' }}
    >
      <span className="text-[13px] font-medium" style={{ color: c.muted }}>
        {label}
      </span>
      <span className="text-[13.5px] font-semibold" style={{ color: c.text }}>
        {value}
      </span>
    </div>
  )
}
