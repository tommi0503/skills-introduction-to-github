import { ImagePlaceholder } from '../../../ui'
import { Lines } from '../components/Lines'
import { Pill } from '../components/Pill'
import { mcp } from '../data'
import { theme, type } from '../theme'

export function Mcp() {
  return (
    <section className="absolute left-0 w-full" style={{ top: 3905, color: theme.ink }}>
      <div className="absolute" style={{ left: theme.gutter, top: 106 }}>
        <Lines lines={mcp.title} style={type.h2} />
        <div className="flex items-center gap-4" style={{ marginTop: 40 }}>
          <Pill variant="soft" paddingX={22}>
            {mcp.cta}
          </Pill>
          <span style={{ ...type.tiny, color: theme.muted }}>{mcp.note}</span>
        </div>
        <div className="flex items-center gap-[29px]" style={{ marginTop: 80 }}>
          {mcp.clients.map((c) => (
            <ImagePlaceholder key={c.label} label={`${c.label} logo`} style={{ width: c.w, height: 40 }} />
          ))}
        </div>
      </div>
      <ChatCard />
    </section>
  )
}

function ChatCard() {
  return (
    <div
      className="absolute overflow-hidden"
      style={{ left: 730, top: 0, width: 513, height: 513, borderRadius: 24, background: theme.surface, ...type.small }}
    >
      <p
        className="absolute"
        style={{ left: 130, top: 188, width: 319, padding: '20px 19px', background: theme.bubble, borderRadius: '20px 20px 0 20px' }}
      >
        {mcp.prompt.before}
        <strong style={{ fontWeight: 600 }}>{mcp.prompt.strong}</strong>
        {mcp.prompt.after}
      </p>
      <p className="absolute" style={{ left: 64, top: 300 }}>
        {mcp.result}
      </p>
    </div>
  )
}
