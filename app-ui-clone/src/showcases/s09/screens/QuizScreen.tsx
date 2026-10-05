import { X } from 'lucide-react'
import { Box } from '../../shared-canvas/Box'
import { KitchenStatusBar } from '../components/KitchenStatusBar'
import { quiz } from '../data'
import { theme } from '../theme'

/** "Help me choose" questionnaire header with progress. */
export function QuizScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.canvas }}>
      <div className="absolute inset-x-0 top-0 h-[180px] rounded-b-[22px]" style={{ background: theme.dark }}>
        <KitchenStatusBar />
        <Box rect={{ x: 23, y: 58, w: 330, h: 24 }} className="flex items-center justify-between text-white">
          <span className="font-poppins text-[17px] leading-[24px] font-semibold">{quiz.title}</span>
          <X size={22} strokeWidth={1.8} />
        </Box>
        <Box rect={{ x: 23, y: 100, w: 331, h: 15 }} className="overflow-hidden rounded-full" style={{ background: '#565656' }}>
          <div className="h-full rounded-full" style={{ width: `${quiz.progress * 100 * 0.98}%`, background: theme.lime }} />
        </Box>
      </div>
    </div>
  )
}
