import { BackTitleHeader, NaverStatusBar, OptionGrid, PrimaryButton, WebToolbar } from '../../shared-naver'
import { AmountField } from '../components/AmountField'
import { CardSummaryHeader } from '../components/CardSummaryHeader'
import { alertQuestion, amountOptions, amountPlaceholder, cardInfo } from '../data'

export interface AlertSetupScreenProps {
  /** Index of the chosen preset; undefined = nothing entered yet. */
  selected?: number
}

/** "카드 실적 알림" amount picker — empty and filled states share this screen. */
export function AlertSetupScreen({ selected }: AlertSetupScreenProps) {
  const value = selected === undefined ? undefined : amountOptions[selected]
  return (
    <>
      <NaverStatusBar time="1:53" glyph="silent" level={0.55} />
      <BackTitleHeader title="카드 실적 알림" titleSize={17.5} arrowSize={30} arrowLeft={23.7} />
      <div className="absolute inset-x-0" style={{ top: 133 }}>
        <CardSummaryHeader issuer={cardInfo.issuer} name={cardInfo.name} />
      </div>
      <div className="absolute inset-x-0" style={{ top: 217, height: 10, background: '#eff0f2' }} />
      <div className="absolute inset-x-0" style={{ top: 255 }}>
        <AmountField label={alertQuestion} placeholder={amountPlaceholder} value={value} />
      </div>
      <OptionGrid
        options={amountOptions}
        selected={selected}
        className="absolute"
        height={44}
        fontSize={15.5}
        borderColor="#e4e4e6"
        activeColor="#3caa54"
        textColor="#1d1d1f"
        weight={500}
        activeWeight={500}
        radius={4}
        style={{ left: 19.6, right: 20.6, top: 340.5 }}
      />
      <PrimaryButton
        variant={value ? 'primary' : 'disabled'}
        background={value ? '#44a84c' : '#dcdde0'}
        color={value ? '#fff' : '#a3a4a6'}
        height={52}
        radius={6}
        className="absolute"
        style={{ left: 19.6, right: 20.6, top: 678 }}
      >
        알림 설정하기
      </PrimaryButton>
      <WebToolbar background="#fafafa" />
    </>
  )
}
