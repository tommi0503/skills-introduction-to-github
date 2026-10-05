import { ImagePlaceholder } from '../../../ui'
import { stats } from '../data'
import { theme } from '../theme'

const columnWidths = [424, 424, 384]

export function Stats() {
  return (
    <section
      className="mx-auto mt-[119px] flex border-y py-[40px]"
      style={{ width: theme.content, borderColor: theme.rule, color: theme.ink }}
    >
      {stats.map((s, i) => (
        <div
          key={s.value}
          className="h-[100px]"
          style={{ width: columnWidths[i], ...(i > 0 ? { borderLeft: `1px solid ${theme.rule}`, paddingLeft: 40 } : null) }}
        >
          <div className="pt-[11px] text-[48px] font-[450] leading-[48px] tracking-[-0.48px]">{s.value}</div>
          <div className="mt-[22px] flex items-center gap-[8px] text-[14px] font-[450] leading-5" style={{ color: theme.muted }}>
            {s.label}
            {s.logo && <ImagePlaceholder label="Colossus wordmark" style={{ width: 109, height: 8 }} />}
          </div>
        </div>
      ))}
    </section>
  )
}
