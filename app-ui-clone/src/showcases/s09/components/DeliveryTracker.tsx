import type { DeliveryStep } from '../data'
import { theme } from '../theme'

/** Step icons joined by dotted lime connectors. */
export function DeliveryTracker({ steps }: { steps: DeliveryStep[] }) {
  return (
    <div className="flex items-center">
      {steps.map((s, i) => {
        const Icon = s.icon
        return (
          <div key={s.key} className="flex flex-1 items-center last:flex-none">
            {s.done ? (
              <Icon size={s.size} strokeWidth={2.3} color={theme.lime} />
            ) : (
              <Icon size={s.size} strokeWidth={2} color={theme.dark} fill="#8a8a8a" />
            )}
            {i < steps.length - 1 && (
              <span
                className="mx-[6px] h-[3.5px] flex-1"
                style={{
                  backgroundImage: `radial-gradient(circle, ${steps[i + 1].done ? theme.lime : '#9a9a9a'} 1.6px, transparent 1.8px)`,
                  backgroundSize: '5.5px 3.5px',
                }}
              />
            )}
          </div>
        )
      })}
    </div>
  )
}
