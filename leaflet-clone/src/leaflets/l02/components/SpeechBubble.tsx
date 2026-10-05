import { Placed, cn } from '../../../ui'
import type { Bubble } from '../data'
import { Lines } from './Lines'

interface SpeechBubbleProps {
  bubble: Bubble
  fill: string
  textClassName?: string
}

/** Rounded speech balloon with a triangular tail, positioned in panel coordinates. */
export function SpeechBubble({ bubble, fill, textClassName }: SpeechBubbleProps) {
  const { box, radius, tail, lines, align, textX, textY } = bubble
  return (
    <Placed x={box.x} y={box.y} width={box.w} height={box.h}>
      <svg className="absolute inset-0 overflow-visible" width={box.w} height={box.h} aria-hidden>
        <polygon points={tail.map((p) => p.join(',')).join(' ')} fill={fill} />
      </svg>
      <div className="absolute inset-0" style={{ background: fill, borderRadius: radius }} />
      <Lines
        lines={lines}
        className={cn('absolute', align === 'center' ? 'inset-x-0 text-center' : '', textClassName)}
        style={{ top: textY, left: align === 'center' ? 0 : textX }}
      />
    </Placed>
  )
}
