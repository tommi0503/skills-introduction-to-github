import { CloseButton, NaverStatusBar, OptionGrid, PrimaryButton, WebToolbar } from '../../shared-naver'
import { CheckRow } from '../components/CheckRow'
import { FieldLabel } from '../components/FieldLabel'
import { FormTitle } from '../components/FormTitle'
import { UnderlineField } from '../components/UnderlineField'
import { healthInsurance, housing } from '../data'
import { t22 } from '../theme'

const grid = {
  height: 48.5,
  radius: 4,
  fontSize: 15.8,
  borderColor: '#e6e6e8',
  activeColor: t22.greenBorder,
  textColor: '#555557',
  weight: 400,
  activeWeight: 700,
} as const

export function ExtraInfoScreen() {
  return (
    <>
      <NaverStatusBar time="2:40" level={0.85} />
      <CloseButton centerY={85.2} right={11.5} size={30} />
      <FormTitle top={121} lines={['마지막으로', '추가 정보를 확인해주세요']} />
      <div className="absolute" style={{ left: 20, right: 20, top: 210.5 }}>
        <FieldLabel>의료보험 가입구분</FieldLabel>
      </div>
      <OptionGrid {...grid} options={healthInsurance.options} selected={healthInsurance.selected} className="absolute" style={{ left: 19.6, right: 20.6, top: 236.3 }} />
      <div className="absolute" style={{ left: 20, right: 20, top: 314.5 }}>
        <FieldLabel>주거 소유 형태</FieldLabel>
      </div>
      <OptionGrid {...grid} options={housing.options} selected={housing.selected} className="absolute" style={{ left: 19.6, right: 20.6, top: 341.5 }} />
      <div className="absolute" style={{ left: 20, right: 20, top: 421 }}>
        <FieldLabel>내 차 번호</FieldLabel>
        <UnderlineField placeholder="123가 4567" height={40} fontSize={17.5} offsetY={1.5} />
      </div>
      <p className="absolute" style={{ left: 20, top: 489.5, fontSize: 14.2, color: '#3d9b45', letterSpacing: -0.4 }}>
        *입력하면 금리 및 한도에 추가 혜택을 받을 수 있어요!
      </p>
      <div className="absolute" style={{ left: 19.6, top: 528.3 }}>
        <CheckRow label="입력한 정보 기억하기" />
      </div>
      <PrimaryButton
        background={t22.green}
        color="#040402"
        height={51.6}
        radius={8}
        fontSize={16.5}
        className="absolute"
        style={{ left: 19.6, right: 20.6, top: 686.1 }}
      >
        한도·금리 비교하기
      </PrimaryButton>
      <WebToolbar background={t22.toolbar} />
    </>
  )
}
