import { ChevronRight } from 'lucide-react'
import { pointMoney } from '../data'
import { t19 } from '../theme'

function Caret({ color = '#2c6b26' }: { color?: string }) {
  return (
    <span
      style={{
        marginLeft: 8,
        width: 0,
        height: 0,
        borderLeft: '4px solid transparent',
        borderRight: '4px solid transparent',
        borderTop: '5px solid ' + color,
      }}
    />
  )
}

/** Green 포인트•머니 card with balance and withdrawal account rows. */
export function PointMoneyCard({ style }: { style?: React.CSSProperties }) {
  return (
    <div className="absolute overflow-hidden" style={{ background: t19.pointGreen, borderRadius: 13, height: 192, ...style }}>
      <div className="absolute" style={{ left: 19.5, top: 21.5, fontSize: 16.5, fontWeight: 700, color: '#0b0b0b', letterSpacing: -0.3 }}>
        {pointMoney.title}
      </div>
      <div className="absolute flex items-center justify-between" style={{ left: 20.5, right: 19.5, top: 95, height: 24 }}>
        <span style={{ fontSize: 15.5, fontWeight: 600, color: '#0b0b0b', letterSpacing: -0.3 }}>{pointMoney.balanceLabel}</span>
        <span className="flex items-center" style={{ fontSize: 21.5, fontWeight: 700, color: '#0b0b0b', letterSpacing: -0.2 }}>
          {pointMoney.balance}
          <ChevronRight size={16} strokeWidth={2.4} style={{ marginLeft: 1, marginRight: -4 }} />
        </span>
      </div>
      <div className="absolute inset-x-0" style={{ top: 136.5, height: 1, background: t19.pointLine }} />
      <div className="absolute flex items-center justify-between" style={{ left: 20.5, right: 20.5, top: 152, height: 22 }}>
        <span style={{ fontSize: 15, color: '#1f4a1b', letterSpacing: -0.3 }}>{pointMoney.accountLabel}</span>
        <span className="flex items-center" style={{ fontSize: 15, fontWeight: 600, color: '#0b0b0b', letterSpacing: -0.3 }}>
          {pointMoney.account}
          <Caret />
        </span>
      </div>
    </div>
  )
}
