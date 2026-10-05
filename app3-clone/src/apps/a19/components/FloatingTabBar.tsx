import { CircleUserRound, Compass, Search } from 'lucide-react'

/** Glassy pill tab bar; first tab is the custom "agenda" glyph. */
export function FloatingTabBar() {
  return (
    <div
      className="absolute top-[765px] left-[20px] flex h-[61px] w-[349px] items-center justify-between rounded-full bg-white/75 pr-[39px] pl-[40px] backdrop-blur-md"
      style={{ boxShadow: '0 4px 24px rgba(0,0,0,0.12)' }}
    >
      <span className="flex flex-col gap-[3px]">
        <span className="h-[8px] w-[24px] rounded-[2px] bg-black" />
        <span className="h-[8px] w-[24px] rounded-[2px] bg-black" />
      </span>
      <Compass size={22} strokeWidth={1.8} color="#1e2035" />
      <Search size={23} strokeWidth={2} color="#111" />
      <CircleUserRound size={24} strokeWidth={1.8} color="#111" />
    </div>
  )
}
