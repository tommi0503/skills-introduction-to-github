import { cn } from '../../../ui'
import type { StreakPlan } from '../data'
import { streakPalette as c } from '../theme'
import { RadioMark } from './RadioMark'

export function StreakPlanCard({ plan, selected }: { plan: StreakPlan; selected: boolean }) {
  return (
    <div
      className={cn('relative rounded-[20px] pr-[18px] pl-[12px]')}
      style={{
        height: plan.height,
        paddingTop: plan.padTop,
        background: selected ? c.selectedBg : '#fff',
        border: selected ? `2px solid ${c.accent}` : '2px solid transparent',
        boxShadow: selected ? '0 4px 18px rgba(214,91,50,0.18)' : '0 2px 22px rgba(0,0,0,0.05)',
      }}
    >
      {plan.badge && (
        <span
          className="absolute -top-[12px] right-[17px] rounded-[7px] px-[8px] py-[3px] text-[12.5px] leading-[17px] font-semibold text-white"
          style={{ background: c.accent }}
        >
          {plan.badge}
        </span>
      )}
      <div className="flex items-center">
        <RadioMark checked={selected} size={22} color={c.accent} idle={c.radio} />
        <span className="ml-[11px] flex-1 text-[19.5px] font-semibold" style={{ color: c.text }}>
          {plan.name}
        </span>
        <span className="text-[15px] font-semibold" style={{ color: c.text }}>
          {plan.price}
        </span>
      </div>
      <div className="relative mt-[1px] ml-[33px]">
        {plan.lines.map((l) => (
          <div
            key={l.text}
            className={l.strong ? 'mt-[2px] text-[15px] leading-[22px]' : 'text-[14.5px] leading-[19px]'}
            style={{ color: l.strong ? c.text : c.muted }}
          >
            {l.text}
          </div>
        ))}
        {plan.strike && (
          <span className="absolute top-0 right-0 text-[14.5px] leading-[19px] line-through" style={{ color: c.muted }}>
            {plan.strike}
          </span>
        )}
      </div>
    </div>
  )
}
