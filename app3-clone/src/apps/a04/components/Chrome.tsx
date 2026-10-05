import { HomeIndicator, StatusBar } from '../../../ui'

/** Status bar and home bar shared by every screen. */
export function Chrome({ statusColor = '#000' }: { statusColor?: string }) {
  return (
    <>
      <StatusBar color={statusColor} className="absolute inset-x-0 top-0 z-40 font-inter" paddingX={34} paddingTop={19} />
      <HomeIndicator width={138} bottom={6} />
    </>
  )
}
