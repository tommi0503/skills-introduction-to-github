import { StatusBar } from '../../../ui'

/** iOS status bar tuned to this board (light glyphs on dark headers, dark on maps). */
export function KitchenStatusBar({ tone = 'light' }: { tone?: 'light' | 'dark' }) {
  return (
    <StatusBar
      color={tone === 'light' ? '#fff' : '#111'}
      className="absolute inset-x-0 top-0"
      paddingTop={13}
      paddingX={30}
      fontSize={15}
      timeClassName="font-poppins font-medium"
    />
  )
}
