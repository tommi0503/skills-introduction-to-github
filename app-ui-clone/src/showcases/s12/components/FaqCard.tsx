import { theme } from '../theme'
import { Starburst } from './Starburst'

export interface FaqItem {
  question: string
  answer: string[]
  open: boolean
}

/** White FAQ card with the "?" seal on its top-right corner. */
export function FaqCard({ item, height }: { item: FaqItem; height: number }) {
  return (
    <div className="relative w-[335px] rounded-[34px] bg-white" style={{ height }}>
      <div className="absolute top-[-8px] right-[0px]">
        <Starburst size={71}>
          <span className="text-[30px] leading-none font-bold">?</span>
        </Starburst>
      </div>
      <div className="absolute top-[38px] left-[35.5px] w-[240px] text-[24px] leading-[31px] font-medium tracking-[-0.035em] text-[#111]">
        {item.question}
      </div>
      {item.open && (
        <div className="absolute top-[118px] left-[35.5px] w-[256px] text-[16.2px] font-[450] leading-[21.8px] tracking-[-0.03em] text-[#222]">
          {item.answer.map((p) => (
            <p key={p} className="mb-[21.8px]">
              {p}
            </p>
          ))}
          <span className="font-bold" style={{ color: theme.brand }}>
            + Less
          </span>
        </div>
      )}
    </div>
  )
}
