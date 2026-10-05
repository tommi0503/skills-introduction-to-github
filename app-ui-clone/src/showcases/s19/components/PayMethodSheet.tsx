import { Check } from 'lucide-react'
import { HomeIndicator, ImagePlaceholder } from '../../../ui'
import { BottomSheet } from '../../shared-naver'
import type { PayMethod } from '../data'

const ROW = 71.3

function MethodRow({ m, divider }: { m: PayMethod; divider: boolean }) {
  return (
    <div className="relative flex items-center" style={{ height: ROW, margin: '0 19.6px', borderBottom: divider ? '1px solid #ececec' : undefined }}>
      <ImagePlaceholder
        label={`${m.name} logo`}
        tone={m.tone}
        className="rounded-full"
        style={{ width: 41.3, height: 41.3, border: m.outlined ? '1px solid #e3e3e3' : undefined }}
      />
      <span className="flex items-center" style={{ marginLeft: 10.5, fontSize: 15, letterSpacing: -0.4 }}>
        <span style={{ color: m.selected ? '#3aa94e' : '#1d1d1d', fontWeight: m.selected ? 700 : 500 }}>{m.name}</span>
        <span style={{ margin: '0 3px', color: '#c8c8c8', fontSize: 13 }}>|</span>
        <span style={{ color: '#999', fontSize: 14 }}>{m.region}</span>
        {m.event && (
          <span
            className="flex items-center rounded-full font-inter"
            style={{ marginLeft: 6, height: 20.5, padding: '0 8px', background: '#e3eefc', color: '#3d7be0', fontSize: 11, fontWeight: 700 }}
          >
            EVENT
          </span>
        )}
      </span>
      {m.selected && <Check size={20} strokeWidth={2} color="#43a956" className="absolute" style={{ right: 9 }} />}
    </div>
  )
}

/** "결제 방법 선택" sheet listing the payment schemes. */
export function PayMethodSheet({ methods, top }: { methods: PayMethod[]; top: number }) {
  return (
    <BottomSheet top={top} title="결제 방법 선택" titleTop={23} titleSize={20} closeSize={30} closeTop={9} closeRight={8.6} radius={22}>
      <div className="absolute inset-x-0" style={{ top: 47.5 }}>
        {methods.map((m, i) => (
          <MethodRow key={m.name} m={m} divider={i < methods.length - 1} />
        ))}
      </div>
      <HomeIndicator width={138} bottom={6.5} className="!h-[4.5px]" />
    </BottomSheet>
  )
}
