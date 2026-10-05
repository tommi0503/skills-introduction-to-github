import { StatusBar } from '../../../ui'

/** Status bar as laid out in the Rakuten recordings (time visible, no highlight chip). */
export function PhoneStatusBar() {
  return (
    <StatusBar
      fontSize={17}
      paddingX={39}
      paddingTop={19}
      timeClassName="pl-[15px] tracking-[-0.2px]"
      className="absolute inset-x-0 top-0"
    />
  )
}
