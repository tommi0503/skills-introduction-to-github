import { ChevronLeft, CirclePlus } from 'lucide-react'
import { BackTitleHeader, NaverStatusBar } from '../../shared-naver'
import { BillingSection } from '../components/BillingSection'
import { pastBilling, upcomingBilling } from '../data'

const tabs = ['월 사용금액', '결제금액']
const ACTIVE_TAB = 1

/** "카드" asset page — 결제금액 tab with upcoming and past statements. */
export function CardPaymentsScreen() {
  return (
    <>
      <NaverStatusBar time="1:52" glyph="location" level={0.55} />
      <BackTitleHeader
        title="카드"
        titleSize={17}
        left={
          <span className="flex items-center" style={{ fontSize: 15.5, color: '#1d1d1d', marginLeft: -15, letterSpacing: -0.3 }}>
            <ChevronLeft size={26} strokeWidth={1.4} style={{ marginRight: 1 }} />내 자산
          </span>
        }
        right={
          <span className="flex items-center" style={{ fontSize: 16, color: '#3aa856', marginRight: 4, letterSpacing: -0.3 }}>
            <CirclePlus size={19} strokeWidth={1.6} style={{ marginRight: 4 }} />카드 연결
          </span>
        }
      />
      <div className="absolute inset-x-0 flex" style={{ top: 118, height: 36, borderBottom: '1px solid #f1f1f1' }}>
        {tabs.map((t, i) => (
          <div
            key={t}
            className="relative flex flex-1 items-center justify-center"
            style={{
              fontSize: 15,
              letterSpacing: -0.3,
              color: i === ACTIVE_TAB ? '#111' : '#9a9a9c',
              fontWeight: i === ACTIVE_TAB ? 600 : 400,
            }}
          >
            {t}
            {i === ACTIVE_TAB && <span className="absolute inset-x-0" style={{ bottom: -1, height: 3, background: '#2b2b2f' }} />}
          </div>
        ))}
      </div>
      <div className="absolute" style={{ left: 20.5, top: 178.5 }}>
        <div style={{ fontSize: 16, fontWeight: 600, color: '#1d1d1f', letterSpacing: -0.4 }}>결제예정 금액</div>
        <div style={{ fontSize: 27.7, fontWeight: 700, color: '#151419', letterSpacing: -0.6, marginTop: -2 }}>778,913원</div>
      </div>
      <div className="absolute inset-x-0" style={{ top: 258.5 }}>
        {upcomingBilling.map((m, i) => (
          <div key={m.month} style={{ marginTop: i ? 11 : 0 }}>
            <BillingSection month={m} />
          </div>
        ))}
        <div style={{ margin: '6.5px 21px 0 20.5px', borderTop: '1px solid #ececee' }} />
        <p style={{ margin: '24px 20.5px 0', fontSize: 14, color: '#86868a', letterSpacing: -0.4 }}>
          결제일이 주말/공휴일인 경우 다음 영업일에 출금됩니다.
        </p>
        <div style={{ marginTop: 24, height: 9, background: '#eff0f4' }} />
        <p style={{ margin: '22px 20.5px 0', fontSize: 16.5, color: '#1b1b1d', letterSpacing: -0.4 }}>
          이전 청구서 <span style={{ fontSize: 13, color: '#55555a' }}>(2025.2.16 기준)</span>
        </p>
        <div style={{ marginTop: 16 }}>
          {pastBilling.map((m) => (
            <BillingSection key={m.month} month={m} />
          ))}
        </div>
      </div>
      <span className="absolute rounded-full" style={{ left: 383.8, top: 730, width: 2.6, height: 106, background: '#888' }} />
    </>
  )
}
