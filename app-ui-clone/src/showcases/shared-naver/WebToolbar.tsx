import { ChevronLeft, ChevronRight, RotateCw, X, type LucideIcon } from 'lucide-react'
import { HomeIndicator, cn } from '../../ui'

export interface ToolbarAction {
  icon: LucideIcon
  disabled?: boolean
  /** Horizontal centre (logical px). */
  x: number
  size?: number
  strokeWidth?: number
}

const DEFAULT_ACTIONS: ToolbarAction[] = [
  { icon: ChevronLeft, x: 38, size: 33 },
  { icon: ChevronRight, x: 143, size: 33, disabled: true },
  { icon: RotateCw, x: 247.5, size: 21 },
  { icon: X, x: 351.5, size: 27 },
]

export interface WebToolbarProps {
  /** Top of the toolbar (logical px). */
  top?: number
  background?: string
  color?: string
  disabledColor?: string
  /** Vertical centre of the icons relative to the toolbar top. */
  iconCenter?: number
  actions?: ToolbarAction[]
  homeIndicator?: boolean
  className?: string
}

/** In-app webview bottom bar: back / forward / reload / close + home indicator. */
export function WebToolbar({
  top = 758,
  background = '#fff',
  color = '#1f1f1f',
  disabledColor = '#d9d9d9',
  iconCenter = 27.5,
  actions = DEFAULT_ACTIONS,
  homeIndicator = true,
  className,
}: WebToolbarProps) {
  return (
    <div className={cn('absolute inset-x-0 bottom-0 z-30', className)} style={{ top, background, boxShadow: '0 -1px 0 rgba(0,0,0,0.012)' }}>
      {actions.map(({ icon: Icon, x, size = 24, disabled, strokeWidth = (1.6 * 24) / size }, i) => (
        <Icon
          key={i}
          size={size}
          strokeWidth={strokeWidth}
          className="absolute"
          style={{ left: x - size / 2, top: iconCenter - size / 2, color: disabled ? disabledColor : color }}
        />
      ))}
      {homeIndicator && <HomeIndicator width={138} bottom={7.5} className="!h-[4.5px]" />}
    </div>
  )
}
