interface StepProgressProps {
  total: number
  done: number
}

/** Segmented onboarding progress bar. */
export function StepProgress({ total, done }: StepProgressProps) {
  return (
    <div className="flex gap-[4px]">
      {Array.from({ length: total }, (_, i) => (
        <span key={i} className="h-[3px] flex-1 rounded-full" style={{ background: i < done ? '#1a1a1a' : '#ececec' }} />
      ))}
    </div>
  )
}
