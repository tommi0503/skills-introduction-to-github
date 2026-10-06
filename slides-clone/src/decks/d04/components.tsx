import { Abs } from '../../ui'
import { theme } from './theme'
import type { Step } from './data'

export function StepColumn({ s, x }: { s: Step; x: number }) {
  return (
    <>
      <Abs x={x} y={226} className="font-inter text-[13px] font-semibold" style={{ color: '#5d78a8' }}>{s.label}</Abs>
      <Abs x={x} y={254} w={26} h={26} className="rounded-full border-[3px] bg-white" style={{ borderColor: '#8a97ad' }} />
      <Abs x={x} y={298} w={330} className="font-inter text-[24px] font-semibold leading-[34px]">{s.title}</Abs>
      <Abs x={x} y={346} w={270} className="font-inter text-[14px] leading-[24px]" style={{ color: theme.muted }}>
        {s.text}
        {s.bullets?.map((b) => <div key={b} className="mb-1 flex gap-2"><span>•</span><span>{b}</span></div>)}
      </Abs>
      <Abs x={x} y={s.chipY} className="flex gap-2">
        {s.chips.map((c) => <div key={c} className="h-[14px] w-[14px] rounded-[3px]" style={{ background: c }} />)}
      </Abs>
    </>
  )
}
