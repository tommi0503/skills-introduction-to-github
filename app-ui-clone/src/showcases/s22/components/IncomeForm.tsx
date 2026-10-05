import { ChevronDown } from 'lucide-react'
import { CloseButton, PrimaryButton } from '../../shared-naver'
import { t22 } from '../theme'
import { ClearButton } from './ClearButton'
import { FieldLabel } from './FieldLabel'
import { FormTitle } from './FormTitle'
import { UnderlineField } from './UnderlineField'

export interface IncomeFormProps {
  joinDate: string
  /** False renders the date in placeholder grey (not yet confirmed). */
  dateConfirmed: boolean
  income?: string
}

/** "입사일과 소득을 알려주세요" — join date + yearly income. */
export function IncomeForm({ joinDate, dateConfirmed, income }: IncomeFormProps) {
  return (
    <>
      <CloseButton centerY={85.2} right={11.5} size={30} />
      <FormTitle top={120.5} lines={['입사일과 소득을 알려주세요']} />
      <div className="absolute" style={{ left: 20, right: 20, top: 174.5 }}>
        <FieldLabel>입사일</FieldLabel>
        <UnderlineField
          value={dateConfirmed ? joinDate : undefined}
          placeholder={joinDate}
          height={45.5}
          offsetY={3}
          trailing={<ChevronDown size={29} strokeWidth={1.2} color="#a8a8a8" style={{ marginRight: -5, marginTop: -16 }} />}
        />
      </div>
      <div className="absolute" style={{ left: 20, right: 20, top: 268.5 }}>
        <FieldLabel>내 소득</FieldLabel>
        <UnderlineField
          value={income}
          placeholder="연소득(세전)"
          height={44.5}
          offsetY={3}
          trailing={
            <span className="flex items-center" style={{ gap: 8 }}>
              {income && <ClearButton size={23.5} />}
              <span style={{ fontSize: 17.5, color: '#232323', letterSpacing: -0.4 }}>만원</span>
            </span>
          }
        />
      </div>
      <PrimaryButton
        background={income ? t22.green : '#dcdcdf'}
        color={income ? '#040402' : '#a0a0a2'}
        height={52.7}
        radius={8}
        fontSize={16.5}
        className="absolute"
        style={{ left: 19.6, right: 20.6, top: 384.8, fontWeight: 600 }}
      >
        다음
      </PrimaryButton>
    </>
  )
}
