export interface LabeledToggleProps {
  on: boolean
  width?: number
  height?: number
  knobInset?: number
  onColor?: string
  offColor?: string
  onLabel?: string
  offLabel?: string
}

/** Pill switch with an "ON"/"OFF" caption inside the track. */
export function LabeledToggle({
  on,
  width = 58,
  height = 31,
  knobInset = 3,
  onColor = '#44a85c',
  offColor = '#d5d5d5',
  onLabel = 'ON',
  offLabel = 'OFF',
}: LabeledToggleProps) {
  const knob = height - knobInset * 2
  return (
    <div className="relative shrink-0 rounded-full" style={{ width, height, background: on ? onColor : offColor }}>
      <span
        className="absolute top-0 flex h-full items-center font-inter font-bold text-white"
        style={{ fontSize: 12, [on ? 'left' : 'right']: 10, letterSpacing: -0.2 }}
      >
        {on ? onLabel : offLabel}
      </span>
      <span
        className="absolute rounded-full bg-white"
        style={{ width: knob, height: knob, top: knobInset, left: on ? width - knob - knobInset : knobInset }}
      />
    </div>
  )
}
