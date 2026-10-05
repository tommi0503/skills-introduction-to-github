import { Heart } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed, VerticalText } from '../../../ui'
import { interviewPanel as d } from '../data'
import { theme } from '../theme'
import { OutlineBadge } from '../components/OutlineBadge'
import { Lines } from '../components/Lines'

/** Panel 2 — artist interview with side title and two artwork photos. */
export function InterviewPanel() {
  return (
    <Panel background={theme.white}>
      <Placed x={40} y={72} width={46} className="flex justify-center">
        <VerticalText mode="rotate" className="font-poppins text-[41px] font-light leading-none tracking-[0.12em] text-[#111]">{d.sideTitle}</VerticalText>
      </Placed>
      <Placed x={52} y={618} className="flex flex-col items-center gap-[10px] text-[#1e1e1e]">
        <Heart size={23} fill="currentColor" strokeWidth={0} />
        <Heart size={23} fill="currentColor" strokeWidth={0} />
      </Placed>
      <Placed x={52} y={712} className="flex">
        <VerticalText mode="rotate" className="font-poppins text-[10.5px] leading-[15px] tracking-[0.17em] text-[#444] [&>span]:block">
          {d.sideCaption.map((c) => (
            <span key={c}>{c}</span>
          ))}
        </VerticalText>
      </Placed>
      <Placed x={147} y={72}>
        <OutlineBadge label={d.badge} className="border-[1.5px] border-[#2a2a2a] bg-white px-[13px]" />
      </Placed>
      <Placed x={147} y={117}>
        <Lines lines={d.heading} className="text-[20px] font-semibold leading-[31px] text-[#1e1e1e]" />
        <Lines lines={d.intro} className="mt-[19px] text-[18px] leading-[31px] text-[#6b6b6b]" />
      </Placed>
      <Placed x={147} y={307} width={273} height={166}>
        <ImagePlaceholder label="artist photo" className="h-full w-full rounded-[14px]" />
      </Placed>
      <Placed x={147} y={496}>
        <p className="m-0 font-poppins text-[16px] font-semibold leading-none text-[#1e1e1e]">{d.artist.name}</p>
        <p className="m-0 mt-[13px] font-poppins text-[12.5px] font-semibold leading-none text-[#6b6b6b]">{d.artist.role}</p>
      </Placed>
      <Placed x={147} y={602} width={273} height={166}>
        <ImagePlaceholder label="artwork photo" className="h-full w-full rounded-[14px]" />
      </Placed>
      <Placed x={147} y={792} className="font-poppins leading-none text-[#1e1e1e]">
        <span className="text-[16px] font-semibold">{d.work.title}</span>
        <span className="ml-[5px] text-[13px] text-[#555]">{d.work.year}</span>
      </Placed>
      <Placed x={147} y={846}>
        <Lines lines={d.body} className="text-[18px] leading-[32px] text-[#6b6b6b]" />
      </Placed>
    </Panel>
  )
}
