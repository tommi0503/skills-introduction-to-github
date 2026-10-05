import { Camera } from 'lucide-react'
import { theme } from '../theme'

/** Blue capture button with a thin outer ring. */
export function ShutterButton({ size = 74 }: { size?: number }) {
  return (
    <div
      className="flex items-center justify-center rounded-full"
      style={{ width: size, height: size, boxShadow: `inset 0 0 0 1.5px ${theme.accent}aa`, background: '#0c0a0a' }}
    >
      <div
        className="flex items-center justify-center rounded-full text-white"
        style={{ width: size - 15, height: size - 15, background: theme.accent }}
      >
        <Camera size={25} strokeWidth={2.2} fill="white" stroke="white" className="[&>circle]:fill-[#2d5ff5]" />
      </div>
    </div>
  )
}
