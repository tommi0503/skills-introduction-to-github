/** Graph-paper backdrop: flat paper colour with 1px grid lines. */
export function GridPaper({ color, line, size, offsetX = 0, offsetY = 0 }: { color: string; line: string; size: number; offsetX?: number; offsetY?: number }) {
  return (
    <div
      className="absolute inset-0"
      style={{
        backgroundColor: color,
        backgroundImage: `linear-gradient(90deg, ${line} 1px, transparent 1px), linear-gradient(0deg, ${line} 1px, transparent 1px)`,
        backgroundSize: `${size}px ${size}px`,
        backgroundPosition: `${offsetX}px ${offsetY}px`,
      }}
    />
  )
}
