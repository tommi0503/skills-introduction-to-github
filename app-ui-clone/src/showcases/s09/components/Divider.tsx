import { theme } from '../theme'

export function Divider({ inset = 0 }: { inset?: number }) {
  return <div className="h-px" style={{ background: theme.hairline, marginLeft: inset, marginRight: inset }} />
}
