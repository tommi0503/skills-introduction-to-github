import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export function PillButton({ children, variant }: { children: ReactNode; variant: 'outline' | 'solid' }) {
  return (
    <div
      className={cn(
        'flex h-[58px] flex-1 items-center justify-center rounded-full text-[17px] font-medium',
        variant === 'solid' ? 'bg-black text-white' : 'border border-[#cfcfcf] bg-white text-black',
      )}
    >
      {children}
    </div>
  )
}
