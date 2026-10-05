import type { ApplyStep } from '../data'

export interface StepRowProps {
  index: number
  step: ApplyStep
  height: number
}

/** Translucent numbered capsule of the application flow. */
export function StepRow({ index, step, height }: StepRowProps) {
  return (
    <div className="relative flex w-[390px] items-center rounded-[26px] bg-white/25" style={{ height }}>
      <span className="absolute left-[14px] flex h-[36px] w-[36px] items-center justify-center rounded-full bg-white text-[19px] font-bold text-[#6aa675]">
        {index + 1}
      </span>
      <div className="flex flex-1 flex-col items-center pl-[38px] font-dohyeon text-[20px] leading-[26px] text-white">
        {step.lines.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </div>
    </div>
  )
}
