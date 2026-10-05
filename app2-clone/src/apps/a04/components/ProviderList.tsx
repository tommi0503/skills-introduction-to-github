import { cn } from '../../../ui'
import type { Provider } from '../data'
import { ProviderButton } from './ProviderButton'

export function ProviderList({ items, className }: { items: Provider[]; className?: string }) {
  return (
    <div className={cn('flex flex-col gap-[12.6px]', className)}>
      {items.map((p) => (
        <ProviderButton key={p.key} provider={p} />
      ))}
    </div>
  )
}
