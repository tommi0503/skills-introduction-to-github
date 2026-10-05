import { ImagePlaceholder } from '../../../ui'
import type { WalletCard } from '../data'

function CardBadge({ text }: { text: string }) {
  return (
    <span
      className="absolute flex items-center justify-center rounded-full"
      style={{ right: 19.6, height: 19.5, padding: '0 8px', background: 'rgba(25,25,27,0.88)', color: '#fff', fontSize: 12.5, fontWeight: 600, letterSpacing: -0.3 }}
    >
      {text}
    </span>
  )
}

/** Overlapping payment-card images (placeholders) each with a last-digits badge. */
export function WalletCardStack({ cards }: { cards: WalletCard[] }) {
  return (
    <>
      {cards.map((c) => (
        <div key={c.badge} className="absolute" style={{ left: 23.7, right: 24.8, top: c.top, height: 260 }}>
          <ImagePlaceholder label="payment card" tone={c.tone} className="h-full w-full" style={{ borderRadius: 13 }} />
          <div className="absolute inset-x-0" style={{ top: c.badgeTop }}>
            <CardBadge text={c.badge} />
          </div>
        </div>
      ))}
    </>
  )
}
