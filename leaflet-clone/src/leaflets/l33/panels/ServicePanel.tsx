import { Panel, Placed } from '../../../ui'
import { SectionHeading } from '../../shared-3233/components/SectionHeading'
import { ServiceIntro } from '../../shared-3233/components/ServiceIntro'
import { TitledEntries } from '../../shared-3233/components/TitledEntries'
import { hutech } from '../../shared-3233/theme'
import type { ServiceContent } from '../data'

export interface ServicePanelProps {
  service: ServiceContent
}

/** Inside service panel: icon intro followed by accent-ruled sections (paragraph or titled entries). */
export function ServicePanel({ service }: ServicePanelProps) {
  return (
    <Panel background={hutech.paper} className="font-noto-sans" style={{ color: hutech.ink }}>
      <Placed x={service.inset} y={72}>
        <ServiceIntro iconBox={service.iconBox} label={service.label} headline={service.headline} />
      </Placed>
      <Placed x={service.inset} y={472} width={385} className="flex flex-col gap-y-[24px]">
        {service.sections.map((s) => (
          <section key={s.title}>
            <SectionHeading title={s.title} color={hutech.accent} titleClassName="text-[19.5px] leading-[28px]" gap={9} />
            {s.body && (
              <p className="m-0 mt-[20px] whitespace-pre-line text-[16.5px] leading-[26px] tracking-[-0.02em]" style={{ color: hutech.inkSoft }}>
                {s.body}
              </p>
            )}
            {s.entries && (
              <TitledEntries
                entries={s.entries}
                className="mt-[20px]"
                gap={27}
                titleClassName="text-[16.5px] leading-[26px]"
                bodyClassName="mt-[1px] text-[16.5px] leading-[22px] tracking-[-0.02em]"
              />
            )}
          </section>
        ))}
      </Placed>
    </Panel>
  )
}
