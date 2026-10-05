import { cn } from '../../ui'

export interface OptionGridProps {
  options: string[]
  selected?: number
  height?: number
  radius?: number
  fontSize?: number
  borderColor?: string
  activeColor?: string
  textColor?: string
  activeWeight?: number
  weight?: number
  className?: string
  style?: React.CSSProperties
}

/**
 * Row of equally sized, joined option cells (e.g. 30만원 | 50만원 | …).
 * The selected cell draws a coloured border on top of its neighbours.
 */
export function OptionGrid({
  options,
  selected,
  height = 44,
  radius = 4,
  fontSize = 15,
  borderColor = '#e2e2e2',
  activeColor = '#43a94e',
  textColor = '#222',
  weight = 500,
  activeWeight = 600,
  className,
  style,
}: OptionGridProps) {
  return (
    <div
      className={cn('flex', className)}
      style={{ height, borderRadius: radius, border: `1px solid ${borderColor}`, ...style }}
    >
      {options.map((label, i) => {
        const active = i === selected
        return (
          <div
            key={label}
            className="relative flex flex-1 items-center justify-center"
            style={{
              fontSize,
              color: active ? activeColor : textColor,
              fontWeight: active ? activeWeight : weight,
              borderLeft: i > 0 ? `1px solid ${borderColor}` : undefined,
              letterSpacing: -0.3,
            }}
          >
            {active && (
              <span
                className="pointer-events-none absolute"
                style={{
                  inset: -1,
                  left: i > 0 ? -1 : -1,
                  border: `1.5px solid ${activeColor}`,
                  borderRadius:
                    i === 0
                      ? `${radius}px 0 0 ${radius}px`
                      : i === options.length - 1
                        ? `0 ${radius}px ${radius}px 0`
                        : 0,
                }}
              />
            )}
            {label}
          </div>
        )
      })}
    </div>
  )
}
