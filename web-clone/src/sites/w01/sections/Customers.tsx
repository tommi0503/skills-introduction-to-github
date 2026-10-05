import { ImagePlaceholder } from '../../../ui'
import { Column } from '../components/Column'
import { customers } from '../data'
import { serifStyle, theme } from '../theme'

const ROWS = [139, 143]

export function Customers() {
  const border = `1px solid ${theme.rule}`
  return (
    <Column height={356}>
      <p className="absolute left-[48px] top-[24px] text-[16px] leading-[26px] font-medium" style={{ color: theme.muted }}>
        {customers.lead} <span style={{ color: theme.ink }}>{customers.leadStrong}</span>
      </p>
      <div className="absolute inset-x-0 top-[74px] flex" style={{ borderTop: border }}>
        <div className="relative h-[282px] w-[320px]" style={{ background: theme.panel, borderRight: border }}>
          <ImagePlaceholder label="ranking badge" className="absolute left-[48px] top-[48px] size-[32px]" />
          <p className={`${theme.fonts.serif} absolute left-[48px] top-[112px]`} style={{ ...serifStyle(26), color: theme.ink }}>
            {customers.stat.title}
          </p>
          <p className="absolute left-[48px] top-[170px] w-[223px] text-[16px] leading-[21.6px]" style={{ color: theme.muted }}>
            {customers.stat.body}
          </p>
        </div>
        <div className="grid flex-1" style={{ gridTemplateColumns: `repeat(4, 1fr)`, gridTemplateRows: ROWS.map((r) => `${r}px`).join(' ') }}>
          {customers.logos.map(([w, h], i) => (
            <div
              key={i}
              className="flex items-center justify-center"
              style={{ borderRight: i % 4 < 3 ? border : undefined, borderBottom: i < 4 ? border : undefined }}
            >
              <ImagePlaceholder label="customer logo" style={{ width: w, height: h }} />
            </div>
          ))}
        </div>
      </div>
    </Column>
  )
}
