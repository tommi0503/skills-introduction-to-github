import { ImagePlaceholder } from '../../../ui'
import { Lines } from '../components/Lines'
import { knowSection as s } from '../data'
import { theme } from '../theme'

/** "Know what you’re looking at." — right-aligned title, tall photo with credit, side copy. */
export function Know() {
  return (
    <>
      <div className="absolute right-[965px] top-[2940px] text-right">
        <Lines
          lines={s.title}
          hangingSpace
          style={{ fontSize: 66, lineHeight: '66px', letterSpacing: '-2.64px', color: theme.color.ink }}
        />
      </div>
      <div className="absolute left-[505px] top-[2719px] h-[640px] w-[420px] overflow-hidden rounded-[12px]">
        <ImagePlaceholder className="h-full w-full" />
        <div className="absolute left-0 top-[303px] flex w-full items-center justify-center gap-[4px] text-[16px] leading-[16px] text-white [text-shadow:0_0_6px_rgba(0,0,0,0.35)]">
          <span style={{ letterSpacing: '-0.18px' }}>{s.credit}</span>
          <span className="flex h-[34px] items-center rounded-[11px] px-[11px]" style={{ background: 'rgba(80,80,80,0.55)' }}>
            {s.creditName}
          </span>
        </div>
      </div>
      <Lines
        lines={s.body}
        className="absolute left-[955px] top-[2995px] text-[26px] leading-[29.9px]"
        style={{ color: theme.color.muted }}
      />
    </>
  )
}
