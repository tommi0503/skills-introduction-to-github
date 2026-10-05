import { Bell, Plus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

/** Google Photos top bar: product mark, create, notifications, account. */
export function LibraryHeader({ initial }: { initial: string }) {
  return (
    <div className="absolute inset-x-0 top-[71px] flex h-[31px] items-center pr-[13px] pl-[17px] text-[#1f1f1f]">
      <ImagePlaceholder label="Google Photos logo" className="size-[29px] rounded-full" />
      <span className="flex-1" />
      <span className="relative mr-[26px]">
        <Plus size={22} strokeWidth={1.7} />
        <span className="absolute -top-[2px] -right-[3px] size-[6px] rounded-full bg-[#d93025]" />
      </span>
      <Bell size={20} strokeWidth={1.7} className="mr-[28px]" />
      <span className="relative flex size-[31px] items-center justify-center rounded-full text-[16px] text-white" style={{ background: theme.avatar }}>
        {initial}
        <span className="absolute -right-[3px] -bottom-[3px] size-[13px] rounded-full border-[1.5px] border-white bg-[#f1f3f4]" />
      </span>
    </div>
  )
}
