import { Users } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { StatusOverlay } from '../components/StatusOverlay'
import { season } from '../data'

function Chip({ label }: { label: string }) {
  return (
    <span className="absolute top-[16px] left-[16px] flex h-[22px] items-center rounded-full bg-white px-[12px] text-[8.5px] font-semibold">
      {label}
    </span>
  )
}

export function SeasonScreen() {
  return (
    <AppScreen background="#f5f5f5" className="font-sora text-[#111]">
      <StatusOverlay />
      <div className="absolute top-[71px] left-0 w-full text-center text-[17px] font-medium text-[#333] italic">{season.header}</div>
      <div className="absolute top-[114px] left-[20px] text-[23.5px] font-bold tracking-[0px] italic">{season.title}</div>
      <div className="absolute top-[156px] left-[20px] h-[319px] w-[350px] overflow-hidden rounded-[14px] border border-[#e6e6e6] bg-white">
        <ImagePlaceholder tone="#3a3540" label="season artwork" className="h-[110px] w-full" />
        <Chip label={season.chip} />
        <div className="mx-[16px] mt-[17px] flex h-[55px] items-center rounded-[8px] bg-[#ededed]">
          {season.stats.map((s, i) => (
            <div key={s.label} className="flex flex-1 flex-col items-center gap-[3px]" style={i ? { borderLeft: '1px solid #ddd' } : undefined}>
              <span className="text-[8.5px] text-[#999]">{s.label}</span>
              <span className="text-[12px] font-bold">{s.value}</span>
            </div>
          ))}
        </div>
        <p className="mt-[15.5px] px-[18px] text-center text-[8.5px] leading-[13px] text-[#555]">{season.text}</p>
        <div className="mx-[16px] mt-[16.5px] flex h-[41px] items-center justify-center rounded-[8px] bg-[#e8914a] text-[13.5px] font-semibold text-white shadow-[0_6px_16px_rgba(232,145,74,0.35)]">
          {season.cta}
        </div>
        <div className="mt-[10px] flex items-center justify-center gap-[4px] text-[8.5px] text-[#999]">
          <Users size={9} strokeWidth={2.4} />
          {season.joined}
        </div>
      </div>
      <div className="absolute top-[494px] left-[20px] text-[23.5px] font-bold tracking-[0px] italic">{season.duo.title}</div>
      <div className="absolute top-[537px] left-[20px] h-[175px] w-[350px] overflow-hidden rounded-[14px] border border-[#e6e6e6] bg-white">
        <ImagePlaceholder tone="#3b3633" label="duo artwork" className="h-[111px] w-full" />
        <Chip label={season.duo.chip} />
        <div className="absolute top-[64px] left-[16px] text-[24px] font-bold tracking-[0px] text-white italic">{season.duo.banner}</div>
        <div className="mt-[17px] pl-[16px] text-[12.5px] font-semibold text-[#555]">{season.duo.status}</div>
        <div className="mt-[3px] pl-[16px] text-[8px] text-[#777]">{season.duo.note}</div>
      </div>
      <BottomNav active="season" />
    </AppScreen>
  )
}
