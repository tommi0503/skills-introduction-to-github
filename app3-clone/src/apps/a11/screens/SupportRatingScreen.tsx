import { ArrowLeft, Ellipsis } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import { ChipRows } from '../components/Chip'
import { SheetScreen } from '../components/SheetScreen'
import { support as d } from '../data'

function ChatBackdrop() {
  return (
    <>
      <ArrowLeft size={22} strokeWidth={2} className="absolute top-[58px] left-[15px] text-[#111]" />
      <Ellipsis size={22} strokeWidth={2.4} className="absolute top-[58px] right-[19px] text-[#111]" />
      <p className="absolute inset-x-0 top-[47px] text-center text-[15px] leading-[20px] text-[#111]">{d.header}</p>
      <p className="absolute inset-x-0 top-[71px] text-center text-[13px] leading-[18px] text-[#9a9a9a]">{d.headerSub}</p>
      <ImagePlaceholder className="absolute top-[153px] left-[210px] h-[62px] w-[95px] rounded-[6px]" tone="#2b4cc1" label="card image" />
      <span className="absolute top-[183px] left-[311px] rounded-full bg-[#c9c9c9] px-[8px] py-[1px] text-[11px] text-white">
        {d.messageTime}
      </span>
    </>
  )
}

export function SupportRatingScreen() {
  const rows = [d.reasons.slice(0, 2), d.reasons.slice(2, 4), d.reasons.slice(4)]
  return (
    <SheetScreen
      className="font-inter"
      background="#ffffff"
      dim={0.81}
      sheetTop={213}
      sheetClassName="rounded-t-[22px] bg-[#f7f7f7]"
      backdrop={<ChatBackdrop />}
      status={{ color: '#111' }}
      statusDimmed
    >
      <span className="absolute top-[14px] left-1/2 h-[4px] w-[50px] -translate-x-1/2 rounded-full bg-[#c8c9cd]" />
      <h2 className="absolute top-[34px] left-[17px] text-[19.5px] leading-[29px] font-bold text-[#111]">
        {d.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h2>
      <span className="absolute top-[38px] right-[17px] text-[16px] font-medium text-[#3d71dc]">{d.skip}</span>
      <p className="absolute top-[110px] left-[17px] text-[13.5px] text-[#8b8b8b]">{d.subtitle}</p>
      <div className="absolute top-[150px] right-[17px] left-[17px] flex h-[122px] justify-center gap-[33px] rounded-[14px] bg-white pt-[23px]">
        {d.ratings.map((r) => (
          <div key={r.label} className="flex w-[46px] flex-col items-center">
            <ImagePlaceholder className={cn('h-[46px] w-[46px] rounded-full', !r.selected && 'opacity-60')} label={`${r.label} emoji`} />
            <span className={cn('mt-[15px] text-[14px]', r.selected ? 'text-[#111]' : 'text-[#a6a6a6]')}>{r.label}</span>
          </div>
        ))}
      </div>
      <p className="absolute top-[291px] left-[17px] text-[17.5px] font-semibold text-[#111]">{d.reasonsTitle}</p>
      <ChipRows
        rows={rows}
        className="absolute top-[328px] left-[17px] flex flex-col gap-[10px]"
        rowClassName="gap-[8px]"
        chipClassName="h-[40px] bg-[#e4e5e9] px-[15px] text-[14px] font-medium text-[#222]"
      />
      <div className="absolute inset-x-0 top-[500px] h-px bg-[#efefef]" />
      <button
        type="button"
        className="absolute top-[520px] right-[17px] left-[17px] h-[53px] rounded-full bg-[#3f67df] text-[16px] font-medium text-white"
        style={{ boxShadow: '0 4px 14px rgba(63,103,223,0.35)' }}
      >
        {d.action}
      </button>
    </SheetScreen>
  )
}
