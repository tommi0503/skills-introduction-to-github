import { Moon, RefreshCw } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { footerColumns, footerMeta, type FooterGroup } from '../data'
import { theme } from '../theme'

function Group({ group }: { group: FooterGroup }) {
  return (
    <div>
      <div className="text-[13px] font-[450] leading-[19.5px]">{group.title}</div>
      <ul className="mt-[6px] flex flex-col gap-[4px]">
        {group.links.map((l) => (
          <li key={l} className="text-[13px] leading-[21.125px]">
            {l}
          </li>
        ))}
      </ul>
    </div>
  )
}

export function Footer() {
  return (
    <footer className="mx-auto mt-[96px] border-t pt-[40px]" style={{ width: 1280, borderColor: theme.footerRule, color: theme.ink }}>
      <div className="mx-auto flex" style={{ width: theme.content }}>
        <div className="relative h-[360px] w-[345px] shrink-0 border-r border-dashed" style={{ borderColor: '#ececec' }}>
          <ImagePlaceholder label="SpaceXAI wordmark" style={{ width: 125, height: 14 }} />
          <div className="mt-[22px] text-[10px] leading-[10px]">{footerMeta.copyright}</div>
          <div className="absolute flex items-center" style={{ top: 330, left: 0 }}>
            <Moon size={16} strokeWidth={1.5} className="ml-[6px] text-black/30" />
            <span className="ml-[18px] flex h-[29px] items-center gap-[7px] rounded-full border border-[#ececec] px-[11px] text-[10px] font-[450] text-black/25">
              <RefreshCw size={12} strokeWidth={1.5} />
              {footerMeta.builtWith}
            </span>
          </div>
        </div>
        <div className="ml-[103px] flex shrink-0">
          {footerColumns.map((col, i) => (
            <div key={i} className="flex w-[168px] shrink-0 flex-col gap-[36px]">
              {col.map((g) => (
                <Group key={g.title} group={g} />
              ))}
            </div>
          ))}
        </div>
      </div>
    </footer>
  )
}
