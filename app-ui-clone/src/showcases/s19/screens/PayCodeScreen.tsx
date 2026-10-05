import type { ReactNode } from 'react'
import { NaverStatusBar } from '../../shared-naver'
import { BottomNav } from '../components/BottomNav'
import { EventStrip } from '../components/EventStrip'
import { PayCodeCard } from '../components/PayCodeCard'
import { PayTabs } from '../components/PayTabs'
import { PointMoneyCard } from '../components/PointMoneyCard'
import { FrontCardImage } from '../components/ShinhanFrontCard'
import { DEFAULT_EDGES, StackedCardEdges, type CardEdge } from '../components/StackedCardEdges'
import { ACTIVE_PAY_TAB, eventsA, navItems, payTabs, type EventCardData } from '../data'
import { t19 } from '../theme'

export interface PayCodeScreenProps {
  time: string
  /** Which card is in front of the stack. */
  front: 'point' | 'card'
  events?: EventCardData[]
  withNav?: boolean
  /** Extra layers (dim + sheet). */
  overlay?: ReactNode
  statusColor?: string
  scrollIndicator?: boolean
}

const CARD_EDGES_BEHIND_CREDIT: CardEdge[] = [
  DEFAULT_EDGES[0],
  DEFAULT_EDGES[1],
  { ...DEFAULT_EDGES[2], surface: t19.pointGreen },
]

/** 현장결제 tab: payment code card with the selected payment means. */
export function PayCodeScreen({ time, front, events = eventsA, withNav = false, overlay, statusColor = '#fff', scrollIndicator = false }: PayCodeScreenProps) {
  return (
    <div className="absolute inset-0" style={{ background: t19.screen }}>
      <NaverStatusBar time={time} color={statusColor} charging className="!z-40" />
      <PayTabs tabs={payTabs} active={ACTIVE_PAY_TAB} className="absolute" style={{ left: 23.7, right: 24.8, top: 73.4 }} />
      <div className="absolute" style={{ left: 23.7, right: 24.8, top: 133 }}>
        <PayCodeCard>
          <div className="absolute inset-x-0" style={{ top: 253 }}>
            <StackedCardEdges edges={front === 'card' ? CARD_EDGES_BEHIND_CREDIT : DEFAULT_EDGES} />
          </div>
          {front === 'point' ? (
            <PointMoneyCard style={{ left: 19.6, right: 18.5, top: 266 }} />
          ) : (
            <FrontCardImage digits="5699" style={{ left: 19.6, right: 18.5, top: 266 }} />
          )}
        </PayCodeCard>
      </div>
      <EventStrip events={events} top={642} />
      {scrollIndicator && (
        <span className="absolute rounded-full" style={{ left: 383, top: 134, width: 2.6, height: 166, background: '#2a3038' }} />
      )}
      {withNav && <BottomNav items={navItems} />}
      {overlay}
    </div>
  )
}
