import { Home, MapPinHouse, Search, ShoppingCart, UserRoundCog, type LucideIcon } from 'lucide-react'

const left: { key: string; icon: LucideIcon; filled?: boolean }[] = [
  { key: 'home', icon: Home, filled: true },
  { key: 'browse', icon: MapPinHouse },
]
const right: { key: string; icon: LucideIcon }[] = [
  { key: 'cart', icon: ShoppingCart },
  { key: 'account', icon: UserRoundCog },
]

function Bubble({ icon: Icon, filled }: { icon: LucideIcon; filled?: boolean }) {
  return (
    <span className="flex h-[42px] w-[42px] items-center justify-center rounded-full bg-white shadow-[0_1px_6px_rgba(0,0,0,0.14)]">
      <Icon size={17} strokeWidth={1.7} fill={filled ? 'currentColor' : 'none'} />
    </span>
  )
}

/** Uber Eats floating bottom bar over a white fade. */
export function FloatingNav({ searchLabel }: { searchLabel: string }) {
  return (
    <div className="absolute inset-x-0 bottom-0 h-[130px] bg-gradient-to-b from-white/0 via-white/80 to-white">
      <div className="absolute inset-x-[17px] bottom-[37px] flex items-center gap-[11px]">
        {left.map((b) => (
          <Bubble key={b.key} icon={b.icon} filled={b.filled} />
        ))}
        <span className="flex h-[42px] flex-1 items-center justify-center gap-[8px] rounded-full bg-white text-[13.5px] text-[#555] shadow-[0_1px_6px_rgba(0,0,0,0.14)]">
          <Search size={15} strokeWidth={2} />
          {searchLabel}
        </span>
        {right.map((b) => (
          <Bubble key={b.key} icon={b.icon} />
        ))}
      </div>
    </div>
  )
}
