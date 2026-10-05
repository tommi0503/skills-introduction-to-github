import type { InfoParagraph } from '../data'

const TONES: Record<InfoParagraph['tone'], React.CSSProperties> = {
  strong: { color: '#17181c', fontWeight: 700, fontSize: 15, lineHeight: '21px' },
  accent: { color: '#3aa35a', fontWeight: 600, fontSize: 14, lineHeight: '19.6px' },
  body: { color: '#45464b', fontWeight: 400, fontSize: 14, lineHeight: '19.6px' },
}

/** Grey notice panel made of styled paragraphs. */
export function InfoBox({ paragraphs }: { paragraphs: InfoParagraph[] }) {
  return (
    <div style={{ background: '#f6f7f9', padding: '20px 18px 22px 19px' }}>
      {paragraphs.map((p, i) => (
        <p key={i} className="whitespace-pre-line" style={{ ...TONES[p.tone], marginTop: p.gap ?? 0, letterSpacing: -0.35 }}>
          {p.text}
        </p>
      ))}
    </div>
  )
}
