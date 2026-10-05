import { theme } from '../theme'
import { Eyebrow } from './Eyebrow'

/** Listing attribute ("CONDITION" / "DIMENSIONS"). */
export function SpecTile({ label, value }: { label: string; value: string[] }) {
  return (
    <div className="flex-1 rounded-[9px] px-[16px] pt-[17px]" style={{ background: theme.surface, height: 91 }}>
      <Eyebrow className="tracking-[0.06em]">{label}</Eyebrow>
      <div className="mt-[4px] font-dm text-[15px] leading-[21.5px] font-medium" style={{ color: theme.ink }}>
        {value.map((v) => (
          <div key={v}>{v}</div>
        ))}
      </div>
    </div>
  )
}
