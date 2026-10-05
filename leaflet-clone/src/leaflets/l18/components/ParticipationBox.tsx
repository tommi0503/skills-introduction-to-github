import { RoundedBox } from '../../shared-1718/components/RoundedBox'
import { CornerFrame } from '../../shared-1718/components/CornerFrame'
import { LabeledLine } from '../../shared-1718/components/LabeledLine'
import type { FestivalPalette } from '../../shared-1718/theme'
import type { participation } from '../data'

export interface ParticipationBoxProps {
  content: typeof participation
  palette: FestivalPalette
  x: number
  y: number
  width: number
  height: number
  /** QR frame position relative to the box. */
  qr: { x: number; y: number; size: number }
}

/** Tinted band with registration info and a QR target spanning both inner panels. */
export function ParticipationBox({ content, palette, x, y, width, height, qr }: ParticipationBoxProps) {
  return (
    <RoundedBox x={x} y={y} width={width} height={height} radius={14} background={palette.periwinkleSoft}>
      <div className="absolute" style={{ left: 38, top: 29, width: 700 }}>
        <h3 className="m-0 text-[22px] font-bold leading-[36px]" style={{ color: palette.ink }}>
          {content.title}
        </h3>
        <div className="mt-[13px] text-[16.6px] leading-[27px]" style={{ color: palette.inkSoft }}>
          {content.lines.map((line) => (
            <p key={line} className="m-0 whitespace-nowrap">
              {line}
            </p>
          ))}
        </div>
        <div className="mt-[20px]" style={{ color: palette.inkSoft }}>
          <LabeledLine items={content.contacts} separator="  " gap={22} className="text-[14.5px]" labelClassName="font-semibold" />
        </div>
      </div>
      <div className="absolute flex flex-col items-center" style={{ left: qr.x, top: qr.y }}>
        <CornerFrame size={qr.size} arm={34} stroke={3} color={palette.onPeriwinkle}>
          <span className="text-[15px] font-bold" style={{ color: palette.onPeriwinkleSoft }}>
            {content.qr.label}
          </span>
        </CornerFrame>
        <span className="mt-[10px] text-[13px] font-medium" style={{ color: palette.onPeriwinkleSoft }}>
          {content.qr.caption}
        </span>
      </div>
    </RoundedBox>
  )
}
