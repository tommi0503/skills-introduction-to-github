import { CircleCheck } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { cardTones, type CardTone } from '../theme'

export interface MatchStackProps {
  name: string
  note: string
  score: string
  pages: number
}

function ScoreChip({ score, className }: { score: string; className?: string }) {
  return (
    <span className={cn('flex h-[24px] items-center gap-[4px] rounded-full bg-white px-[8px] text-[11px] text-[#333]', className)}>
      <CircleCheck size={12} fill="#22a34a" color="#fff" strokeWidth={2.5} />
      {score}
    </span>
  )
}

function BackCard({ tone, height, className }: { tone: CardTone; height: number; className: string }) {
  return <div className={cn('absolute w-[150px] rounded-[22px]', className)} style={{ height, background: cardTones[tone] }} />
}

/** Fanned stack of matched dishes with a pager. */
export function MatchStack({ name, note, score, pages }: MatchStackProps) {
  return (
    <div className="relative h-[275px] w-[390px]">
      <BackCard tone="yellow" height={201} className="top-[17px] left-[69px]" />
      <BackCard tone="pink" height={181} className="top-[29px] left-[165px]" />
      <ScoreChip score={score} className="absolute top-[40px] left-[238px] w-[70px] justify-end" />
      <div
        className="absolute top-0 left-[109px] h-[227px] w-[169px] rounded-[22px] bg-[#c4d7f8]"
        style={{ boxShadow: '0 14px 26px rgba(30,40,80,0.13)' }}
      >
        <ScoreChip score={score} className="absolute top-[10px] right-[10px]" />
        <ImagePlaceholder className="absolute top-[52px] left-[44px] h-[104px] w-[111px] rounded-[10px]" label="burger" />
        <div className="absolute top-[176px] right-0 left-0 text-center">
          <div className="font-condensed text-[14.5px] leading-[18px] font-bold text-[#111]">{name}</div>
          <div className="mt-[2px] text-[13px] text-[#777]">{note}</div>
        </div>
      </div>
      <div className="absolute top-[258px] left-0 flex w-full justify-center gap-[8px]">
        {Array.from({ length: pages }, (_, i) => (
          <span key={i} className="h-[9.5px] w-[9.5px] rounded-full" style={{ background: i === 0 ? '#111' : '#dcdce0' }} />
        ))}
      </div>
    </div>
  )
}
