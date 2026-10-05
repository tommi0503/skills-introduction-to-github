import { Check } from 'lucide-react'
import { Fragment } from 'react'
import { ImagePlaceholder } from '../../../ui'
import type { StepState } from '../data'
import { theme } from '../theme'

/** Horizontal step tracker: orange checks, a photo for the current stop, grey for pending. */
export function ShipmentProgress({ steps, size = 25, gap = 27.5 }: { steps: StepState[]; size?: number; gap?: number }) {
  return (
    <div className="flex items-center">
      {steps.map((s, i) => (
        <Fragment key={i}>
          {i > 0 && <Connector width={gap} active={steps[i - 1] === 'done'} />}
          <Step state={s} size={size} />
        </Fragment>
      ))}
    </div>
  )
}

function Step({ state, size }: { state: StepState; size: number }) {
  if (state === 'current') return <ImagePlaceholder className="rounded-full" style={{ width: size, height: size }} label="courier" />
  const done = state === 'done'
  return (
    <span
      className="flex items-center justify-center rounded-full"
      style={{
        width: size,
        height: size,
        background: done ? theme.orange : '#e6e2e2',
        boxShadow: `0 0 0 2.5px ${done ? '#fde1d2' : '#f4f1f1'}`,
        border: `1.5px solid ${done ? '#fff' : '#fff'}`,
      }}
    >
      <Check size={size * 0.5} strokeWidth={3} color={done ? '#fff' : '#bdb6b6'} />
    </span>
  )
}

function Connector({ width, active }: { width: number; active: boolean }) {
  return (
    <span
      className="mx-[1px]"
      style={{
        width,
        height: 2,
        backgroundImage: `linear-gradient(90deg, ${active ? theme.orange : '#cfcfcf'} 55%, transparent 55%)`,
        backgroundSize: '6px 2px',
      }}
    />
  )
}
