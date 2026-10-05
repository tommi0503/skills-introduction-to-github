import { Search } from 'lucide-react'
import { CloseButton, NaverStatusBar, WebToolbar } from '../../shared-naver'
import { ClearButton } from '../components/ClearButton'
import { CompanyResultItem } from '../components/CompanyResultItem'
import { FormTitle } from '../components/FormTitle'
import { UnderlineField } from '../components/UnderlineField'
import { companyQuery, companyResults } from '../data'
import { t22 } from '../theme'

export function CompanySearchScreen() {
  return (
    <>
      <NaverStatusBar time="2:39" level={0.85} />
      <CloseButton centerY={85.2} right={11.5} size={30} />
      <FormTitle top={121} lines={['직장명을 입력해 주세요']} />
      <div className="absolute" style={{ left: 20, right: 20, top: 181 }}>
        <UnderlineField
          value={companyQuery}
          height={39.5}
          fontSize={18.5}
          lineWidth={1.2}
          trailing={
            <span className="flex items-center" style={{ gap: 4 }}>
              <ClearButton size={21} />
              <Search size={24} strokeWidth={2} color="#26252a" style={{ marginRight: -2 }} />
            </span>
          }
        />
      </div>
      <div className="absolute flex items-center justify-between" style={{ left: 20, right: 21, top: 242.5, height: 30 }}>
        <span style={{ fontSize: 15, color: '#757575', letterSpacing: -0.4 }}>검색 결과가 없다면 직접 입력해주세요.</span>
        <span
          className="flex items-center justify-center"
          style={{ width: 70.5, height: 30, borderRadius: 4, background: '#f4f5f7', fontSize: 14, color: '#5a5a5c', letterSpacing: -0.4 }}
        >
          직접 입력
        </span>
      </div>
      <div className="absolute inset-x-0" style={{ top: 297.5 }}>
        {companyResults.map((c) => (
          <CompanyResultItem key={c.bizNo} item={c} />
        ))}
      </div>
      <WebToolbar background={t22.toolbar} />
    </>
  )
}
