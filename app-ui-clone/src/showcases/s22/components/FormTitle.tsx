import { t22 } from '../theme'

/** Large bold page heading; lines are passed explicitly to keep the reference wrapping. */
export function FormTitle({ lines, top }: { lines: string[]; top: number }) {
  return (
    <h1
      className="absolute whitespace-pre-line"
      style={{ left: 20, top, fontSize: 22, lineHeight: '27px', fontWeight: 700, color: t22.title, letterSpacing: -0.5 }}
    >
      {lines.join('\n')}
    </h1>
  )
}
