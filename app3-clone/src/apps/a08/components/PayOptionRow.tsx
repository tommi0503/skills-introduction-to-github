import type { PayOption } from '../data'
import { airbnb } from '../theme'
import { Radio } from './Radio'

export function PayOptionRow({ option, selected }: { option: PayOption; selected: boolean }) {
  return (
    <div className="flex items-start justify-between" style={{ color: airbnb.ink }}>
      <div className="w-[285px]">
        <div className="text-[16px] leading-[20px] font-semibold">{option.title}</div>
        <p className="mt-[6px] text-[16px] leading-[21px]">
          {option.description}
          {option.link && (
            <>
              {' '}
              <span className="underline underline-offset-2">{option.link}</span>
            </>
          )}
        </p>
      </div>
      <Radio checked={selected} color={airbnb.ink} size={25} className="-mr-[2px]" />
    </div>
  )
}
