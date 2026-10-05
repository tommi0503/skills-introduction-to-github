import { Avatar } from '../../../ui'

/** Pet photo pin on a map: white ringed circle with a small pointer. */
export function PetMarker({ size = 52, className, style }: { size?: number; className?: string; style?: React.CSSProperties }) {
  return (
    <div className={className} style={style}>
      <div className="relative rounded-full bg-white p-[3px] shadow-[0_2px_6px_rgba(0,0,0,0.18)]" style={{ width: size, height: size }}>
        <Avatar size={size - 6} />
        <span className="absolute -bottom-[5px] left-1/2 h-[10px] w-[10px] -translate-x-1/2 rotate-45 bg-white" />
      </div>
    </div>
  )
}
