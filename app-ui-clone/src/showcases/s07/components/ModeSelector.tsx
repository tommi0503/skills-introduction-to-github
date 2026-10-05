import { cn } from '../../../ui'

export interface ModeSelectorProps<T extends string> {
  modes: T[]
  active: T
}

/** AUTO / MANUAL / BATCH capture-mode switch. */
export function ModeSelector<T extends string>({ modes, active }: ModeSelectorProps<T>) {
  return (
    <div className="flex h-full items-center gap-[4px] rounded-[8px] p-[4px]" style={{ background: 'rgba(14,11,9,0.85)' }}>
      {modes.map((m) => (
        <span
          key={m}
          className={cn(
            'flex h-full flex-1 items-center justify-center rounded-[6px] font-spacemono text-[11.5px] font-bold tracking-[0.08em]',
            m === active ? 'bg-[#3a3633] text-white' : 'text-[#8d8780]',
          )}
        >
          {m}
        </span>
      ))}
    </div>
  )
}
