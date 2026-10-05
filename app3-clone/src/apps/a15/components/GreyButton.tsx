import { Button } from '../../../ui'
import { palette as c } from '../theme'

export function GreyButton({ label }: { label: string }) {
  return (
    <Button className="h-[32px] rounded-[8px] px-[16px] text-[12px] font-semibold" style={{ background: c.chip, color: c.text }}>
      {label}
    </Button>
  )
}
