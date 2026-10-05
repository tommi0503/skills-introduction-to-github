/** Thick grey separator between Airbnb sections. */
export function SectionBand({ color, height = 7 }: { color: string; height?: number }) {
  return <div style={{ height, background: color }} />
}
