import type { Macro } from '../data'
import { theme } from '../theme'
import { Ring } from './Ring'

export function MacroCard({ m }: { m: Macro }) {
  const Icon = m.icon
  return (
    <div className="h-[149px] flex-1 rounded-[14px] bg-white px-[10px] pt-[14px]" style={{ boxShadow: '0 2px 10px rgba(0,0,0,.05)' }}>
      <div className="text-[17.5px] font-semibold leading-none">{m.amount}</div>
      <div className="mt-[9px] text-[11px] leading-none text-[#333]">
        {m.name} <b className="font-semibold">left</b>
      </div>
      <div className="mt-[16px] flex justify-center">
        <Ring size={66} stroke={5} progress={m.progress} color={m.color} track={theme.ringTrack}>
          <Icon size={13} color={m.color} fill={m.color} />
        </Ring>
      </div>
    </div>
  )
}
