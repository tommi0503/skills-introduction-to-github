/** Lyft's lollipop place pin: solid head with a white hole and a short stem. */
export function PlacePin({ color, size = 17 }: { color: string; size?: number }) {
  return (
    <span className="flex flex-col items-center">
      <span className="flex items-center justify-center rounded-full" style={{ width: size, height: size, background: color }}>
        <span className="rounded-full bg-white" style={{ width: size * 0.36, height: size * 0.36 }} />
      </span>
      <span style={{ width: 2.2, height: size * 0.45, background: color }} />
    </span>
  )
}
