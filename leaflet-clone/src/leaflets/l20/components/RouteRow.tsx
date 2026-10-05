import type { TransitRoute } from '../data'

export interface RouteRowProps {
  route: TransitRoute
}

/** Transit route: small blue glyph + grey lines. */
export function RouteRow({ route }: RouteRowProps) {
  const Icon = route.icon
  return (
    <div className="flex items-start">
      <span className="flex w-[52px] justify-center pt-[2px] text-[#5d84ad]">
        <Icon size={22} strokeWidth={1.8} />
      </span>
      <div className="ml-[15px] flex flex-col text-[15.5px] font-medium leading-[25.5px] tracking-[-0.02em] text-[#55595f]">
        {route.lines.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </div>
    </div>
  )
}
