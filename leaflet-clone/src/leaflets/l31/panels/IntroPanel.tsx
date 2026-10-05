import { Panel, Placed } from '../../../ui'
import { ArtworkLayer } from '../../shared-3031/components/ArtworkLayer'
import { DisplayTitle } from '../../shared-3031/components/DisplayTitle'
import { RichLines } from '../../shared-3031/components/RichLines'
import { growth } from '../../shared-3031/theme'
import { intro } from '../data'

/** Panel 1 — programme introduction. */
export function IntroPanel() {
  return (
    <Panel>
      <Placed x={0} y={103} width={476}>
        <DisplayTitle lines={intro.title} color={growth.ink} className="text-[33px] leading-[50px] tracking-[2.5px]" />
      </Placed>
      <Placed x={74} y={253} className="flex flex-col gap-[24px]">
        {intro.paragraphs.map((p, i) => (
          <RichLines
            key={i}
            lines={p}
            className="text-[19px] font-medium leading-[25.7px] tracking-[-0.4px]"
            strongClassName="font-bold text-[var(--ink)]"
          />
        ))}
      </Placed>
      <ArtworkLayer items={[intro.figure]} />
    </Panel>
  )
}
