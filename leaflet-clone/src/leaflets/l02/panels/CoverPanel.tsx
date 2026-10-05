import { Heart } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed, VerticalText } from '../../../ui'
import { coverPanel } from '../data'
import { theme } from '../theme'
import { OutlineBadge } from '../components/OutlineBadge'

/** Panel 1 — photo cover, stacked wordmark, vertical poem, coupon. */
export function CoverPanel() {
  const { badge, wordmark, poem, coupon } = coverPanel
  return (
    <Panel background={theme.paper}>
      <Placed x={0} y={0} width={480} height={588}>
        <ImagePlaceholder label="house photo" className="h-full w-full" tone={theme.photoOnLight} />
      </Placed>
      <Placed x={50} y={70}>
        <OutlineBadge label={badge} className="bg-white px-[15px]" />
      </Placed>
      <Placed x={51} y={462} width={89} height={271} className="flex justify-center gap-[6px] bg-[#f4f4f4] pt-[4px]">
        <VerticalText className="font-poppins text-[26px] font-bold leading-[26px] tracking-[0.15em] text-[#111]">{wordmark.strong}</VerticalText>
        <VerticalText className="mt-[18px] font-poppins text-[25px] font-light leading-[26px] tracking-[0.2em] text-[#111]">{wordmark.light}</VerticalText>
      </Placed>
      <Placed x={170} y={620} width={210}>
        <VerticalText className="text-[22px] font-bold leading-[29px] tracking-[-0.06em] text-[#1e1e1e] [&>span]:block">
          {poem.map((col, i) => (
            <span key={col} style={{ marginLeft: i % 2 === 1 ? 17 : 0 }}>{col}</span>
          ))}
        </VerticalText>
      </Placed>
      <Placed x={44} y={900} width={118}>
        <p className="m-0 text-center font-poppins text-[5.5px] font-semibold leading-none tracking-[0.3em] text-[#222]">{coupon.caption}</p>
        <ImagePlaceholder label="barcode" className="mt-[4px] h-[36px] w-full" tone={theme.photoOnLight} />
      </Placed>
      <Placed x={182} y={897} width={250} height={50} className="flex items-center justify-between rounded-[6px] border-[1.5px] border-[#c8c8c8] bg-[#f6f6f6] pl-[17px] pr-[17px]">
        <span className="text-[17px] text-[#1e1e1e]">{coupon.label}</span>
        <Heart size={22} fill="#1e1e1e" strokeWidth={0} />
      </Placed>
    </Panel>
  )
}
