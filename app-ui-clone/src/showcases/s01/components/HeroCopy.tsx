import { ArrowRight } from 'lucide-react'

interface HeroCopyProps {
  title: string[]
  cta: string
}

/** Large white headline over the hero photo with a round-arrow call to action. */
export function HeroCopy({ title, cta }: HeroCopyProps) {
  return (
    <div className="text-white">
      {title.map((line) => (
        <div key={line} className="text-[28px] leading-[32px] font-semibold tracking-[-0.4px]">
          {line}
        </div>
      ))}
      <div className="mt-[14px] flex items-center gap-[11px]">
        <span className="flex h-[21px] w-[21px] items-center justify-center rounded-full bg-white text-[#111]">
          <ArrowRight size={12} strokeWidth={2.4} />
        </span>
        <span className="text-[14.5px] font-normal tracking-[-0.1px]">{cta}</span>
      </div>
    </div>
  )
}
