/** Assistant mascot reduced to plain shapes: blue speech bubble with two eyes. */
export function BotGlyph({ size = 42, color = '#7ea4f6' }: { size?: number; color?: string }) {
  const eyeW = size * 0.17
  const eyeH = size * 0.34
  return (
    <span className="relative inline-block" style={{ width: size, height: size }}>
      <span className="absolute inset-0" style={{ background: color, borderRadius: size * 0.32 }} />
      <span
        className="absolute"
        style={{ left: size * 0.12, bottom: -size * 0.12, width: size * 0.28, height: size * 0.28, background: color, transform: 'skewX(-25deg)', borderRadius: size * 0.04 }}
      />
      {[0.24, 0.56].map((x) => (
        <span
          key={x}
          className="absolute rounded-full bg-white"
          style={{ left: size * x, top: size * 0.2, width: eyeW, height: eyeH }}
        />
      ))}
      <span className="absolute rounded-full bg-white/80" style={{ left: size * 0.4, top: size * 0.62, width: size * 0.2, height: size * 0.06 }} />
    </span>
  )
}
