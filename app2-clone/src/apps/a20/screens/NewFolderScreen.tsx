import { Check, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { GnStatusBar } from '../components/GnStatusBar'
import { IconCircle } from '../components/IconCircle'
import { FolderShape } from '../components/FolderShape'
import { PillTabs } from '../components/PillTabs'
import { SwatchGrid } from '../components/SwatchGrid'
import { newFolder } from '../data'
import { gn } from '../theme'

export function NewFolderScreen() {
  return (
    <AppScreen className="font-dm">
      <ImagePlaceholder className="absolute inset-0" tone="#f4f4f6" label="blurred colour background" />
      <GnStatusBar />
      <IconCircle icon={X} size={44} iconSize={24} strokeWidth={1.8} className="absolute left-[15px] top-[57px] bg-white" />
      <div className="absolute inset-x-0 top-[68px] text-center text-[16px] font-semibold text-black">{newFolder.title}</div>
      <IconCircle icon={Check} size={44} iconSize={27} strokeWidth={1.4} className="absolute left-[330px] top-[57px] bg-[#5186e8] text-white" />
      <FolderShape back={gn.folderBack} front={gn.folderFront} className="absolute left-[107px] top-[268px] h-[153px] w-[176px]" />
      <div className="absolute left-[59px] top-[463px] flex h-[30px] w-[272px] items-center justify-center rounded-full border border-[#e2e2e2] bg-white text-[22px] text-black">
        {newFolder.name}
      </div>
      <PillTabs
        items={newFolder.tabs}
        active="Color"
        className="absolute left-[19px] top-[511px] h-[30px] w-[353px] bg-[#e4e9ee]/80"
        itemClassName="text-[13px] font-semibold text-[#222]"
      />
      <SwatchGrid rows={newFolder.swatches} selected={newFolder.selected} className="absolute left-[82px] top-[568px]" />
    </AppScreen>
  )
}
