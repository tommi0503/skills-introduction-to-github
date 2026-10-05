import { theme } from '../theme'

/** Horizontal dashed divider spanning the content column. */
export function DashedRule({ top }: { top: number }) {
  return (
    <div
      className="absolute h-px"
      style={{
        top,
        left: theme.column.left,
        width: theme.column.width,
        backgroundImage: `repeating-linear-gradient(to right, ${theme.rule} 0 3px, transparent 3px 5px)`,
      }}
    />
  )
}
