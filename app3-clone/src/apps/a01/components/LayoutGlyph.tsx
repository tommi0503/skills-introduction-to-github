/** Instagram "layout" tool glyph: rounded square split into a left column and two right cells. */
export function LayoutGlyph({ size = 24, strokeWidth = 2 }: { size?: number; strokeWidth?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={strokeWidth}>
      <rect x="2.5" y="2.5" width="19" height="19" rx="5" />
      <path d="M11 2.5v19M11 12.5h10.5" />
    </svg>
  )
}
