import type { CSSProperties } from 'react'
import { cn } from '../../../ui'
import type { InfoSection } from '../data'

interface InfoBoxProps {
  sections: InfoSection[]
  className?: string
  style?: CSSProperties
}

/** Rounded grey card holding heading + lines sections (기부 방법 / 계좌번호). */
export function InfoBox({ sections, className, style }: InfoBoxProps) {
  return (
    <div className={cn('flex flex-col items-center rounded-[22px] border-2 border-[#1f1f1f] text-center', className)} style={style}>
      {sections.map((s, i) => (
        <section key={s.heading} className={cn('flex flex-col items-center', i > 0 && 'mt-[52px]')}>
          <h3 className="m-0 text-[26px] font-semibold leading-none tracking-[0.12em] text-[#1a1a1a]">{s.heading}</h3>
          <div className={cn('mt-[24px] flex flex-col text-[17px] leading-none text-[#222]', i === 0 ? 'gap-[24px]' : 'gap-[12px]')}>
            {s.lines.map((l) => (
              <p key={l} className="m-0">{l}</p>
            ))}
          </div>
        </section>
      ))}
    </div>
  )
}
