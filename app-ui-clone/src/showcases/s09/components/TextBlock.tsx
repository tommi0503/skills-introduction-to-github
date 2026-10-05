import { theme } from '../theme'

/** Bold caption followed by muted multi-line copy. */
export function TextBlock({ title, lines }: { title: string; lines: string[] }) {
  return (
    <div>
      <div className="font-poppins text-[13.5px] leading-[20px] font-semibold" style={{ color: theme.ink }}>
        {title}
      </div>
      <div className="mt-[6px] font-poppins text-[13.5px] leading-[25.2px] whitespace-nowrap" style={{ color: '#b3b3b3' }}>
        {lines.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>
    </div>
  )
}
