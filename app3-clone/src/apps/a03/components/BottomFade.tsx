import { nd } from '../theme'

/** Soft fade of the scrolling content into the background behind the floating nav. */
export function BottomFade() {
  return (
    <div
      className="absolute inset-x-0 bottom-0 h-[95px]"
      style={{ background: `linear-gradient(to bottom, transparent, ${nd.bg} 70%)` }}
    />
  )
}
