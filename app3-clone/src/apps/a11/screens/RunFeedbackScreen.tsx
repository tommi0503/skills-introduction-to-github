import { Navigation, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { ChipRows } from '../components/Chip'
import { SheetScreen } from '../components/SheetScreen'
import { run as d } from '../data'

export function RunFeedbackScreen() {
  return (
    <SheetScreen
      className="font-inter"
      background="#ffffff"
      dim={0.5}
      sheetTop={80}
      sheetClassName="rounded-t-[14px] bg-white"
      backdrop={null}
      status={{
        color: '#111',
        time: d.time,
        timeAddon: <Navigation size={12} fill="currentColor" strokeWidth={0} className="rotate-0" />,
      }}
      overlay={<X size={22} strokeWidth={2} className="absolute top-[58px] right-[16px] text-[#111]" />}
    >
      <span className="absolute top-[7px] left-1/2 h-[4px] w-[36px] -translate-x-1/2 rounded-full bg-[#c4c4c4]" />
      <p className="absolute inset-x-0 top-[19px] text-center text-[17px] font-medium text-[#111]">{d.sheetTitle}</p>
      <div className="absolute inset-x-0 top-[47px] h-px bg-[#d9d9d9]" />
      <h2 className="absolute top-[81px] left-[25px] text-[22.5px] leading-[27px] font-medium tracking-[-0.1px] text-[#111]">
        {d.question.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h2>
      <ImagePlaceholder className="absolute top-[244px] left-[94px] h-[48px] w-[48px] rounded-full" label="thumbs down" />
      <div className="absolute top-[216px] left-[218px] flex h-[104px] w-[104px] items-center justify-center rounded-full bg-[#fdf1d3]">
        <ImagePlaceholder className="h-[48px] w-[48px] rounded-full" label="thumbs up" />
      </div>
      <p className="absolute top-[373px] left-[25px] text-[21px] font-medium text-[#111]">{d.moreTitle}</p>
      <ChipRows
        rows={d.tags}
        className="absolute top-[427px] left-[25px] flex flex-col gap-[8px]"
        rowClassName="gap-[9px]"
        chipClassName="h-[40px] border border-[#bdbdbd] px-[24px] text-[14px] font-medium text-[#111]"
      />
      <button
        type="button"
        className="absolute top-[587px] right-[26px] left-[25px] h-[62px] rounded-full bg-black text-[18px] font-medium text-white"
      >
        {d.action}
      </button>
      <p className="absolute inset-x-0 top-[673px] text-center text-[13px] text-[#8e8e8e]">{d.footer}</p>
    </SheetScreen>
  )
}
