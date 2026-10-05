import { CircleCheck, Link, Plus, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { place, saveSheet } from '../data'
import { theme } from '../theme'
import { Chrome } from '../components/Chrome'
import { OvalPhoto } from '../components/OvalPhoto'
import { PhotosCard } from '../components/PhotosCard'
import { ReactionTiles } from '../components/ReactionTiles'
import { SegmentToggle } from '../components/SegmentToggle'

export function SaveSheetScreen() {
  const s = saveSheet
  return (
    <AppScreen className="font-archivo" background={theme.pageBg}>
      <h1 className="a05-wide absolute inset-x-0 top-[68px] text-center text-[20.5px] font-bold leading-[24px] tracking-[-0.9px] text-black" style={{ fontStretch: '108%' }}>
        {place.name}
      </h1>
      <X size={26} strokeWidth={1.8} className="absolute left-[338px] top-[67px]" />
      <SegmentToggle items={s.segments} activeKey={s.active} className="absolute left-[16px] right-[8px] top-[118px] h-[34px]" />
      <ReactionTiles items={s.reactions} activeKey={s.activeReaction} className="absolute left-[17px] right-[17px] top-[166px]" />
      <PhotosCard uploaded={2} suggestions={2} label={s.addPhotos} className="absolute left-[16px] right-[18px] top-[250px] h-[284px]" />
      <div className="absolute left-[70px] right-[18px] top-[557px] h-[144px] rounded-[14px] bg-white">
        <p className="absolute left-[16px] top-[18px] text-[14.5px] text-[#b8b8bc]">{s.thoughtPlaceholder}</p>
        <div className="absolute left-[12px] right-[12px] top-[99px] h-px bg-[#e9e9ec]" />
        <p className="absolute left-[12px] top-[112px] flex items-center gap-[7px] text-[12.5px] text-[#c4c4c8]">
          <Link size={13} strokeWidth={1.8} color="#aaa" />
          {s.addLink}
        </p>
      </div>
      <OvalPhoto className="absolute left-[16px] top-[646px] h-[55px] w-[42px]" />
      <p className="a05-wide absolute left-[20px] top-[735px] text-[15px] font-bold tracking-[-0.6px] text-[#111]">{s.curation}</p>
      <div className="absolute left-[338px] top-[730px] flex h-[29px] w-[30px] items-center justify-center rounded-[8px] bg-white" style={{ boxShadow: theme.softShadow }}>
        <Plus size={18} strokeWidth={1.6} />
      </div>
      <div className="absolute left-[15px] right-[15px] top-[783px] h-[80px] rounded-[14px] bg-white/70">
        <ImagePlaceholder label="curation cover" className="absolute left-[11px] top-[17px] h-[63px] w-[120px] rounded-[4px]" />
        <p className="absolute left-[144px] top-[30px] text-[16px] text-[#8f8f93]">{s.note}</p>
      </div>
      <div className="absolute left-[22px] right-[24px] top-[750px] flex h-[62px] items-center justify-center gap-[10px] rounded-full bg-black text-white">
        <CircleCheck size={22} fill="#fff" color="#000" strokeWidth={2} />
        <span className="a05-wide text-[20px] font-bold tracking-[-0.6px]" style={{ fontStretch: '110%' }}>{s.save}</span>
      </div>
      <Chrome />
    </AppScreen>
  )
}
