import { DimOverlay } from '../../shared-naver'
import { PayMethodSheet } from '../components/PayMethodSheet'
import { payMethods } from '../data'
import { PayCodeScreen } from './PayCodeScreen'

/** Payment code screen dimmed behind the "결제 방법 선택" sheet. */
export function MethodSheetScreen() {
  return (
    <PayCodeScreen
      time="1:36"
      front="point"
      overlay={
        <>
          <DimOverlay opacity={0.6} zIndex={35} />
          <div className="absolute inset-0 z-[36]">
            <PayMethodSheet methods={payMethods} top={462.7} />
          </div>
        </>
      }
    />
  )
}
