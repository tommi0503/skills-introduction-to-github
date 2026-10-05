import { Bookmark, MapPinned } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { FormField } from '../components/FormField'
import { GradientButton } from '../components/GradientButton'
import { NavHeader } from '../components/NavHeader'
import { Panel } from '../components/Panel'
import { deliveryScreen as d } from '../data'
import { theme } from '../theme'

export function DeliveryDetailsScreen() {
  return (
    <div className="absolute inset-0" style={{ color: theme.ink }}>
      <div className="absolute top-[50px] right-0 left-0">
        <NavHeader title={d.title} />
      </div>

      {/* Place card */}
      <Panel className="absolute top-[100px] right-0 left-0 h-[338px] px-[12px] pt-[10px]">
        <ImagePlaceholder className="h-[172px] w-full rounded-[11px]" label="isometric delivery map" />
        <div className="mt-[12px] flex items-center">
          <span className="flex h-[41px] w-[41px] items-center justify-center rounded-full bg-[#f3f3f3]">
            <Bookmark size={18} strokeWidth={2} fill="currentColor" />
          </span>
          <span className="ml-[10px] flex-1 text-[17.5px] tracking-[-0.2px]">{d.place.label}</span>
          <span className="flex h-[32px] w-[52px] items-center justify-center rounded-full bg-[#1f1f1f] text-[13px] text-white">
            {d.place.action}
          </span>
        </div>
        <div className="mt-[18px] text-[11.2px] tracking-[-0.2px]" style={{ color: '#8c8c8c' }}>
          {d.place.address}
        </div>
        <div className="mt-[12px] flex h-[42px] items-center justify-center gap-[6px] rounded-full bg-[#f4f4f4] text-[12px] tracking-[-0.15px]">
          <MapPinned size={16} strokeWidth={1.7} />
          {d.helpCta}
        </div>
      </Panel>

      {/* Recipient card */}
      <Panel className="absolute top-[455px] right-0 left-0 h-[223px] px-[16px] pt-[16px]">
        <div className="flex items-center justify-between">
          <span className="text-[18px] tracking-[-0.5px]">{d.recipient.title}</span>
          <span className="flex h-[28px] items-center rounded-full border border-[#e2e2e2] px-[11px] text-[10px] text-[#555]">
            {d.recipient.action}
          </span>
        </div>
        <div className="mt-[16px] flex flex-col gap-[10px]">
          {d.recipient.fields.map((f) => (
            <FormField key={f.key} label={f.label} placeholder={f.placeholder} />
          ))}
        </div>
      </Panel>

      {/* Package card */}
      <Panel className="absolute top-[694px] right-0 left-0 h-[150px] px-[16px] pt-[16px]">
        <div className="-mt-[3px] text-[18px] tracking-[-0.5px]">{d.packageTitle}</div>
        <div className="mt-[12px] flex justify-between">
          {d.packageKinds.map(({ key, label, icon: Icon }) => (
            <span key={key} className="flex h-[36px] w-[103px] items-center justify-center gap-[5px] rounded-[18px] bg-[#efefef] text-[12px] tracking-[-0.3px]">
              <Icon size={16} strokeWidth={1.6} />
              {label}
            </span>
          ))}
        </div>
      </Panel>

      {/* Fade + save */}
      <div
        className="absolute right-0 bottom-0 left-0 h-[86px]"
        style={{ background: `linear-gradient(180deg, rgba(246,246,246,0) 0%, ${theme.screen} 30%)` }}
      />
      <GradientButton label={d.save} icon={Bookmark} className="absolute top-[780px] right-[14px] left-[16px] h-[53px] text-[14px]" />
    </div>
  )
}
