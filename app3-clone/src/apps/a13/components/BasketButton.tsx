import { Button, cn } from '../../../ui'
import type { BasketAction } from '../data'
import { theme } from '../theme'

export function BasketButton({ action }: { action: BasketAction }) {
  const primary = action.kind === 'primary'
  return (
    <Button
      className={cn('h-[46.5px] w-full rounded-[8px] text-[15px] font-medium')}
      style={{ background: primary ? '#000' : theme.secondaryBg, color: primary ? '#fff' : '#000' }}
    >
      {action.label}
    </Button>
  )
}
