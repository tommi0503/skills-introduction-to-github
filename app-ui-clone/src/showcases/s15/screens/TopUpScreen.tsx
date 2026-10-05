import { ChevronDown } from 'lucide-react'
import { BigAmount } from '../components/BigAmount'
import { InvestPhone } from '../components/InvestPhone'
import { Keypad } from '../components/Keypad'
import { Pill } from '../components/Pill'
import { RecipientRow } from '../components/RecipientRow'
import { ScreenHeader } from '../components/ScreenHeader'
import { keypad, topUp } from '../data'
import { theme } from '../theme'

/** Top-up flow: amount, currency, recipient, presets and keypad. */
export function TopUpScreen() {
  const t = topUp
  return (
    <InvestPhone background={theme.topUpScreen}>
      <ScreenHeader title={t.title} />
      <BigAmount value={t.amount} className="absolute inset-x-0 top-[160px]" />
      <span className="absolute left-[165px] top-[250px] flex h-[27px] w-[63px] items-center justify-center gap-[3px] rounded-full bg-white text-[11px] text-[#9a9aa0]">
        {t.currency}
        <ChevronDown size={12} strokeWidth={2} />
      </span>
      <div className="absolute inset-x-[22px] top-[310px]">
        <RecipientRow recipient={t.recipient} />
      </div>
      <div className="absolute inset-x-[22px] top-[403px] flex justify-between">
        {t.presets.map((p) => (
          <Pill key={p} active={p === t.activePreset} className="h-[47px] w-[64px] text-[12px]">
            {p}
          </Pill>
        ))}
      </div>
      <div className="absolute inset-x-[22px] top-[478px]">
        <Keypad keys={keypad} />
      </div>
    </InvestPhone>
  )
}
