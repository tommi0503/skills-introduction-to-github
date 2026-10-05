import { ChevronRight } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { drawerPromo, primaryMenu, profile, secondaryMenu } from '../data'
import { theme } from '../theme'

/** Left navigation drawer (profile, coupon promo, menu). */
export function SideDrawer({ className }: { className?: string }) {
  return (
    <div className={cn('absolute inset-y-0 left-0 z-20 w-[317px] bg-white font-pretendard', className)}>
      <div className="absolute top-[74px] left-[26px]">
        <div className="text-[18.5px] font-bold leading-[22px] tracking-[0px]" style={{ color: theme.navy }}>
          {profile.name}
        </div>
        <div className="mt-[4.5px] text-[13.5px] leading-[16px] text-[#777]">{profile.phone}</div>
        <div className="mt-[15.6px] text-[13px] leading-[16px] text-[#666]">{profile.credit}</div>
      </div>
      <ChevronRight size={18} strokeWidth={1.4} color="#9a9a9a" className="absolute top-[85px] left-[280px]" />

      <div className="absolute top-[166px] left-0 h-[62.5px] w-full overflow-hidden bg-[#edf0f2]">
        <div className="absolute top-[15px] left-[26px]">
          <div className="text-[15px] font-bold leading-[18px] tracking-[-0.3px]" style={{ color: theme.navy }}>
            {drawerPromo.title}
          </div>
          <div className="mt-[3px] flex items-center text-[11.2px] tracking-[-0.2px] text-[#333]">
            {drawerPromo.link}
            <ChevronRight size={10} strokeWidth={2} />
          </div>
        </div>
        <ImagePlaceholder
          label="쿠폰 표지판 그래픽"
          tone="#cfd4dc"
          className="absolute top-0 left-[182px] h-full w-[135px]"
          style={{ clipPath: 'polygon(100% 0, 100% 100%, 0 100%)' }}
        />
      </div>

      <div className="absolute top-[239.2px] left-[26px] right-0">
        {primaryMenu.map((item) => (
          <div
            key={item.label}
            className={cn('flex flex-col', item.caption ? 'h-[73.6px] pt-[15.2px]' : 'h-[51.6px] justify-center')}
          >
            <div className="text-[17.5px] leading-[20px] tracking-[-0.1px] text-[#1c1c1e]">{item.label}</div>
            {item.caption && (
              <div className="mt-[9px] text-[13px] leading-[14px] tracking-[-0.1px]" style={{ color: theme.passport }}>
                {item.caption}
              </div>
            )}
          </div>
        ))}
        <div className="mt-[11.7px] mb-[18px] h-px bg-[#efeff2]" />
        {secondaryMenu.map((label) => (
          <div key={label} className="flex h-[39px] items-center text-[14.8px] tracking-[-0.2px] text-[#666a78]">
            {label}
          </div>
        ))}
      </div>
    </div>
  )
}
