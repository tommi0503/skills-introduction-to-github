import { Button } from '../../../ui'
import { palette as c } from '../theme'

export function CheckButton({ label, className }: { label: string; className?: string }) {
  return (
    <div className={className}>
      <Button
        className="h-[46px] w-full rounded-[14px] pb-[3px] text-[14px] font-bold tracking-[0.8px]"
        style={{ background: c.green, color: c.checkText, boxShadow: `inset 0 -4px 0 ${c.greenShadow}` }}
      >
        {label}
      </Button>
    </div>
  )
}
