import { ImagePlaceholder, cn } from '../../../ui'
import { theme } from '../theme'

/** Filter preset preview with caption; the selected one gets an accent ring. */
export function FilterThumb({ label, selected, size }: { label: string; selected: boolean; size: number }) {
  return (
    <div className="flex flex-col items-center gap-[11px]">
      <div
        className="rounded-[8px] p-[3px]"
        style={{ width: size, height: size, boxShadow: selected ? `inset 0 0 0 2.2px ${theme.accent}` : `inset 0 0 0 1px ${theme.hairline}` }}
      >
        <ImagePlaceholder label={`${label} preview`} className="h-full w-full rounded-[5px]" />
      </div>
      <span
        className={cn('font-plexmono text-[9.5px] leading-none font-medium tracking-[0.1em]')}
        style={{ color: selected ? theme.accent : '#8c8a85' }}
      >
        {label}
      </span>
    </div>
  )
}
