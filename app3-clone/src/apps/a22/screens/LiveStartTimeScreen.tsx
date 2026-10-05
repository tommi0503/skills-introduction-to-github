import { ChevronRight, XCircle } from 'lucide-react'
import { Shell } from '../components/Shell'
import { WheelPicker } from '../components/WheelPicker'
import { live } from '../data'
import { theme } from '../theme'

export function LiveStartTimeScreen() {
  return (
    <Shell background={theme.scrim} statusColor="#000">
      <div style={{ color: theme.scrimText }}>
        <span className="absolute inset-x-0 top-[59px] text-center text-[16px] font-semibold">{live.title}</span>
        <span className="absolute right-[16px] top-[58px] text-[17px]">{live.cancel}</span>
        {live.rows.map((r, i) => (
          <div
            key={r}
            className="absolute inset-x-0 flex h-[50px] items-center justify-between border-b pl-[17px] pr-[18px] text-[15.5px]"
            style={{ top: 93 + i * 50, borderColor: '#454545' }}
          >
            {r}
            {i === 0 ? <XCircle size={17} fill="#3a3a3a" color={theme.scrim} /> : <ChevronRight size={18} strokeWidth={1.5} />}
          </div>
        ))}
        <p className="absolute left-[17px] top-[210px] text-[13px]" style={{ color: theme.scrimSub }}>{live.note}</p>
      </div>

      <div className="absolute inset-x-0 bottom-0 top-[387px] rounded-t-[14px] bg-white">
        <span className="absolute left-1/2 top-[12px] h-[4px] w-[36px] -translate-x-1/2 rounded-full bg-[#d4d4d4]" />
        <span className="absolute inset-x-0 top-[39px] text-center text-[16.5px] font-semibold">{live.sheetTitle}</span>
        <span className="absolute inset-x-0 top-[72px] h-px bg-[#ececec]" />
        <p className="absolute inset-x-0 top-[90px] text-center text-[12px] leading-[15px] text-[#555]">
          {live.sheetBody.map((l) => (
            <span key={l} className="block">{l}</span>
          ))}
        </p>
        <WheelPicker
          className="absolute inset-x-0 top-[140px]"
          height={186}
          columns={live.picker}
          step={22.5}
          radius={86}
          fontSize={18.5}
          selectedFontSize={21}
          color="#1a1a1a"
          dimColor="#8a8a8a"
          band={{ left: 39, right: 38, height: 34, color: theme.band, radius: 7 }}
        />
        <span className="absolute inset-x-0 top-[336px] h-px bg-[#f0f0f0]" />
        <div
          className="absolute left-[17px] right-[17px] top-[362px] flex h-[45px] items-center justify-center rounded-[8px] text-[15px] font-medium text-white"
          style={{ background: theme.doneBlue }}
        >
          {live.done}
        </div>
      </div>
    </Shell>
  )
}
