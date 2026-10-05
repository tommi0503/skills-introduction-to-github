import { Check } from 'lucide-react'

/** Filled green check circle + label. */
export function CheckRow({ label, color = '#4fa460' }: { label: string; color?: string }) {
  return (
    <div className="flex items-center">
      <span className="flex items-center justify-center rounded-full" style={{ width: 22.7, height: 22.7, background: color }}>
        <Check size={15} strokeWidth={2.8} color="#fff" />
      </span>
      <span style={{ marginLeft: 8, fontSize: 15.5, color: '#1a191e', letterSpacing: -0.4 }}>{label}</span>
    </div>
  )
}
