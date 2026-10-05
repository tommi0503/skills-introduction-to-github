import { CircleHelp } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { StatusRow } from '../components/StatusRow'
import { intro as d } from '../data'
import { nord } from '../theme'

export function Intro() {
  return (
    <AppScreen className="font-inter" style={{ color: nord.ink }}>
      <StatusRow />
      <CircleHelp size={21} strokeWidth={1.4} className="absolute top-[65px] left-[350px] text-[#5a5a5e]" />
      <ImagePlaceholder label="VPN illustration" className="absolute top-[182px] left-[100px] h-[190px] w-[190px] rounded-full" />
      <h1 className="absolute inset-x-0 top-[418px] text-center text-[19px] font-semibold">{d.title}</h1>
      <div className="absolute inset-x-0 top-[451px] text-center text-[15px] leading-[20.5px] text-[#808084]">
        {d.body.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
      <div className="absolute top-[581px] left-0 flex w-full justify-center gap-[9px]">
        {Array.from({ length: d.pages }, (_, i) => (
          <span key={i} className={cn('h-[7px] w-[7px] rounded-full', i === d.activePage ? 'bg-[#4f65f9]' : 'bg-[#cfcfd2]')} />
        ))}
      </div>
      <button
        className="absolute top-[630px] left-[15px] h-[48px] w-[358px] rounded-full text-[16px] font-medium text-white"
        style={{ background: nord.blue }}
      >
        {d.primary}
      </button>
      <button className="absolute top-[686px] left-[15px] h-[48px] w-[358px] rounded-full border border-[#d8d8db] text-[16px] font-medium">
        {d.secondary}
      </button>
      <div className="absolute inset-x-0 top-[755px] text-center text-[16px] font-medium" style={{ color: nord.blueText }}>
        {d.link}
      </div>
    </AppScreen>
  )
}
