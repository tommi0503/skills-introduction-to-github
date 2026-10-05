import { Check } from 'lucide-react'

/** Black check disc inside a partial blue progress ring (plain SVG + lucide). */
export function DeadlineBadge({ size = 32 }: { size?: number }) {
  return (
    <span className="relative flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} viewBox="0 0 32 32" className="absolute inset-0">
        <circle cx={16} cy={16} r={14.5} fill="none" stroke="#2f6fe4" strokeWidth={2.4} strokeDasharray="70 21" />
      </svg>
      <span className="flex h-[22px] w-[22px] items-center justify-center rounded-full bg-black">
        <Check size={13} strokeWidth={2.6} color="#fff" />
      </span>
    </span>
  )
}
