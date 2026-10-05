import { ChevronRight } from 'lucide-react'
import type { CompanyResult } from '../data'
import { t22 } from '../theme'

/** Workplace search hit: name, business number and address. */
export function CompanyResultItem({ item }: { item: CompanyResult }) {
  const meta = { fontSize: 14, lineHeight: '19.6px', letterSpacing: -0.3 } as const
  return (
    <div className="relative" style={{ height: 77.4, padding: '0 20px' }}>
      <div style={{ fontSize: 15, lineHeight: '20px', fontWeight: 500, color: '#242426', letterSpacing: -0.4 }}>{item.name}</div>
      <div style={{ ...meta, color: '#7b7b7b', marginTop: 1 }}>
        사업자 번호 <span style={{ color: t22.link, marginLeft: 3, letterSpacing: -0.1 }}>{item.bizNo}</span>
      </div>
      <div style={{ ...meta, color: '#858585' }}>
        주소 <span style={{ color: '#d0d0d0', margin: '0 3px' }}>|</span> {item.address}
      </div>
      <ChevronRight size={17} strokeWidth={2} className="absolute" style={{ right: 17.5, top: 1.5, color: '#3e3e40' }} />
    </div>
  )
}
