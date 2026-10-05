/** Two-line "sidebar" glyph (long over short). */
export function MenuGlyph({ x, y }: { x: number; y: number }) {
  return (
    <div className="absolute flex flex-col gap-[7px]" style={{ left: x, top: y }}>
      <span className="h-[1.8px] w-[17px] rounded-full bg-[#111]" />
      <span className="h-[1.8px] w-[11px] rounded-full bg-[#111]" />
    </div>
  )
}
