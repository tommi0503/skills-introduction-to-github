import type { ReactNode } from 'react'
import { Clock } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { botCard, chatBubbles, productCards } from '../data'
import { theme } from '../theme'
import { CardLabels } from '../components/CardLabels'
import { ChatBubble } from '../components/ChatBubble'

function Card({ children, className, dark }: { children?: ReactNode; className?: string; dark?: boolean }) {
  return (
    <div
      className={cn('relative h-[280px] overflow-hidden rounded-[16px]', className)}
      style={{ background: dark ? theme.darkCard : theme.card }}
    >
      {children}
    </div>
  )
}

function ChatCard() {
  return (
    <Card>
      {chatBubbles.map((b) => (
        <ChatBubble
          key={b.text}
          from={b.from}
          className="absolute"
          style={{ top: b.top, width: b.width, ...(b.from === 'user' ? { right: 20 } : { left: 20, paddingRight: b.padRight }) }}
        >
          {b.text}
        </ChatBubble>
      ))}
      <CardLabels title={productCards.chat} action={productCards.explore} />
    </Card>
  )
}

function BuildCard() {
  return (
    <Card dark>
      <ImagePlaceholder label="terminal session" tone="#1d1d1d" className="absolute inset-[12px] bottom-[52px] rounded-[8px]" />
      <CardLabels title={productCards.build} action={productCards.explore} tone="light" />
    </Card>
  )
}

function BotCard() {
  return (
    <Card>
      <div
        className="absolute rounded-[16px] px-[12px] py-[6px] text-[14px] leading-5 tracking-[-0.15px] text-white"
        style={{ left: 72, top: -28, width: 315, height: 56, background: 'rgb(17,17,16)' }}
      >
        <span className="absolute bottom-[8px] left-[12px]">me?</span>
      </div>
      <div
        className="absolute whitespace-pre-line rounded-[16px] px-[12px] py-[10px] text-[14px] leading-5 tracking-[-0.15px]"
        style={{ left: 16, top: 43, width: 341, paddingRight: 20, background: '#efeeeb', color: theme.ink }}
      >
        {botCard.reply}
      </div>
      <div className="absolute flex items-center gap-[6px] text-[13px] leading-4" style={{ left: 83, top: 140 }}>
        <span className="text-black/55">{botCard.routineLabel}</span>
        <Clock size={15} strokeWidth={1.5} className="text-black/55" />
        <span style={{ color: theme.ink }}>{botCard.routineName}</span>
      </div>
      <div className="absolute flex items-center" style={{ left: 18, top: 192 }}>
        {[0.45, 0.65, 1].map((o) => (
          <span key={o} className="mr-[4px] size-[10px] rounded-full" style={{ background: '#f97316', opacity: o }} />
        ))}
        <span className="ml-[12px] text-[13px] text-black/35">{botCard.thinking}</span>
      </div>
      <CardLabels title={productCards.bot} action={productCards.explore} />
    </Card>
  )
}

function ImagineCard() {
  return (
    <Card className="p-[4px]">
      <div className="flex h-full gap-[3px]">
        <ImagePlaceholder label="merchandise photo" className="h-[272px] w-[400px] rounded-l-[12px]" />
        <div className="flex flex-col gap-[3px]">
          <ImagePlaceholder label="athlete photo" className="h-[135px] w-[199px] rounded-tr-[12px]" />
          <ImagePlaceholder label="product photo" className="h-[134px] w-[199px] rounded-br-[12px]" />
        </div>
      </div>
      <CardLabels title={productCards.imagine} action={productCards.explore} tone="light" className="right-[18px] bottom-[20px] left-[20px]" />
    </Card>
  )
}

function VoiceCard() {
  return (
    <Card>
      <ImagePlaceholder label="voice orb" className="absolute rounded-full" style={{ left: 196, top: 31, width: 218, height: 218 }} />
      <CardLabels title={productCards.voice} action={productCards.explore} />
    </Card>
  )
}

export function ProductGrid() {
  return (
    <section className="mx-auto mt-[80px] flex flex-col gap-[12px]" style={{ width: theme.content }}>
      <div className="grid grid-cols-3 gap-[13px]">
        <ChatCard />
        <BuildCard />
        <BotCard />
      </div>
      <div className="grid grid-cols-[608px_610px] gap-[14px]">
        <ImagineCard />
        <VoiceCard />
      </div>
    </section>
  )
}
