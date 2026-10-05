import { Panel, Placed } from '../../../ui'
import { autumn, fonts } from '../../shared-2829/theme'
import { cover } from '../data'

/** Panel 3 — cover with stacked title, dates and venue. */
export function CoverPanel() {
  const [autumnWord, flowerWord, festivalWord] = cover.words
  return (
    <Panel>
      <Placed x={0} y={150} width={480} className={`text-center ${fonts.display}`}>
        <p className="m-0 pl-[10px] text-[36px] leading-[40px]" style={{ color: autumn.oliveText }}>
          {cover.edition}
        </p>
      </Placed>
      <Placed x={0} y={205} width={480} className={`text-center ${fonts.display}`} style={{ color: autumn.brown }}>
        <p className="m-0 pl-[10px] text-[100px] leading-[110px]">{autumnWord}</p>
      </Placed>
      <Placed x={0} y={355} width={480} className={`text-center ${fonts.display}`} style={{ color: autumn.orangeText }}>
        <p className="m-0 pl-[10px] text-[70px] leading-[80px]">{flowerWord}</p>
      </Placed>
      <Placed x={0} y={482} width={480} className={`text-center ${fonts.display}`} style={{ color: autumn.brown }}>
        <p className="m-0 pl-[10px] text-[100px] leading-[110px]">{festivalWord}</p>
      </Placed>
      <Placed x={0} y={624} width={480} className="flex items-center justify-center gap-[9px] pl-[10px]" style={{ color: autumn.oliveText }}>
        {cover.dates.map((d, i) => (
          <span key={d.day} className="flex items-center gap-[9px]">
            {i > 0 && <span className="text-[26px] font-bold">~</span>}
            <span className="text-[27px] font-bold tracking-[-0.5px]">{d.date}</span>
            <span className="flex h-[30px] w-[30px] items-center justify-center rounded-full text-[14px] font-bold text-white" style={{ background: autumn.brown }}>
              {d.day}
            </span>
          </span>
        ))}
      </Placed>
      <Placed x={0} y={674} width={480} className="pl-[10px] text-center text-[17.5px] font-bold" style={{ color: autumn.oliveText }}>
        {cover.address}
      </Placed>
    </Panel>
  )
}
