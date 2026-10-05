import { Sparkles } from 'lucide-react'

/** Floating round assistant button with a cyan rim. */
export function SparkFab() {
  return (
    <div
      className="flex h-[80px] w-[80px] items-center justify-center rounded-full bg-white"
      style={{ boxShadow: '0 0 0 2px #57c4f5, 0 10px 18px rgba(0,0,0,0.12)' }}
    >
      <Sparkles size={30} strokeWidth={1.6} color="#4b4fd8" className="[&>path:first-child]:stroke-[#3a63e8] [&>path:not(:first-child)]:stroke-[#d33a5a]" />
    </div>
  )
}
