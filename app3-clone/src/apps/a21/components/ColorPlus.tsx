/** Google four-colour plus, built from four bars. */
const ARMS = [
  { color: '#ea4335', style: { left: 11, top: 0, width: 4, height: 13 } },
  { color: '#4285f4', style: { left: 13, top: 11, width: 13, height: 4 } },
  { color: '#34a853', style: { left: 11, top: 13, width: 4, height: 13 } },
  { color: '#fbbc05', style: { left: 0, top: 11, width: 13, height: 4 } },
]

export function ColorPlus({ size = 26 }: { size?: number }) {
  return (
    <div className="relative" style={{ width: size, height: size, transform: `scale(${size / 26})` }}>
      {ARMS.map((a) => (
        <span key={a.color} className="absolute rounded-[1px]" style={{ background: a.color, ...a.style }} />
      ))}
    </div>
  )
}
