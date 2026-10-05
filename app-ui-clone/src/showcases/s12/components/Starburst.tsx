import type { ReactNode } from 'react'

function starPolygon(points: number, inner: number) {
  const coords: string[] = []
  for (let i = 0; i < points * 2; i++) {
    const r = i % 2 === 0 ? 50 : 50 * inner
    const a = (Math.PI * i) / points - Math.PI / 2
    coords.push(`${(50 + r * Math.cos(a)).toFixed(2)}% ${(50 + r * Math.sin(a)).toFixed(2)}%`)
  }
  return `polygon(${coords.join(', ')})`
}

/** Black zig-zag seal badge (pure CSS clip-path) with centred content. */
export function Starburst({ size, points = 14, children }: { size: number; points?: number; children: ReactNode }) {
  return (
    <div
      className="flex items-center justify-center bg-black text-white"
      style={{ width: size, height: size, clipPath: starPolygon(points, 0.8) }}
    >
      {children}
    </div>
  )
}
