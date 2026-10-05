import { BulletList, cn } from '../../../ui'
import type { FestivalPalette } from '../../shared-1718/theme'
import type { ProgramDetail } from '../data'

export interface ProgramBlockProps {
  program: ProgramDetail
  palette: FestivalPalette
  className?: string
}

/** Programme description: title with trailing rule, paragraph, bullet facts. */
export function ProgramBlock({ program, palette, className }: ProgramBlockProps) {
  return (
    <article className={cn('flex flex-col', className)}>
      <header className="flex items-center gap-[24px]">
        <h3 className="m-0 shrink-0 text-[17px] font-bold leading-[24px]" style={{ color: palette.ink }}>
          {program.title}
        </h3>
        <span className="h-[2px] flex-1" style={{ background: palette.rule }} />
      </header>
      <p className="m-0 mt-[11px] break-all text-[14.8px] leading-[25px]" style={{ color: palette.inkMuted }}>
        {program.description}
      </p>
      <div className="mt-[10px]" style={{ color: palette.inkSoft }}>
        <BulletList
          items={program.bullets}
          className="whitespace-pre-wrap text-[14.5px] font-semibold leading-[25px]"
          itemClassName="gap-[9px]"
          markerClassName="pl-[12px]"
        />
      </div>
    </article>
  )
}
