import { Smile } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { HandLine } from '../components/HandLine'
import { PillHeading } from '../components/PillHeading'
import { groupPhoto, reviews } from '../data'
import { theme } from '../theme'

/** Inside-left: 이용소감 reviews with smiley markers + polaroid group photo. */
export function ReviewsPanel() {
  const { frame, photo } = groupPhoto
  return (
    <Panel background={theme.cream} style={{ color: theme.ink }}>
      <PillHeading x={104} y={90} width={271}>
        {reviews.heading}
      </PillHeading>
      {reviews.items.map((r) => (
        <Placed key={r.y} x={44} y={r.y} className="flex gap-[8px]">
          <Smile size={40} strokeWidth={1.4} color={theme.smile} className="-mt-[1px] shrink-0" />
          <div className="font-gaegu text-[13px] font-bold tracking-[-0.01em]">
            {r.lines.map((l) => (
              <HandLine key={l.text} marked={l.marked} className="leading-[21px]">
                {l.text}
              </HandLine>
            ))}
          </div>
        </Placed>
      ))}
      <Placed x={frame.x} y={frame.y} width={frame.w} height={frame.h} style={{ background: '#f6f5f3' }} />
      <ImagePlaceholder label="group photo" className="absolute" style={{ left: photo.x, top: photo.y, width: photo.w, height: photo.h }} />
    </Panel>
  )
}
