import type { LucideIcon } from 'lucide-react'
import { Button } from '../../../ui'

interface PrimaryButtonProps {
  label: string
  icon: LucideIcon
}

/** Full-width black pill CTA with a trailing icon. */
export function PrimaryButton({ label, icon }: PrimaryButtonProps) {
  return (
    <Button
      trailingIcon={icon}
      iconSize={16}
      iconStrokeWidth={2.2}
      className="h-[55px] w-full gap-[15px] rounded-full bg-[#18171c] text-[15.5px] font-semibold text-white"
    >
      {label}
    </Button>
  )
}
