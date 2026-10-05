import type { WheelColumn } from '../data'

const ROW = 38.2
const COLORS = ['#b8b8b8', '#8a8a8c', '#191a1c', '#8a8a8c', '#b8b8b8']

/** iOS-style 3-column wheel snapshot with the middle row highlighted. */
export function DateWheel({ columns }: { columns: WheelColumn[] }) {
  return (
    <div className="relative" style={{ height: ROW * 5 }}>
      <div
        className="absolute"
        style={{ left: 14.4, right: 14.4, top: ROW * 2 - 1.8, height: 41.2, background: '#f6f7f9', borderRadius: 6 }}
      />
      {columns.map((col) =>
        col.items.map((label, row) =>
          label ? (
            <span
              key={`${col.x}-${row}`}
              className="absolute flex items-center"
              style={{
                left: col.x - 1,
                top: ROW * row,
                height: ROW,
                fontSize: 19.5,
                color: COLORS[row],
                fontWeight: row === 2 ? 500 : 400,
                letterSpacing: -0.4,
              }}
            >
              {label}
            </span>
          ) : null,
        ),
      )}
    </div>
  )
}
