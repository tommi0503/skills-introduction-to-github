import { ChevronDown } from 'lucide-react'
import { Fragment } from 'react'
import { larana } from '../../shared-3435/theme'

export interface StepFlowProps {
  steps: string[]
  className?: string
}

/** Vertical process: outlined capsules with numbered badges, joined by chevrons. */
export function StepFlow({ steps, className }: StepFlowProps) {
  return (
    <ol className={`m-0 flex list-none flex-col items-center p-0 ${className ?? ''}`}>
      {steps.map((s, i) => (
        <Fragment key={s}>
          {i > 0 && <ChevronDown size={22} strokeWidth={2.4} className="my-[10px]" color={larana.blue} />}
          <li
            className="flex h-[64px] w-full items-center justify-center gap-[12px] rounded-full"
            style={{ border: `2px solid ${larana.cardLine}`, background: '#eef2f9' }}
          >
            <span
              className="flex h-[20px] w-[32px] items-center justify-center rounded-full text-[13px] font-bold text-white"
              style={{ background: larana.blue }}
            >
              {String(i + 1).padStart(2, '0')}
            </span>
            <span className="text-[16.5px] font-bold" style={{ color: larana.ink }}>
              {s}
            </span>
          </li>
        </Fragment>
      ))}
    </ol>
  )
}
