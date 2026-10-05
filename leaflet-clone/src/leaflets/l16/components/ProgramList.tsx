import { concertTheme as t } from '../../shared-1516/theme'
import type { ProgramPart } from '../data'

/** One programme part: serif part title followed by composer / piece / note entries. */
export function ProgramList({ part }: { part: ProgramPart }) {
  return (
    <div className="flex flex-col items-center text-center">
      <div className={`${t.font.serif} text-[24px] leading-[32px]`} style={{ color: t.onDark }}>
        {part.title}
      </div>
      <div className="mt-[20px] flex flex-col gap-[31px]">
        {part.pieces.map((p) => (
          <div key={p.title} className="flex flex-col">
            <div className="text-[12.5px] leading-[20px]" style={{ color: t.onDarkMuted }}>
              {p.composer}
            </div>
            <div className="mt-[3.5px] text-[17px] font-semibold leading-[27px]" style={{ color: t.onDark }}>
              {p.title}
            </div>
            {p.note && (
              <div className="mt-[2.5px] text-[12px] leading-[20px]" style={{ color: t.onDarkMuted }}>
                {p.note}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
