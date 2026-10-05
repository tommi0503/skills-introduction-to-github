import { BulletList, ImagePlaceholder } from '../../../ui'
import { concertTheme as t } from '../theme'

export interface Artist {
  role: string
  name: string
  notes: string[]
  /** Which side the rounded cap and portrait sit on. */
  side: 'left' | 'right'
  /** Band position within the panel. */
  y: number
  /** Text column x relative to the band's left edge. */
  textX: number
}

export interface ArtistCardProps {
  artist: Artist
  panelWidth: number
  inset: number
  height: number
  photoSize: number
}

/** Cream half-capsule band with a round portrait and role / name / bullet notes. */
export function ArtistCard({ artist, panelWidth, inset, height, photoSize }: ArtistCardProps) {
  const left = artist.side === 'left'
  const width = panelWidth - inset
  const r = height / 2
  const photoPad = (height - photoSize) / 2
  return (
    <div
      className="absolute"
      style={{
        left: left ? inset : 0,
        top: artist.y,
        width,
        height,
        background: t.cream,
        borderRadius: left ? `${r}px 0 0 ${r}px` : `0 ${r}px ${r}px 0`,
      }}
    >
      <ImagePlaceholder
        className="absolute rounded-full"
        style={{ top: photoPad, width: photoSize, height: photoSize, ...(left ? { left: photoPad + 1 } : { right: photoPad + 7 }) }}
        label={`${artist.name} portrait`}
      />
      <div className="absolute" style={{ left: artist.textX, top: 44 }}>
        <div className="flex items-baseline gap-[12px] whitespace-nowrap">
          <span className="text-[20px] font-semibold" style={{ color: t.ink }}>
            {artist.role}
          </span>
          <span className={`${t.font.display} text-[31px] leading-[36px]`} style={{ color: t.heading }}>
            {artist.name}
          </span>
        </div>
        <BulletList
          items={artist.notes}
          className="mt-[14px] gap-[4px]"
          itemClassName="text-[15.5px] leading-[24px]"
          markerClassName="flex h-[24px] w-[19px] items-center"
          marker={<span className="inline-block size-[5px] rounded-full bg-current" />}
        />
      </div>
    </div>
  )
}
