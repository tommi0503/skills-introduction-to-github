import type { LucideIcon } from 'lucide-react'

/** Icon + short sentence, centred. */
export function FeatureLine({ icon: Icon, label }: { icon: LucideIcon; label: string }) {
  return (
    <div className="flex items-center justify-center gap-[4px] text-[9.5px] text-[#222]">
      <Icon size={13} strokeWidth={1.6} />
      {label}
    </div>
  )
}
