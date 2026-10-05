import { ImagePlaceholder } from '../../../ui'
import { Pill } from '../components/Pill'
import { cookie } from '../data'
import { theme, type } from '../theme'

/** Grey framed product screenshot with the (fixed) cookie banner floating over it. */
export function ProductPreview() {
  return (
    <>
      <section
        className="absolute overflow-hidden"
        style={{ left: 158, top: 776, width: 1125, height: 682, borderRadius: 40, background: theme.surface }}
      >
        <ImagePlaceholder
          label="Mobbin app screenshot"
          className="absolute"
          style={{ left: 40, top: 40, width: 1045, height: 642, borderRadius: '24px 24px 0 0' }}
        />
      </section>
      <CookieBanner />
    </>
  )
}

function CookieBanner() {
  return (
    <div
      className="absolute flex items-center rounded-full"
      style={{
        left: 509,
        top: 808,
        width: 422,
        height: 60,
        background: theme.banner,
        color: theme.white,
        paddingLeft: 24,
        boxShadow: '0 12px 32px rgba(0,0,0,0.12)',
      }}
    >
      <span style={{ ...type.nav, fontWeight: 456 }}>
        {cookie.text} <span className="underline underline-offset-2">{cookie.link}</span>
      </span>
      <Pill variant="light" height={36} paddingX={12} style={{ ...type.small, fontWeight: 600, marginLeft: 49 }}>
        {cookie.accept}
      </Pill>
      <Pill variant="outline" height={36} paddingX={12} style={{ ...type.small, fontWeight: 600, marginLeft: 8 }}>
        {cookie.deny}
      </Pill>
    </div>
  )
}
