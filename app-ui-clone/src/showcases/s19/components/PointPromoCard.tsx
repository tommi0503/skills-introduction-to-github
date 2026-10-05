import { pointMoney } from '../data'
import { t19 } from '../theme'

/** Vivid green 포인트•머니 header card with the "포인트 뽑기" tooltip. */
export function PointPromoCard({ style }: { style?: React.CSSProperties }) {
  return (
    <div className="absolute" style={{ height: 200, borderRadius: 13, background: t19.pointGreenVivid, ...style }}>
      <div className="absolute flex items-center justify-between" style={{ left: 19.6, right: 19.6, top: 20, height: 24 }}>
        <span style={{ fontSize: 16.5, fontWeight: 700, color: '#0b0b0b', letterSpacing: -0.3 }}>{pointMoney.title}</span>
        <span style={{ fontSize: 18, fontWeight: 700, color: '#0b0b0b', letterSpacing: -0.2 }}>{pointMoney.balance}</span>
      </div>
      <div
        className="absolute flex items-center"
        style={{ left: 19.6, top: 52.5, height: 27, padding: '0 8px 0 6.5px', borderRadius: 4, background: '#0c0c0c' }}
      >
        <span
          className="absolute"
          style={{ left: 38, top: -4, width: 0, height: 0, borderLeft: '4px solid transparent', borderRight: '4px solid transparent', borderBottom: '4.5px solid #0c0c0c' }}
        />
        <span
          className="flex items-center justify-center rounded-full font-bold"
          style={{ width: 15.5, height: 15.5, background: '#2bc56a', color: '#0c0c0c', fontSize: 9 }}
        >
          N
        </span>
        <span style={{ marginLeft: 5, fontSize: 13, color: '#fff', fontWeight: 600, letterSpacing: -0.4 }}>
          {pointMoney.promo.text}
          <span style={{ color: t19.pointGreenVivid }}>{pointMoney.promo.highlight}</span>
        </span>
      </div>
    </div>
  )
}
