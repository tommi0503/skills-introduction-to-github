import { Panel, Placed } from '../../../ui'
import { SectionHeading } from '../../shared-3233/components/SectionHeading'
import { TitledEntries } from '../../shared-3233/components/TitledEntries'
import { hutech, hutechType } from '../../shared-3233/theme'
import { about } from '../data'

const heading = 'text-[20px] leading-[26px]'

/** Right outside panel: ABOUT US title, company philosophy and milestones. */
export function AboutPanel() {
  return (
    <Panel background={hutech.paper} className="font-noto-sans" style={{ color: hutech.ink }}>
      <Placed x={50} y={74}>
        <h2 className={`m-0 text-[44px] leading-[60px] ${hutechType.display}`} style={{ color: hutech.accent }}>
          {about.title}
        </h2>
        <p className="m-0 mt-[11px] text-[28px] leading-[40px]" style={{ color: hutech.inkSoft }}>
          {about.subtitle}
        </p>
      </Placed>

      <Placed x={48} y={354} width={390}>
        <SectionHeading title={about.philosophy.title} color={hutech.accent} titleClassName={heading} gap={10} />
        <TitledEntries
          entries={about.philosophy.entries}
          className="mt-[16px]"
          gap={30}
          titleClassName="text-[16.5px] leading-[24px]"
          bodyClassName="mt-[4px] text-[16.5px] leading-[21px] tracking-[-0.02em]"
        />
      </Placed>

      <Placed x={48} y={606} width={390}>
        <SectionHeading title={about.milestones.title} color={hutech.accent} titleClassName={heading} gap={10} />
        <ul className="m-0 mt-[13px] flex list-none flex-col gap-y-[8px] p-0 text-[16.2px] leading-[26px] tracking-[-0.01em]">
          {about.milestones.rows.map((r) => (
            <li key={r.year} className="flex">
              <span className="w-[50px] shrink-0 text-[17px] font-bold">{r.year}</span>
              <span className="whitespace-pre-line">{r.text}</span>
            </li>
          ))}
        </ul>
      </Placed>
    </Panel>
  )
}
