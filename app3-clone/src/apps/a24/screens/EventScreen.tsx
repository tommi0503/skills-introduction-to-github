import { Check, Info, MoreHorizontal, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { Keyboard } from '../components/Keyboard'
import { Shell } from '../components/Shell'
import { WheelPicker } from '../components/WheelPicker'
import { eventScreen as d, keyboards } from '../data'
import { theme } from '../theme'

const SHADOW = 'shadow-[0_4px_14px_rgba(0,0,0,.06)]'

export function EventScreen() {
  return (
    <Shell background="#f6f6f6">
      <CircleButton x={41} y={88} className={SHADOW}>
        <X size={18} strokeWidth={1.8} color="#333" />
      </CircleButton>
      <span className="absolute inset-x-0 top-[78px] text-center text-[14px] font-semibold">{d.title}</span>
      <CircleButton x={291} y={88} className={SHADOW}>
        <MoreHorizontal size={18} strokeWidth={2.4} />
      </CircleButton>
      <CircleButton x={347} y={88} background={theme.violet}>
        <Check size={20} strokeWidth={1.8} color="#fff" />
      </CircleButton>

      <ImagePlaceholder label="Event cover photo" tone="#cfcac4" className="absolute left-[20px] top-[154px] h-[184px] w-[350px] rounded-[16px]" />
      <span className="absolute left-[18px] top-[369px] text-[22px] font-bold">{d.heading}</span>

      <div
        className="absolute left-[31px] top-[180px] h-[242px] w-[346px] rounded-[22px]"
        style={{ background: '#f3f3f3', boxShadow: '0 8px 30px rgba(0,0,0,.12)' }}
      >
        <WheelPicker
          className="absolute inset-x-0 top-[24px]"
          height={196}
          columns={d.picker.map((c) => ({ ...c, x: c.x - 31 }))}
          step={19.4}
          radius={93}
          fontSize={18.5}
          selectedFontSize={22}
          color="#111"
          dimColor="#8e8e8e"
          band={{ left: 24, right: 24, height: 35, color: '#dcdcdc' }}
        />
      </div>

      <div className="absolute left-[22px] right-[24px] top-[424px] h-[102px] rounded-[18px] bg-white" style={{ boxShadow: '0 6px 20px rgba(0,0,0,.06)' }}>
        <span className="absolute left-[18px] top-[24px] h-[54px] border-l border-dotted border-[#cfcfcf]" />
        {d.rows.map((r, i) => (
          <div key={r.label} className="absolute left-0 right-[14px] flex items-center text-[12px]" style={{ top: 18 + i * 52 }}>
            <span className="ml-[15px] size-[7px] rounded-full border border-[#bdbdbd] bg-white" />
            <span className="ml-[13px] flex items-center gap-[4px] text-[#7a7a7a]">
              {r.label}
              {r.info && <Info size={11} />}
            </span>
            <span className="ml-auto font-medium text-[#1a1a1a]">{r.value}</span>
          </div>
        ))}
        <span className="absolute left-[63px] right-[14px] top-[52px] h-px bg-[#ececec]" />
      </div>
      <Keyboard layout={keyboards.lower} background="#e9e9eb" className="top-[542px]" />
    </Shell>
  )
}
