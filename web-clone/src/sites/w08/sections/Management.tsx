import { Button } from '../components/Button'
import { Lines } from '../components/Lines'
import { management, stages, type Stage } from '../data'
import { theme, type } from '../theme'

const GAP = 24

export function Management() {
  return (
    <section className="absolute left-0 w-full text-center" style={{ top: 3923, color: theme.ink }}>
      <p className="uppercase" style={type.eyebrow}>
        {management.eyebrow}
      </p>
      <h2 className={theme.display} style={{ ...type.h2, marginTop: 16 }}>
        <Lines lines={management.title} />
      </h2>
      <Lines lines={management.lead} style={{ ...type.lead, color: theme.muted, marginTop: 16 }} />
      <Button height={50} style={{ ...type.button, marginTop: 31, paddingInline: 21 }}>
        {management.cta}
      </Button>
      <div className="absolute flex text-left" style={{ left: 120, top: 398, gap: GAP }}>
        {stages.map((s, i) => (
          <StageCard key={s.title} stage={s} connector={i < stages.length - 1} />
        ))}
      </div>
    </section>
  )
}

function StageCard({ stage, connector }: { stage: Stage; connector: boolean }) {
  const Step = stage.step?.icon
  return (
    <div
      className="relative h-[400px] bg-white"
      style={{ width: stage.width, borderRadius: 32, padding: '32px 32px 0', boxShadow: '0 0 24px rgba(7,26,49,0.04)' }}
    >
      <h3 className={theme.display} style={type.h3}>
        {stage.title}
      </h3>
      {stage.body && <Lines lines={stage.body} style={{ ...type.small, color: theme.muted, marginTop: 11 }} />}
      {stage.step && Step && (
        <div className="flex items-center gap-3" style={{ ...type.small, color: theme.muted, marginTop: 16 }}>
          <span className="flex h-5 w-5 items-center justify-center rounded-full" style={{ background: '#d9f08f', color: theme.ink }}>
            <Step size={12} strokeWidth={2.4} />
          </span>
          {stage.step.text}
        </div>
      )}
      {connector && <Connector />}
    </div>
  )
}

/** White bridge between adjacent cards with two rounded background-coloured cut-outs. */
function Connector() {
  return (
    <span className="absolute bg-white" style={{ left: '100%', top: 40, width: GAP, height: 360 }}>
      <span className="absolute left-0 w-full" style={{ top: -40, height: 64, borderRadius: '0 0 12px 12px', background: theme.panel }} />
      <span className="absolute left-0 w-full" style={{ top: 37, bottom: 0, borderRadius: '12px 12px 0 0', background: theme.panel }} />
    </span>
  )
}
