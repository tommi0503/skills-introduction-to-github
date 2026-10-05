import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { ArcText } from '../../shared-1718/components/ArcText'
import { LabeledLine } from '../../shared-1718/components/LabeledLine'
import { RoundedBox } from '../../shared-1718/components/RoundedBox'
import { outsidePalette as c } from '../../shared-1718/theme'
import { invitation } from '../data'

/** Left outer flap: arched tagline, illustration, invitation card, date line. */
export function InvitationPanel() {
  return (
    <Panel background={c.cream}>
      <Placed x={100} y={78}>
        <ArcText text={invitation.arcTagline} width={290} height={50} rise={22} fontSize={19} color={c.accent} className="font-semibold" />
      </Placed>
      <ImagePlaceholder label="flying children illustration" className="absolute" style={{ left: 48, top: 125, width: 398, height: 165 }} />
      <RoundedBox x={51} y={318} width={389} height={600} radius={11} background={c.periwinkleSoft}>
        <div className="absolute left-0 right-0 flex flex-col items-center gap-[30px] text-center" style={{ top: 47, color: c.onPeriwinkle }}>
          {invitation.message.map((para) => (
            <div key={para[0]} className="text-[21px] font-medium leading-[32px]">
              {para.map((line) => (
                <p key={line} className="m-0">
                  {line}
                </p>
              ))}
            </div>
          ))}
        </div>
        <ImagePlaceholder label="library bookshelf illustration" className="absolute" style={{ left: 14, top: 257, width: 330, height: 345 }} />
      </RoundedBox>
      <Placed x={0} y={945} width={480} style={{ color: c.inkMuted }}>
        <LabeledLine
          items={invitation.footer}
          className="justify-center text-[16px]"
          labelClassName="font-bold"
          valueClassName="font-normal"
        />
      </Placed>
    </Panel>
  )
}
