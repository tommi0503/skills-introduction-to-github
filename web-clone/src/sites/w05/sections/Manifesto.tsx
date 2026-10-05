import { manifesto } from '../data'
import { accents, theme } from '../theme'
import { IconTile } from '../components/IconTile'

export function Manifesto() {
  return (
    <section className="h-[761px] pt-[219px]" style={{ color: theme.text48 }}>
      <div className="mx-auto w-[760px] text-[24px] leading-[37.2px] tracking-[-0.72px]">
        <h2>{manifesto.lead}</h2>
        <p className="mt-[29px]">
          {manifesto.body.map((part, i) =>
            typeof part === 'string' ? (
              <span key={i}>{part}</span>
            ) : (
              <strong key={i} className="whitespace-nowrap font-medium" style={{ color: accents[part.accent].text }}>
                <IconTile accent={part.accent} icon={part.icon} className="mr-[8px] align-[-3px]" />
                {part.word}
              </strong>
            ),
          )}
        </p>
        <p className="mt-[27px]">{manifesto.close}</p>
      </div>
    </section>
  )
}
