import { CircleHelp, Pencil, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder, StatusBar } from '../../../ui'
import { BlockButton } from '../components/BlockButton'
import { DeadlineBadge } from '../components/DeadlineBadge'
import { Pill } from '../components/Pill'
import { SettingListRow } from '../components/SettingListRow'
import { group } from '../data'
import { ue } from '../theme'

export function GroupOrder() {
  return (
    <AppScreen className="font-inter" background="#fff">
      <StatusBar />
      <div className="flex items-center justify-between px-[22px] pt-[14px]">
        <X size={20} strokeWidth={1.8} />
        <CircleHelp size={19} strokeWidth={2} />
      </div>
      <ImagePlaceholder className="absolute top-[115px] left-[105px] h-[91px] w-[180px] rounded-[4px]" label="group order illustration" />
      <div className="absolute inset-x-[16px] top-[234px]">
        <div className="flex items-center justify-between">
          <h1 className="text-[32.5px] leading-[38px] font-bold tracking-[-0.6px]">{group.title}</h1>
          <Pencil size={20} strokeWidth={1.5} color={ue.pencil} className="mt-[6px]" />
        </div>
        <p className="mt-[5px] text-[14px] leading-[21px]" style={{ color: ue.muted }}>
          From <span className="font-medium text-black">{group.from}</span>
        </p>
        <p className="text-[14px] leading-[21px]" style={{ color: ue.muted }}>
          Deliver to <span className="font-medium text-black">{group.deliverTo}</span>
        </p>
        <div className="mt-[23px] flex h-[70px] items-center rounded-[8px] pr-[15px] pl-[18px]" style={{ background: ue.field }}>
          <DeadlineBadge />
          <p className="mr-[12px] ml-[20px] flex-1 text-[12.5px] leading-[18px]">{group.nudge}</p>
          <Pill className="h-[35px] bg-black px-[13px] text-[13.5px] font-semibold text-white">{group.nudgeCta}</Pill>
        </div>
      </div>
      <div className="absolute inset-x-0 top-[421px]">
        {group.settings.map((r) => (
          <SettingListRow key={r.key} row={r} />
        ))}
      </div>
      <div className="absolute inset-x-[16px] top-[742px]">
        <BlockButton className="h-[55px] text-[16px]">{group.cta}</BlockButton>
      </div>
    </AppScreen>
  )
}
