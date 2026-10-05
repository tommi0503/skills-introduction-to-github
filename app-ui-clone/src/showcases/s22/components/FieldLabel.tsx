import { t22 } from '../theme'

export function FieldLabel({ children }: { children: string }) {
  return <div style={{ fontSize: 14.5, lineHeight: '18px', color: t22.label, letterSpacing: -0.4 }}>{children}</div>
}
