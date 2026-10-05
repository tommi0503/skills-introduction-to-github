import { Panel, Placed } from '../../../ui'
import { Lines, Shapes } from '../../shared-0812'
import { cover as d, coverArt } from '../data'
import { theme } from '../theme'

export function CoverPanel() {
  return (
    <Panel background={theme.cover}>
      <Shapes items={coverArt} />
      <Placed x={282} y={40} className="text-[14px] leading-[20px] font-bold text-white">
        {d.booking}
      </Placed>
      <Placed x={58} y={156} className="font-myeongjo text-white">
        <div className="text-[21px] leading-[30px] font-bold text-[#b9c0da]">{d.kicker}</div>
        <Lines lines={d.title} className="mt-[4px] text-[54px] leading-[69px] font-bold" />
      </Placed>
      <Placed x={58} y={385} className="text-[15px] leading-[22.5px] text-[#e9ecf5]">
        <div className="font-bold">{d.closed}</div>
        <Lines lines={d.hours} />
      </Placed>
    </Panel>
  )
}
