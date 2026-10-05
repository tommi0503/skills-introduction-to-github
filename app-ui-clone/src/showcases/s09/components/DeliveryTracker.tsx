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
              <Icon size={24} strokeWidth={2.2} color={theme.lime} />
            ) : (
              <Icon size={23} strokeWidth={2} color={theme.dark} fill="#8a8a8a" />
            )}
            {i < steps.length - 1 && (
              <span
                className="mx-[8px] h-[3px] flex-1"
                style={{
                  backgroundImage: `radial-gradient(circle, ${steps[i + 1].done ? theme.lime : '#9a9a9a'} 1.3px, transparent 1.5px)`,
                  backgroundSize: '5.5px 3px',
                }}
              />
            )}
          </div>
        )
      })}
    </div>
  )
}
