import { ArrowLeft, MessageCircle, Phone } from 'lucide-react'
import { Avatar, HomeIndicator, ImagePlaceholder } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { DeliveryTracker } from '../components/DeliveryTracker'
import { KitchenStatusBar } from '../components/KitchenStatusBar'
import { RoundAction } from '../components/RoundAction'
import { delivery } from '../data'
import { theme } from '../theme'

/** Live delivery tracking: map + dark bottom sheet with ETA, steps and courier. */
export function MapScreen() {
  return (
    <div className="absolute inset-0">
      <ImagePlaceholder label="delivery route map" className="absolute inset-0" />
      <KitchenStatusBar tone="dark" />
      <Box rect={{ x: 19.5, y: 54, w: 83, h: 34 }}>
        <div className="flex h-full items-center justify-center gap-[7px] rounded-[7px] font-poppins text-[14.5px] font-semibold text-white" style={{ background: theme.dark }}>
          <ArrowLeft size={17} strokeWidth={2.2} />
          Back
        </div>
      </Box>

      <div className="absolute inset-x-0 bottom-0 rounded-t-[22px]" style={{ top: 538, background: theme.dark }}>
        <div className="pt-[21.5px] text-center font-poppins">
          <div className="text-[13.5px] leading-[20px] font-semibold text-white">{delivery.title}</div>
          <div className="mt-[5px] text-[13px] leading-[20px] text-[#b5b5b5]">{delivery.subtitle}</div>
        </div>
        <div className="absolute inset-x-0 top-[85.6px] border-t border-[#353535]" />
        <div className="absolute top-[106px] right-[45px] left-[41px]">
          <DeliveryTracker steps={delivery.steps} />
        </div>
        <div className="absolute inset-x-0 top-[162px] border-t border-[#353535]" />
        <div className="absolute top-[179px] right-[21px] left-[18px] flex items-center">
          <Avatar size={57} tone="#d6d6d6" />
          <div className="ml-[11px] flex-1 font-poppins">
            <div className="text-[15px] leading-[21px] font-semibold text-white">{delivery.courier.name}</div>
            <div className="text-[13px] leading-[20px] text-[#9b9b9b]">{delivery.courier.role}</div>
          </div>
          <div className="flex gap-[12px]">
            <RoundAction icon={Phone} />
            <RoundAction icon={MessageCircle} dot />
          </div>
        </div>
        <HomeIndicator tone="light" width={116} bottom={6} />
      </div>
    </div>
  )
}
