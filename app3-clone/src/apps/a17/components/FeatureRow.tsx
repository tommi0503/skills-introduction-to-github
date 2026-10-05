import type { Feature } from '../data'

export function FeatureRow({ feature }: { feature: Feature }) {
  const Icon = feature.icon
  return (
    <div className="flex h-[35px] items-center gap-[15px] text-[15px] text-[#e6e6e6]">
      <span className="flex w-[22px] justify-center">
        <Icon size={19} strokeWidth={2.2} />
      </span>
      <span>{feature.label}</span>
    </div>
  )
}
