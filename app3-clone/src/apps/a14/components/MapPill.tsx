import { Map } from 'lucide-react'

export function MapPill({ label, className }: { label: string; className?: string }) {
  return (
    <div className={className}>
      <div className="flex h-[43px] w-[96px] items-center justify-center gap-[8px] rounded-full bg-[#222] text-[13px] font-semibold text-white">
        {label}
        <Map size={17} strokeWidth={2} fill="#fff" color="#222" />
      </div>
    </div>
  )
}
