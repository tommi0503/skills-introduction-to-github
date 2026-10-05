import { Bell, X } from 'lucide-react'

export interface NotificationCardProps {
  title: string
  body: string
  action: string
}

/** "Turn on notifications" prompt card. */
export function NotificationCard({ title, body, action }: NotificationCardProps) {
  return (
    <div className="relative rounded-[18px] border border-[#ebeae6] bg-white px-[15px] pt-[17px] pb-[15px]">
      <Bell size={20} strokeWidth={1.6} className="text-[#3d3d3a]" />
      <X size={17} strokeWidth={1.6} className="absolute top-[20px] right-[19px] text-[#6b6a65]" />
      <p className="mt-[16px] text-[15px] font-medium text-[#141413]">{title}</p>
      <p className="mt-[7px] text-[12.5px] leading-[18px] text-[#8d8c87]">{body}</p>
      <button type="button" className="mt-[13px] h-[40px] w-full rounded-full border border-[#dedcd6] text-[15px] text-[#3b64a8]">
        {action}
      </button>
    </div>
  )
}
