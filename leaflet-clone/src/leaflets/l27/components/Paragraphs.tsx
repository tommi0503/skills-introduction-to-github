import { TextCard } from '../../shared-2627/components/TextCard'
import type { Paragraph } from '../data'

/** Renders positioned paragraph cards. */
export function Paragraphs({ items }: { items: Paragraph[] }) {
  return (
    <>
      {items.map((p) => (
        <TextCard key={p.y} lines={p.lines} card={p.card ?? true} className="flex flex-col justify-center" style={{ left: p.x, top: p.y, width: p.w, height: p.h }} />
      ))}
    </>
  )
}
