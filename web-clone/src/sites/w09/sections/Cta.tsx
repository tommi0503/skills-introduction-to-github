import { FloatingTiles } from '../components/FloatingTiles'
import { PillButton } from '../components/PillButton'
import { ctaSection as s, ctaTiles } from '../data'
import { theme } from '../theme'

/** Closing canvas: drifting tiles around "Dream with us." and the big sign-up pill. */
export function Cta({ top }: { top: number }) {
  return (
    <section className="absolute left-0 h-[600px] w-[1440px]" style={{ top, background: theme.color.canvas }}>
      <FloatingTiles tiles={ctaTiles} />
      <div className="absolute left-0 top-[159px] flex flex-col items-center" style={{ width: theme.contentWidth }}>
        <p className="text-[26px] leading-[29.9px]" style={{ color: theme.color.ink }}>
          {s.lead}
        </p>
        <PillButton className="mt-[24px] h-[122px] w-[580px] font-normal" style={{ fontSize: 58, letterSpacing: '-2.32px' }}>
          {s.button}
        </PillButton>
      </div>
    </section>
  )
}
