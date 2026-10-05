import { ChevronDown, Headset, MessageCircle, Plus } from 'lucide-react'
import { PhoneStatus } from '../components/PhoneStatus'
import { AppScreen, ChipGroup, SearchField } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { InboxRow } from '../components/InboxRow'
import { TabPill } from '../components/TabPill'
import { inboxChips, pinnedItems, tabs, threadItems } from '../data'

export function InboxScreen() {
  return (
    <AppScreen>
      <PhoneStatus />
      <div className="absolute top-[59px] left-[22px] flex h-[42px] w-[42px] items-center justify-center rounded-full bg-[#3fc35b] text-white">
        <MessageCircle size={24} fill="#fff" strokeWidth={0} />
      </div>
      <span className="absolute top-[58px] left-[80px] text-[17px] font-bold text-[#111]">Alex’s Inbox</span>
      <span className="absolute top-[86px] left-[77px] h-[20px] w-[104px] bg-[#ececec]" />
      <span className="absolute top-[71px] left-[204px] flex h-[18px] w-[18px] items-center justify-center rounded-full bg-[#eeeeee]">
        <ChevronDown size={12} strokeWidth={2.4} />
      </span>
      <CircleButton icon={Headset} variant="floating" className="absolute top-[59px] left-[274px]">
        <span className="absolute top-[11px] right-[11px] h-[6px] w-[6px] rounded-full bg-[#3fc35b]" />
      </CircleButton>
      <CircleButton icon={Plus} variant="floating" className="absolute top-[59px] left-[330px]" iconSize={22} />
      <SearchField
        placeholder="Search or Ask Beside AI"
        className="absolute top-[115px] left-[20px] h-[41px] w-[347px] rounded-full bg-[#f3f3f3] pl-[19px] text-[#555]"
        textClassName="text-[15px] text-[#7a7a7a]"
        iconSize={18}
      />
      <ChipGroup
        items={inboxChips}
        activeKey="all"
        gap={12}
        className="absolute top-[183px] left-[19px]"
        chipClassName="h-[35px] rounded-full px-[12px] text-[13.5px] font-medium text-[#555]"
        activeClassName="bg-[#efefef] text-[#111]"
        inactiveClassName="border border-[#e6e6e6]"
      />
      <div className="absolute top-[229px] inset-x-0">
        {pinnedItems.map((it) => (
          <InboxRow key={it.key} item={it} />
        ))}
      </div>
      <div className="absolute top-[483px] left-[22px] h-px w-[345px] bg-[#ececec]" />
      <div className="absolute top-[499px] inset-x-0">
        {threadItems.map((it) => (
          <InboxRow key={it.key} item={it} />
        ))}
      </div>
      <TabPill tabs={tabs} active="inbox" />
    </AppScreen>
  )
}
