import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

export interface MediaCardProps { title?: string; body?: string; label: string }

/** 383×320 media tile with an optional caption below. */
export function MediaCard({ title, body, label }: MediaCardProps) {
  return (
    <div className="w-[383px]">
      <ImagePlaceholder label={label} className="h-[320px] w-full rounded-[4px]" />
      {title && (
        <p className="mt-[20px] px-[16px] text-[16px] leading-6" style={{ color: theme.grey }}>
          <span className="font-medium" style={{ color: theme.ink }}>{title}</span> {body}
        </p>
      )}
    </div>
  )
}
