import { ImagePlaceholder } from '../../../ui'
import { nav } from '../data'
import { theme } from '../theme'
import { DownloadButton } from '../components/DownloadButton'

export function Nav() {
  return (
    <header className="relative flex h-[96px] items-center px-[145px]">
      <ImagePlaceholder label="Monologue app icon" tone="#2f7f86" className="size-12 rounded-[10px]" />
      <span className={`${theme.wordmark} ml-[11px] text-[38px] leading-[34px] tracking-[-1.52px]`} style={{ color: theme.ink }}>
        <i>{nav.wordmarkInitial}</i>
        {nav.wordmarkRest}
      </span>
      <nav className="ml-[129px] flex gap-[24px] text-[14px] font-medium" style={{ color: theme.text82 }}>
        {nav.links.map((l) => (
          <span key={l}>{l}</span>
        ))}
      </nav>
      <div className="ml-auto flex gap-[13px]">
        <DownloadButton variant="dark" className="w-[193px]">
          {nav.ios}
        </DownloadButton>
        <DownloadButton className="w-[193px]">{nav.mac}</DownloadButton>
      </div>
    </header>
  )
}
