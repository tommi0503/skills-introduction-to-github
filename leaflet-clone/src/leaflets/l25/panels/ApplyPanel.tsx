import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { FramedPill } from '../../shared-2425/components/FramedPill'
import { IconCircleItem } from '../../shared-2425/components/IconCircleItem'
import { NoticeBox } from '../components/NoticeBox'
import { howToApply, type StepAside } from '../data'
import { layout, panelBg } from '../theme'

const L = layout.apply

/** Right-hand element of a step: deadline pill, illustration or QR box. */
function Aside({ aside, top }: { aside: StepAside; top: number }) {
  if (aside.kind === 'pill')
    return (
      <Placed x={326} y={top + 28}>
        <FramedPill fill={library.yellow} width={106} height={33} className="text-[12.5px] font-semibold" style={{ color: library.deep }}>
          {aside.text}
        </FramedPill>
      </Placed>
    )
  if (aside.kind === 'qr')
    return (
      <Placed x={350} y={top - 2} width={85} height={83} className="box-border flex items-center justify-center rounded-[8px] border-2 border-[#ece8dc] bg-[#f6f6f4] text-[11px] font-medium text-[#45496b]">
        {aside.text}
      </Placed>
    )
  return (
    <Placed x={362} y={top + 2} width={63} height={62}>
      <ImagePlaceholder label={aside.label} className="h-full w-full rounded-[6px]" />
    </Placed>
  )
}

/** Panel 2 — 신청방법안내 steps and 유의사항. */
export function ApplyPanel() {
  return (
    <Panel background={panelBg.apply}>
      <Placed x={70} y={68} width={60} height={74}>
        <ImagePlaceholder label="pencil cup" className="h-full w-full rounded-[4px]" />
      </Placed>
      <Placed x={163} y={L.titleY} className="font-dohyeon text-[40px] leading-none tracking-[-0.03em]" style={{ color: library.title, WebkitTextStroke: `0.8px ${library.title}` }}>
        {howToApply.title}
      </Placed>
      <Placed x={61} y={L.ruleY} width={372} height={3} style={{ background: library.ink }} />
      {howToApply.steps.map((s, i) => (
        <div key={s.title}>
          <Placed x={58} y={L.stepYs[i]}>
            <IconCircleItem
              icon={s.icon}
              title={s.title}
              lines={s.lines}
              size={L.circle}
              iconSize={26}
              gap={19}
              circleClassName="bg-[#3c3f62]"
              titleClassName="mb-[4px] text-[17px] font-bold leading-[24px] tracking-[-0.02em] text-[#34385c]"
              lineClassName="text-[13.5px] font-semibold leading-[22px] text-[#4b4f72]"
            />
          </Placed>
          <Aside aside={s.aside} top={L.stepYs[i]} />
        </div>
      ))}
      {L.ruleYs.map((y) => (
        <Placed key={y} x={58} y={y} width={377}>
          <Divider dashed color={library.rule} thickness={1.5} />
        </Placed>
      ))}
      <NoticeBox title={howToApply.notice.title} items={howToApply.notice.items} style={{ left: L.notice.x, top: L.notice.y, width: L.notice.w, height: L.notice.h }} />
    </Panel>
  )
}
