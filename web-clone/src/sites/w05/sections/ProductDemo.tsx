import { RotateCcw } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { productTabs } from '../data'
import { theme } from '../theme'
import { IconTile } from '../components/IconTile'

export function ProductDemo() {
  return (
    <section className="relative h-[705px]" style={{ background: theme.panel }}>
      <div
        className="absolute flex h-[66px] items-center gap-[4px] rounded-[10px] p-[8px]"
        style={{ left: 204, top: 31, width: 1000, background: '#3a3a3a', boxShadow: 'inset 0 1px 0 #4e4e4e, 0 0 0 1px #151515' }}
      >
        {productTabs.map((t, i) => (
          <div
            key={t.label}
            className={cn('flex h-[48px] flex-1 items-center justify-center gap-[13px] rounded-[6px] text-[14px] font-medium text-white')}
            style={i === 0 ? { background: '#4e4e4e' } : { borderLeft: i > 0 ? '1px solid #2a2a2a' : undefined }}
          >
            <IconTile accent={t.accent} icon={t.icon} />
            {t.label}
          </div>
        ))}
      </div>
      <ImagePlaceholder label="product demo video" tone={theme.media} className="absolute rounded-[24px]" style={{ left: 204, top: 120, width: 1000, height: 553 }} />
      <span className="absolute flex size-[44px] items-center justify-center rounded-[8px] bg-[#121212] text-white" style={{ left: 1148, top: 617 }}>
        <RotateCcw size={18} strokeWidth={2} />
      </span>
    </section>
  )
}
