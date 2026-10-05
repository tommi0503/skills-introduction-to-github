import { EyebrowLink } from '../components/EyebrowLink'
import { MediaCard } from '../components/MediaCard'
import { passwords } from '../data'
import { theme } from '../theme'

export function Passwords() {
  return (
    <section className="absolute inset-x-0 top-[4057px] h-[443px]">
      <EyebrowLink label={passwords.link} className="absolute left-[241px] top-[96px]" />
      <h2 className={`${theme.fonts.display} absolute left-[241px] top-[144px] text-[44px] leading-[48px] font-[450]`} style={{ color: theme.ink }}>
        {passwords.title}
      </h2>
      <p className="absolute left-[241px] top-[208px] w-[958px] text-[18px] leading-7" style={{ color: theme.grey }}>
        {passwords.body.map((l) => <span key={l} className="block">{l}</span>)}
      </p>
      <div className="absolute left-[121px] top-[360px] flex gap-[24.5px]">
        {Array.from({ length: passwords.cards }, (_, i) => <MediaCard key={i} label="password manager demo" />)}
      </div>
    </section>
  )
}
