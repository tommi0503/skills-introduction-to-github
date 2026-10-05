import { StatusBar } from '../../../ui'

/** Status bar positioned as in the Instagram recordings. */
export function IgStatusBar({ color = '#000' }: { color?: string }) {
  return <StatusBar color={color} className="absolute inset-x-0 top-0" paddingX={34} paddingTop={19} />
}
