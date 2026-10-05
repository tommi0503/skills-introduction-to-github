import { X } from 'lucide-react'
import { HomeIndicator } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { CartLineCard } from '../components/CartLineCard'
import { DarkButton } from '../components/DarkButton'
import { KitchenStatusBar } from '../components/KitchenStatusBar'
import { cart } from '../data'
import { theme } from '../theme'

/** Cart with three lines, applied promocode and totals. */
export function CartScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.canvas }}>
      <div className="absolute inset-x-0 top-0 h-[102.5px] rounded-b-[22px]" style={{ background: theme.dark }}>
        <KitchenStatusBar />
        <Box rect={{ x: 21, y: 58, w: 334, h: 28 }} className="flex items-center justify-between text-white">
          <span className="font-poppins text-[20px] font-semibold">Cart</span>
          <X size={24} strokeWidth={1.8} className="text-[#cfcfcf]" />
        </Box>
      </div>

      <Box rect={{ x: 21, y: 124, w: 333, h: 380 }} className="flex flex-col gap-[14px]">
        {cart.lines.map((l) => (
          <CartLineCard key={l.key} line={l} />
        ))}
      </Box>

      <Box rect={{ x: 21, y: 541, w: 333, h: 48 }} className="rounded-[12px] bg-white p-[7px]">
        <div className="flex h-full items-center justify-between rounded-[8px] px-[13px] font-poppins text-[13px] font-semibold" style={{ background: theme.lime, color: theme.ink }}>
          <span>{cart.code}</span>
          <span>{cart.promo}</span>
        </div>
      </Box>

      <Box rect={{ x: 21, y: 599, w: 327, h: 120 }} className="font-poppins">
        {cart.summary.map((s) => (
          <div key={s.label} className="flex h-[40px] items-center justify-between border-b text-[13px]" style={{ color: '#b0b0b0', borderColor: theme.hairline }}>
            <span>{s.label}</span>
            <span>{s.value}</span>
          </div>
        ))}
        <div className="flex h-[38px] items-end justify-between text-[17px] font-semibold" style={{ color: theme.ink }}>
          <span>{cart.total.label}</span>
          <span>{cart.total.value}</span>
        </div>
      </Box>

      <Box rect={{ x: 21, y: 728.5, w: 333, h: 44.5 }}>
        <DarkButton className="justify-center">{cart.cta}</DarkButton>
      </Box>
      <HomeIndicator width={116} bottom={6} />
    </div>
  )
}
