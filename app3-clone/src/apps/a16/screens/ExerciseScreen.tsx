import { AppScreen, HomeIndicator, ImagePlaceholder, StatusBar, cn } from '../../../ui'
import { checkLabel, type Exercise } from '../data'
import { CheckButton } from '../components/CheckButton'
import { ExerciseBadge } from '../components/ExerciseBadge'
import { LessonHeader } from '../components/LessonHeader'
import { SpeechBubble } from '../components/SpeechBubble'
import { WordChip } from '../components/WordChip'
import { FONT, palette as c } from '../theme'

const ANSWER_LINE_GAP = 54

export function ExerciseScreen({ exercise: e }: { exercise: Exercise }) {
  return (
    <AppScreen className={cn(FONT)}>
      <StatusBar paddingX={34} paddingTop={18} fontSize={16} />
      <div className="absolute inset-x-0 top-[80px]">
        <LessonHeader progress={e.progress} color={e.progressColor} />
      </div>
      <div className="absolute left-[20px]" style={{ top: e.layout.badgeY }}>
        <ExerciseBadge badge={e.badge} />
      </div>
      <h1 className="absolute left-[17px] text-[21px] font-bold" style={{ top: e.layout.titleY, color: c.text }}>
        {e.title}
      </h1>
      <ImagePlaceholder
        className="absolute rounded-[20px]"
        style={{ left: e.character.x, top: e.character.y, width: e.character.w, height: e.character.h }}
        label="character"
      />
      <div className="absolute left-[150px]" style={{ top: e.bubble.y }}>
        <SpeechBubble words={e.bubble.words} speaker={e.bubble.speaker} />
      </div>
      <div className="absolute flex gap-[8px] pl-[16px]" style={{ top: e.answerTop - 46 }}>
        {e.answer.map((t) => (
          <WordChip key={t.word} token={t} />
        ))}
      </div>
      {[0, 1].map((i) => (
        <div
          key={i}
          className="absolute right-[18px] left-[16px] h-[2px]"
          style={{ top: e.answerTop + i * ANSWER_LINE_GAP, background: c.line }}
        />
      ))}
      <div className="absolute inset-x-0 flex flex-col items-center gap-[10px]" style={{ top: e.bankTop }}>
        {e.bank.map((row, r) => (
          <div key={r} className="flex gap-[8px]">
            {row.map((t) => (
              <WordChip key={t.word} token={t} />
            ))}
          </div>
        ))}
      </div>
      <CheckButton label={checkLabel} className="absolute top-[747px] right-[18px] left-[16px]" />
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
