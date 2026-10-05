import { ImagePlaceholder } from '../../../ui'
import { logos } from '../data'
import { theme } from '../theme'

export function Logos() {
  return (
    <section className="relative h-[201px] overflow-hidden">
      <p className="pt-[24px] text-center text-[16px] leading-[23.2px]" style={{ color: theme.text82 }}>
        {logos.caption}
      </p>
      {logos.items.map((r) => (
        <ImagePlaceholder
          key={r.x}
          label="customer logo"
          tone={theme.media}
          className="absolute"
          style={{ left: r.x - theme.frameInset, top: r.y, width: r.w, height: r.h }}
        />
      ))}
    </section>
  )
}
