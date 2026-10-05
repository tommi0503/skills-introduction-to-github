import { X } from 'lucide-react'
import { BrandMark } from './BrandMark'
import { CircleButton } from './CircleButton'
import { StepProgress } from './StepProgress'

interface FlowHeaderProps {
  step: number
  total: number
}

/** Planner flow header: logo, close button and step progress underneath. */
export function FlowHeader({ step, total }: FlowHeaderProps) {
  return (
    <div>
      <div className="flex items-center justify-between">
        <BrandMark />
        <CircleButton icon={X} iconSize={19} />
      </div>
      <div className="mt-[22px]">
        <StepProgress total={total} done={step} />
      </div>
    </div>
  )
}
