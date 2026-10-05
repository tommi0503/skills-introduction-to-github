import { BackTitleHeader, LabeledToggle, NaverStatusBar, PrimaryButton, WebToolbar } from '../../shared-naver'
import { InfoBox } from '../components/InfoBox'
import { quickPayInfo } from '../data'

export function QuickPayScreen() {
  return (
    <>
      <NaverStatusBar time="1:31" charging />
      <BackTitleHeader title="바로결제" centerY={86} arrowSize={26} arrowLeft={18.5} />
      <div className="absolute flex items-center justify-between" style={{ left: 20.5, right: 20.5, top: 153.7, height: 31 }}>
        <span style={{ fontSize: 16.5, fontWeight: 600, color: '#19191b', letterSpacing: -0.3 }}>현장결제</span>
        <LabeledToggle on />
      </div>
      <PrimaryButton
        variant="soft"
        background="#e8f4ec"
        color="#3d9a50"
        height={48.5}
        radius={6}
        fontSize={16}
        className="absolute"
        style={{ left: 20, right: 20, top: 212.5 }}
      >
        현장결제 도움말
      </PrimaryButton>
      <div className="absolute" style={{ left: 20, right: 20, top: 291 }}>
        <InfoBox paragraphs={quickPayInfo} />
      </div>
      <WebToolbar />
    </>
  )
}
