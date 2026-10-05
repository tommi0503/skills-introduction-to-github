import { ImagePlaceholder } from '../../../ui'

export interface CardEdge {
  inset: number
  top: number
  height: number
  tone: string
  /** Plain UI surface colour (e.g. the green point card) instead of a card image. */
  surface?: string
}

export const DEFAULT_EDGES: CardEdge[] = [
  { inset: 56.5, top: 0, height: 9, tone: '#e5e7eb' },
  { inset: 42.5, top: 5, height: 8, tone: '#dfe1e5' },
  { inset: 33, top: 8.5, height: 9, tone: '#c9cacd' },
]

/** Peeking top edges of the cards stacked behind the front card (card art → placeholders). */
export function StackedCardEdges({ edges = DEFAULT_EDGES }: { edges?: CardEdge[] }) {
  return (
    <>
      {edges.map((e, i) => {
        const style = { left: e.inset, right: e.inset, top: e.top, height: e.height + 10, borderRadius: '10px 10px 0 0' }
        return e.surface ? (
          <div key={i} className="absolute" style={{ ...style, background: e.surface }} />
        ) : (
          <ImagePlaceholder key={i} label="stacked card" tone={e.tone} className="absolute" style={style} />
        )
      })}
    </>
  )
}
