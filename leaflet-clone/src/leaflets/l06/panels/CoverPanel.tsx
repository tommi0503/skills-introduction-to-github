import { Flag, MapPin } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { cover } from '../data'
import { theme } from '../theme'

/** Front cover: dashed walking route with photo stickers and the 행궁동 동네한바퀴 title. */
export function CoverPanel() {
  return (
    <Panel background={theme.coverCream} style={{ color: theme.title }}>
      <svg className="absolute inset-0" width={480} height={1018}>
        <path d={cover.route} fill="none" stroke={theme.route} strokeWidth={4} strokeDasharray="14 8" />
      </svg>
      <Placed x={102} y={170}>
        <MapPin size={42} strokeWidth={2} color={theme.pinGreen} />
      </Placed>
      <Placed x={384} y={506}>
        <MapPin size={42} strokeWidth={2} color={theme.pinRed} />
      </Placed>
      <Placed x={350} y={380}>
        <Flag size={34} strokeWidth={1.8} color="#8b8f8c" />
      </Placed>
      {cover.stickers.map((s) => (
        <ImagePlaceholder
          key={s.label}
          label={s.label}
          className="absolute"
          style={{ left: s.x, top: s.y, width: s.w, height: s.h, transform: s.rotate ? `rotate(${s.rotate}deg)` : undefined }}
        />
      ))}
      <TextLines className="absolute text-[11px]" style={{ left: 97, top: 424, color: theme.muted }} lines={cover.kicker} lineClassName="leading-[17px]" />
      <Placed x={166} y={412} className="flex gap-[9px]">
        {cover.boxed.map((ch) => (
          <span
            key={ch}
            className="flex h-[62px] w-[58px] items-center justify-center rounded-[10px] border-[2.5px] border-dashed pt-[2px] font-dohyeon text-[48px] leading-none"
            style={{ borderColor: theme.title, background: theme.boxTint }}
          >
            {ch}
          </span>
        ))}
      </Placed>
      <Placed x={95} y={486} className="whitespace-nowrap origin-top scale-y-[1.2] font-dohyeon text-[72px] leading-[80px] tracking-[-0.045em]">
        {cover.title}
      </Placed>
      <TextLines
        className="absolute inset-x-0 pl-[6px] text-center font-gowun-batang text-[17px] font-bold"
        style={{ top: 757, color: theme.muted }}
        lines={cover.tagline}
        lineClassName="leading-[30px]"
      />
    </Panel>
  )
}
