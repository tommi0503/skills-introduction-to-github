import { Placed, cn } from '../../../ui'

export interface FooterText {
  text: string
  x: number
}

interface ContactFooterProps {
  items: FooterText[]
  /** Vertical centre line of the footer (panel px). */
  y: number
  className?: string
}

/** Phone / e-mail / url line printed on the green ground band. */
export function ContactFooter({ items, y, className }: ContactFooterProps) {
  return (
    <>
      {items.map((i) => (
        <Placed key={i.text} x={i.x} y={y} className={cn('-translate-y-1/2 whitespace-nowrap leading-none', className)}>
          {i.text}
        </Placed>
      ))}
    </>
  )
}
