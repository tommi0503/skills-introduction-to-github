import { ImagePlaceholder } from '../../../ui'
import { gallery } from '../data'
import { theme } from '../theme'
import { Pill } from '../components/Pill'

/** "Apps that mean business" marquee of app screenshots. */
export function Gallery() {
  const { tile } = gallery
  return (
    <>
      <h2 className="absolute left-[33px] top-[1136px] m-0 w-[1360px] text-center font-inter text-[48px] leading-[50.4px] font-light tracking-[-1.6px] text-[#e9ebdf]">
        {gallery.title}
      </h2>
      {gallery.rows.map((row) =>
        Array.from({ length: Math.ceil((1440 - row.start) / tile.step) }, (_, i) => (
          <ImagePlaceholder
            key={`${row.y}-${i}`}
            label="App screenshot"
            tone={theme.tones.gallery}
            className="absolute rounded-[3px]"
            style={{ left: row.start + i * tile.step, top: row.y - 1, width: tile.w, height: tile.h }}
          />
        )),
      )}
      <Pill variant="outline" className="absolute left-[639px] top-[1640px] w-[147px]">{gallery.cta}</Pill>
    </>
  )
}
