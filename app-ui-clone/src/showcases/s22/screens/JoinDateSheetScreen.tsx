import { BottomSheet, DimOverlay, NaverStatusBar, PrimaryButton, WebToolbar } from '../../shared-naver'
import { DateWheel } from '../components/DateWheel'
import { IncomeForm } from '../components/IncomeForm'
import { joinDateWheel } from '../data'
import { t22 } from '../theme'

/** Income form dimmed behind the "입사일" wheel picker sheet. */
export function JoinDateSheetScreen() {
  return (
    <>
      <NaverStatusBar time="2:39" level={0.85} />
      <IncomeForm joinDate="2025년 2월 13일" dateConfirmed={false} />
      <DimOverlay top={58.5} />
      <BottomSheet top={414.5} title="입사일">
        <div className="absolute inset-x-0" style={{ top: 60 }}>
          <DateWheel columns={joinDateWheel} />
        </div>
        <PrimaryButton
          background={t22.green}
          color="#040402"
          height={51.6}
          radius={8}
          fontSize={16.5}
          className="absolute"
          style={{ left: 13.4, right: 14.4, top: 271.6 }}
        >
          확인
        </PrimaryButton>
      </BottomSheet>
      <WebToolbar background={t22.toolbar} className="!z-30" />
    </>
  )
}
