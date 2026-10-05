export interface BulletNotesProps {
  items: string[]
}

/** Rounded grey panel with "•" bullet notes. */
export function BulletNotes({ items }: BulletNotesProps) {
  return (
    <div style={{ background: '#f5f6f8', borderRadius: 8, padding: '20px 16px 16px 15px' }}>
      {items.map((t, i) => (
        <div key={i} className="flex" style={{ marginTop: i ? 10.3 : 0 }}>
          <span className="relative shrink-0" style={{ width: 9 }}>
            <span className="absolute rounded-full" style={{ left: 0.5, top: 6.5, width: 2.6, height: 2.6, background: '#8d8d8f' }} />
          </span>
          <p
            className="whitespace-pre-line"
            style={{ fontSize: 14, lineHeight: '19.6px', color: '#6b6b6d', letterSpacing: -0.35, fontWeight: 350 }}
          >
            {t}
          </p>
        </div>
      ))}
    </div>
  )
}
