import { Bell, CloudCheck, LayoutGrid, ListFilter, Plus, Search } from 'lucide-react'
import { AppScreen, Avatar } from '../../../ui'
import { GnStatusBar } from '../components/GnStatusBar'
import { DocTile } from '../components/DocTile'
import { Dock } from '../components/Dock'
import { columns, dockTabs, documents } from '../data'
import { gn } from '../theme'

export function DocumentsScreen() {
  return (
    <AppScreen className="font-dm">
      <GnStatusBar />
      <div className="absolute left-[213px] top-[57px] flex h-[45px] w-[159px] items-center justify-between rounded-full bg-white px-[13px] shadow-[0_2px_14px_rgba(0,0,0,0.08)]">
        <Search size={20} strokeWidth={1.8} />
        <Bell size={20} strokeWidth={1.6} />
        <Avatar size={32} text="A" className="[&>div]:!bg-[#25301f] [&>div]:!text-white [&>div]:!text-[12px]" />
      </div>
      <h1 className="absolute left-[17px] top-[111px] text-[32px] font-bold tracking-[-0.3px] text-black">Documents</h1>

      <div className="absolute left-[21px] top-[183px] flex items-center gap-[10px] text-[15px] text-[#222]">
        <ListFilter size={20} strokeWidth={1.6} />
        All
      </div>
      <div className="absolute left-[176px] top-[175px] flex h-[35px] w-[92px] items-center justify-center gap-[6px] rounded-full text-[15px] text-white" style={{ background: gn.blue }}>
        <Plus size={18} strokeWidth={1.8} />
        New
      </div>
      <LayoutGrid size={19} strokeWidth={1.6} className="absolute left-[284px] top-[183px]" />
      <span className="absolute left-[320px] top-[178px] h-[27px] w-px bg-[#ddd]" />
      <CloudCheck size={21} strokeWidth={1.6} className="absolute left-[337px] top-[182px]" />

      {documents.map((d, i) => (
        <DocTile key={d.title.join()} item={d} center={columns[i % 3]} />
      ))}

      <Dock tabs={dockTabs} active="documents" className="absolute left-[24px] top-[765px] w-[342px]" />
    </AppScreen>
  )
}
