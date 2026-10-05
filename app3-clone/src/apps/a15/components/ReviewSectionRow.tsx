import type { ReviewSection } from '../data'
import { palette as c } from '../theme'
import { GreyButton } from './GreyButton'

export function ReviewSectionRow({ section }: { section: ReviewSection }) {
  return (
    <div className="flex items-start justify-between">
      <div style={{ color: c.text }}>
        <div className="text-[13px] leading-[20px] font-semibold">{section.title}</div>
        {section.lines.map((l) => (
          <div key={l.text} className="mt-[2px] text-[13.5px] leading-[20px]">
            {l.text}
            {l.link && (
              <>
                {' '}
                <span className="font-semibold underline underline-offset-2">{l.link}</span>
              </>
            )}
          </div>
        ))}
      </div>
      {section.action && (
        <div className="mt-[1px]">
          <GreyButton label={section.action} />
        </div>
      )}
    </div>
  )
}
