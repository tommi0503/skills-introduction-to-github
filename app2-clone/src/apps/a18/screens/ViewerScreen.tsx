import { ChevronLeft, Ellipsis, Star } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { ActionBar } from '../components/ActionBar'
import { Chrome } from '../components/Chrome'
import { viewer } from '../data'

export function ViewerScreen() {
  return (
    <AppScreen className="font-dm">
      <Chrome />
      <div className="absolute inset-x-0 top-[66px] flex h-[44px] items-center px-[16px] text-[#1f1f1f]">
        <ChevronLeft size={26} strokeWidth={1.8} />
        <div className="absolute inset-x-0 text-center">
          <p className="text-[16px] leading-[20px] font-medium">{viewer.date}</p>
          <p className="text-[11.5px] leading-[14px] text-[#5f6368]">{viewer.time}</p>
        </div>
        <span className="flex-1" />
        <Star size={21} strokeWidth={1.6} className="mr-[22px]" />
        <Ellipsis size={20} strokeWidth={2} />
      </div>
      <ImagePlaceholder label="T-shirt photo" className="absolute inset-x-0 top-[179px] h-[488px]" />
      <ActionBar items={viewer.actions} />
    </AppScreen>
  )
}
