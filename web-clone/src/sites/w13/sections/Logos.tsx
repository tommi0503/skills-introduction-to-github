import { Plus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { logos } from '../data'
import { theme } from '../theme'

/** 4×2 customer logo grid with cross separators. */
export function Logos() {
  return (
    <>
      {logos.rows.flatMap((y, r) =>
        logos.cols.map((x, c) => {
          const [w, h] = logos.marks[r * logos.cols.length + c]
          return (
            <div key={`${r}-${c}`} className="absolute flex items-center justify-center" style={{ left: x, top: y, width: logos.w, height: logos.h }}>
              <ImagePlaceholder label="Customer logo" tone={theme.tones.logo} style={{ width: w, height: h }} />
            </div>
          )
        }),
      )}
      {logos.plus.map((x) => (
        <Plus key={x} size={20} strokeWidth={1} className="absolute top-[990px] text-[#e9ebdf]/15" style={{ left: x }} />
      ))}
    </>
  )
}
