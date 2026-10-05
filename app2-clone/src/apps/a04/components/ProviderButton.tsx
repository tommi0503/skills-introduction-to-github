import { ImagePlaceholder, cn } from '../../../ui'
import type { Provider } from '../data'
import { theme } from '../theme'

export interface ProviderButtonProps {
  provider: Provider
  className?: string
}

/** Full-width outlined sign-in row: leading mark, centred label. */
export function ProviderButton({ provider, className }: ProviderButtonProps) {
  const Icon = provider.icon
  return (
    <div
      className={cn('relative flex h-[47px] items-center justify-center rounded-[10px] bg-white', className)}
      style={{ border: `1px solid ${theme.border}`, color: theme.text }}
    >
      <span className="absolute left-[11px] flex h-[22px] w-[22px] items-center justify-center">
        {Icon ? (
          <Icon size={21} strokeWidth={1.6} />
        ) : (
          <ImagePlaceholder label={`${provider.label} logo`} className="h-[20px] w-[20px] rounded-[4px]" />
        )}
      </span>
      <span className="text-[16px] font-medium">{provider.label}</span>
    </div>
  )
}
