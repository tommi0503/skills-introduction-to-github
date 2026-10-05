import { DynamicIsland, HomeIndicator, StatusBar } from '../../../ui'

/** Status bar, island (with privacy dot) and home bar of the mockup. */
export function DeviceChrome() {
  return (
    <>
      <StatusBar className="absolute inset-x-0 top-0 font-inter" paddingX={50} paddingTop={14} fontSize={16} />
      <DynamicIsland width={103} height={28} top={10} />
      <span className="absolute top-[22px] left-[211px] z-50 h-[5px] w-[5px] rounded-full bg-[#f29a1f]" />
      <HomeIndicator width={130} bottom={8} />
    </>
  )
}
