import { Crown } from 'lucide-react'
import type { Feature } from '../data'
import { trialPalette as c } from '../theme'

export function FeatureRow({ feature }: { feature: Feature }) {
  return (
    <div className="flex items-center">
      <Crown size={25} fill={c.gold} color={c.gold} strokeWidth={1.2} className="ml-[3px] shrink-0" />
      <p className="ml-[22px] text-[12.5px] whitespace-pre-line leading-[17px] tracking-[-0.2px]" style={{ color: c.text }}>
        <span className="font-bold">{feature.title}</span> {feature.text}
      </p>
    </div>
  )
}
