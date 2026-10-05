import { Fragment } from 'react'
import { Divider, ImagePlaceholder, Panel, Pill, Placed } from '../../../ui'
import { cover, goods } from '../data'
import { theme } from '../theme'
import { WavyBlob } from '../components/WavyBlob'
import { LineBlock } from '../components/LineBlock'

/** Panel 3 — front cover on a wavy cream blob. */
export function CoverPanel() {
  return (
    <Panel>
      <Placed x={22} y={59} width={438} height={911}>
        <WavyBlob width={438} height={911} step={95} depth={22} label="wavy cream blob" />
      </Placed>
      <Placed x={99} y={109} width={293} height={65}>
        <Pill className="h-full w-full bg-[#fdd20e] text-[23px] text-[#1b1b1b]">{cover.tag}</Pill>
      </Placed>
      <Placed x={0} y={188} width={480}>
        <LineBlock lines={cover.title} className="text-center font-blackhan text-[78px] leading-[82px] tracking-[0.02em] text-[#1b1b1b]" />
      </Placed>
      {goods.map((g) => (
        <Placed key={g.label} x={g.x} y={g.y} width={g.w} height={g.h}>
          <ImagePlaceholder label={g.label} className="h-full w-full" tone="#d6d9de" style={{ borderRadius: g.radius }} />
        </Placed>
      ))}
      <Placed x={0} y={720} width={480}>
        <LineBlock lines={cover.info} className="text-center text-[25px] leading-[36px] text-[#1b1b1b]" />
      </Placed>
      <Placed x={64} y={847} width={362}>
        <Divider color={theme.green} thickness={2} />
      </Placed>
      <Placed x={0} y={871} width={480} className="flex justify-center gap-[6px] text-[20px] font-bold text-[#1b1b1b]">
        {cover.categories.map((c, i) => (
          <Fragment key={c}>
            {i > 0 && <span className="font-normal">|</span>}
            <span>{c}</span>
          </Fragment>
        ))}
      </Placed>
    </Panel>
  )
}
