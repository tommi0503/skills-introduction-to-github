import { larana } from '../../shared-3435/theme'
import type { Faq } from '../data'

/** Q./A. pairs with blue letter markers. */
export function FaqList({ faqs, className }: { faqs: Faq[]; className?: string }) {
  const row = (mark: string, text: string, strong: boolean) => (
    <p className={`m-0 flex leading-[30px] ${strong ? 'text-[17.5px] font-bold' : 'text-[15.5px] font-medium'}`}>
      <span className="w-[31px] shrink-0 text-[17px] font-bold" style={{ color: larana.label }}>
        {mark}
      </span>
      <span style={{ color: strong ? larana.ink : larana.inkSoft }}>{text}</span>
    </p>
  )
  return (
    <div className={`flex flex-col gap-y-[19px] ${className ?? ''}`}>
      {faqs.map((f) => (
        <div key={f.q}>
          {row('Q.', f.q, true)}
          {row('A.', f.a, false)}
        </div>
      ))}
    </div>
  )
}
