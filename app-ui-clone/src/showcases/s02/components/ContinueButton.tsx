import { ChevronRight, Plane } from 'lucide-react'

/** Sticky black CTA with a white icon disc and fading chevrons. */
export function ContinueButton({ label }: { label: string }) {
  return (
    <div className="flex h-[46px] w-[189px] items-center rounded-full bg-[#1c1c1c] pl-[4px] pr-[14px] text-white shadow-[0_6px_16px_rgba(0,0,0,0.18)]">
      <span className="flex h-[38px] w-[38px] items-center justify-center rounded-full bg-white text-[#1c1c1c]">
        <Plane size={16} strokeWidth={1.8} />
      </span>
      <span className="ml-[14px] flex-1 text-[14.5px] font-medium">{label}</span>
      <span className="flex items-center">
        {[0.35, 0.6, 1].map((o) => (
          <ChevronRight key={o} size={11} strokeWidth={2.4} style={{ opacity: o }} className="-mr-[1px]" />
        ))}
      </span>
    </div>
  )
}
