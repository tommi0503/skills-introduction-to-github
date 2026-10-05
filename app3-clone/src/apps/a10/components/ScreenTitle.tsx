import { cn } from '../../../ui'

/** Large heading; each array entry is one rendered line. */
export function ScreenTitle({ lines, className }: { lines: string[]; className?: string }) {
  return (
    <h1 className={cn('absolute left-[17px] text-[29px] leading-[36px] font-semibold tracking-[-0.7px] text-[#111]', className)}>
      {lines.map((l) => (
        <span key={l} className="block">
          {l}
        </span>
      ))}
    </h1>
  )
}
