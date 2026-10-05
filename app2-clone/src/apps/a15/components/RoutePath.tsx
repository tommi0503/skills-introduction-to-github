export interface RoutePathProps {
  points: Array<[number, number]>
  color: string
  width?: number
}

/** Route polyline drawn over the map placeholder (screen coordinates). */
export function RoutePath({ points, color, width = 4 }: RoutePathProps) {
  return (
    <svg className="pointer-events-none absolute inset-0" width="100%" height="100%">
      <polyline
        points={points.map((p) => p.join(',')).join(' ')}
        fill="none"
        stroke={color}
        strokeWidth={width}
        strokeLinejoin="round"
        strokeLinecap="round"
      />
    </svg>
  )
}
