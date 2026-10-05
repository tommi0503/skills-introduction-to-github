import { ImagePlaceholder } from '../../../ui'
import { kr } from '../theme'

export interface MannerTempProps {
  value: string
  /** 0..1 fill of the gauge. */
  level: number
  label: string
}

/** Karrot "manner temperature": value, gauge bar, face glyph and underlined caption. */
export function MannerTemp({ value, level, label }: MannerTempProps) {
  return (
    <div className="flex flex-col items-end">
      <div className="flex items-start gap-[8px]">
        <div className="flex flex-col items-end">
          <span className="text-[15px] leading-[18px] font-bold" style={{ color: kr.temp }}>
            {value}
          </span>
          <span className="mt-[5px] h-[3px] w-[49px] overflow-hidden rounded-full bg-[#e8e9eb]">
            <span className="block h-full rounded-full" style={{ width: `${level * 100}%`, background: kr.temp }} />
          </span>
        </div>
        <ImagePlaceholder className="mt-[1px] h-[24px] w-[24px] rounded-full" label="manner face" />
      </div>
      <span className="mt-[9px] text-[11px] underline" style={{ color: kr.sub }}>
        {label}
      </span>
    </div>
  )
}
