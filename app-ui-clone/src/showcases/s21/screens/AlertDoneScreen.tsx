import { ImagePlaceholder } from '../../../ui'
import { BackTitleHeader, NaverStatusBar, PrimaryButton, WebToolbar } from '../../shared-naver'
import { BulletNotes } from '../components/BulletNotes'
import { doneNotes, doneTitle } from '../data'

/** Confirmation after enabling the alert (bell illustration → placeholder). */
export function AlertDoneScreen() {
  return (
    <>
      <NaverStatusBar time="1:53" glyph="silent" level={0.55} />
      <BackTitleHeader title="카드 실적 알림" titleSize={17.5} arrowSize={30} arrowLeft={23.7} />
      <h1
        className="absolute whitespace-pre-line"
        style={{ left: 20, top: 132, fontSize: 23.7, lineHeight: '30px', fontWeight: 700, color: '#151419', letterSpacing: -0.5 }}
      >
        {doneTitle.join('\n')}
      </h1>
      <ImagePlaceholder
        label="bell and card illustration"
        className="absolute"
        style={{ left: 126, top: 263, width: 148.5, height: 156, borderRadius: 16 }}
      />
      <div className="absolute" style={{ left: 19.6, right: 19.6, top: 481.5 }}>
        <BulletNotes items={doneNotes} />
      </div>
      <PrimaryButton
        background="#46a853"
        height={51}
        radius={6}
        className="absolute"
        style={{ left: 19.6, right: 20.6, top: 690 }}
      >
        확인
      </PrimaryButton>
      <WebToolbar background="#fafafa" />
    </>
  )
}
