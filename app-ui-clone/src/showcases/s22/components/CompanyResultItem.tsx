import { ChevronRight } from 'lucide-react'
import type { CompanyResult } from '../data'
import { t22 } from '../theme'

/** Workplace search hit: name, business number and address. */
export function CompanyResultItem({ item }: { item: CompanyResult }) {
  const meta = { fontSize: 13.6, lineHeight: '19.6px', letterSpacing: -0.35 } as const
  return (
    <div className="relative" style={{ height: 77.4, padding: '0 20px' }}>
      <div style={{ fontSize: 14.2, lineHeight: '20px', fontWeight: 600, color: '#242426', letterSpacing: -0.4 }}>{item.name}</div>
      <div style={{ ...meta, color: '#7b7b7b', marginTop: 1 }}>
        사업자 번호 <span style={{ color: t22.link, marginLeft: 2, letterSpacing: -0.1, fontWeight: 500 }}>{item.bizNo}</span>
      </div>
      <div style={{ ...meta, color: '#858585' }}>
        주소
        <span className="inline-block align-middle" style={{ width: 1, height: 10, background: '#d6d6d6', margin: '0 5px 2px 6px' }} />
        {item.address}
      </div>
      <ChevronRight size={14} strokeWidth={2.3} className="absolute" style={{ right: 16.4, top: 2, color: '#3e3e40' }} />
    </div>
  )
}
