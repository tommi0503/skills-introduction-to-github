import { ImagePlaceholder } from '../../../ui'
import { logos } from '../data'
import { theme } from '../theme'

const ORIGIN_Y = 1760

/** Customer logo strip. */
export function Logos() {
  return (
    <section className="relative h-[140px]">
      <div className="absolute left-[120px] top-[34px] w-[1200px] text-center font-inter text-[12px] leading-[18px] font-light text-white/30">
        {logos.caption}
      </div>
      {logos.items.map((b) => (
        <ImagePlaceholder
          key={b.x}
          label="Customer logo"
          tone={theme.tones.logo}
          className="absolute"
          style={{ left: b.x, top: b.y - ORIGIN_Y, width: b.w, height: b.h }}
        />
      ))}
    </section>
  )
}
