import { NaverStatusBar, WebToolbar } from '../../shared-naver'
import { IncomeForm } from '../components/IncomeForm'
import { t22 } from '../theme'

export function IncomeScreen() {
  return (
    <>
      <NaverStatusBar time="2:40" level={0.85} />
      <IncomeForm joinDate="2024년 1월 16일" dateConfirmed income="3,000" />
      <WebToolbar background={t22.toolbar} />
    </>
  )
}
