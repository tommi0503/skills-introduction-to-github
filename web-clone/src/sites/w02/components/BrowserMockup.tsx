import { ChevronDown, ChevronLeft, ChevronRight, ChevronUp, Ellipsis, History, KeyRound, PanelLeft, Plus, RotateCw, SquarePen } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { mockup, type SidebarItem } from '../data'
import { theme } from '../theme'

const LIGHTS = ['#ff6467', '#ffb900', '#00c950']
const divider = 'rgba(0, 40, 50, 0.12)'

function SidebarRow({ item }: { item: SidebarItem }) {
  const Icon = item.icon
  const color = item.muted ? theme.grey : theme.ink
  const hasLead = Boolean(Icon || item.logo)
  return (
    <div
      className={cn('relative flex h-[32.5px] items-center text-[14px] leading-5 font-[450]', item.selected && 'rounded-[8px] bg-white')}
      style={{
        color,
        paddingLeft: 7,
        boxShadow: item.selected ? `0 0 0 1px ${divider}, 0 1px 2px rgba(0,0,0,0.04)` : undefined,
      }}
    >
      {Icon && <Icon className="size-[14px]" strokeWidth={1.75} style={{ color: theme.grey }} />}
      {item.logo && <ImagePlaceholder label={`${item.label} icon`} className="size-[14px] rounded-[3px]" />}
      <span className={cn('truncate', hasLead && 'ml-[8px]')} style={{ maxWidth: hasLead ? 184 : 205 }}>{item.label}</span>
      {item.trailing === 'spinner' && <span className="absolute right-[4px] size-[11px] rounded-full border-[1.5px] border-[#d4d4d4] border-t-transparent" />}
      {item.trailing === 'dot' && <span className="absolute right-[5px] size-[6px] rounded-full bg-[#00a6f4]" />}
      {item.trailing === 'count' && (
        <span className="absolute right-[8px] flex items-center gap-[7px] text-[12px] font-medium" style={{ color: theme.grey }}>
          3 <ChevronDown className="size-[11px]" />
        </span>
      )}
    </div>
  )
}

/** Translucent desktop-browser window shown in the hero (clipped by the hero card). */
export function BrowserMockup({ className }: { className?: string }) {
  return (
    <div
      className={cn('absolute overflow-hidden rounded-t-[16px] tracking-[-0.03em]', className)}
      style={{ border: `1px solid ${divider}`, background: 'rgba(255,255,255,0.93)' }}
    >
      {/* Sidebar */}
      <aside className="absolute inset-y-0 left-0 w-[229px] px-[6px]" style={{ background: 'rgba(255,255,255,0.72)', borderRight: `1px solid ${divider}` }}>
        <div className="flex h-[40px] items-center gap-[6px] pl-[12px]">
          {LIGHTS.map((c) => <span key={c} className="size-[12px] rounded-full" style={{ background: c }} />)}
          <PanelLeft className="ml-auto mr-[10px] size-[14px]" style={{ color: theme.grey }} />
        </div>
        <div className="grid grid-cols-3 gap-[5px] pl-[1px]">
          {Array.from({ length: mockup.tiles }, (_, i) => (
            <div key={i} className="flex h-[36px] items-center justify-center rounded-[8px]" style={{ background: 'rgba(0,30,40,0.1)', boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.5)' }}>
              <ImagePlaceholder label="bookmark icon" className="size-[14px] rounded-[3px]" />
            </div>
          ))}
        </div>
        {mockup.sidebar.map((g, gi) => (
          <div key={g.title} className={gi ? 'mt-[6px]' : 'mt-[9px]'}>
            <div className="flex h-[25px] items-center pl-[7px] text-[13px] leading-[19.5px] font-medium" style={{ color: theme.grey }}>{g.title}</div>
            <div className="mt-[2px]">{g.items.map((it) => <SidebarRow key={it.label} item={it} />)}</div>
          </div>
        ))}
      </aside>

      {/* Main pane */}
      <div className="absolute inset-y-0 left-[230px] right-0 text-[14px] leading-5">
        <div className="flex h-[40px] items-center pl-[11px] pr-[10px]" style={{ color: theme.grey }}>
          <ChevronLeft className="size-[18px]" strokeWidth={1.75} />
          <ChevronRight className="ml-[11px] size-[18px]" strokeWidth={1.75} />
          <RotateCw className="ml-[13px] size-[14px]" strokeWidth={1.75} />
          <ImagePlaceholder label="Aside icon" className="ml-[13px] size-[14px] rounded-full" />
          <span className="ml-[7px] font-medium">{mockup.address.site}</span>
          <span className="ml-[15px] font-[450]">{mockup.address.title}</span>
          <KeyRound className="ml-auto size-[17px]" strokeWidth={1.5} />
        </div>
        <div className="flex h-[38px] items-center pl-[13px]">
          <SquarePen className="size-[14px]" style={{ color: theme.grey }} />
          <span className="ml-[11px] font-medium tracking-[-0.14px]" style={{ color: theme.ink }}>{mockup.chatTitle}</span>
          <Ellipsis className="ml-[9px] size-[14px]" style={{ color: theme.grey }} />
        </div>
        <div className="flex justify-end pr-[52px] pt-[8px]">
          <span className="rounded-[16.8px] px-[11px] py-[4px] text-[14px] leading-[19.6px] tracking-[-0.14px]" style={{ background: 'rgba(0,0,0,0.08)', color: theme.ink }}>{mockup.prompt}</span>
        </div>
        <p className="mt-[33px] pl-[36px]" style={{ color: theme.ink }}>{mockup.reply}</p>
        <div className="mt-[11px] flex items-center pl-[36px]" style={{ color: theme.grey }}>
          <History className="size-[14px]" />
          <span className="ml-[10px]">{mockup.search.lead}</span>
          <span className="ml-[4px] font-medium" style={{ color: theme.link }}>{mockup.search.term}</span>
          <ChevronUp className="ml-[9px] size-[14px]" />
        </div>
        <div className="ml-[57px] mr-[52px] mt-[8px] rounded-[8px] bg-white px-[7px] py-[5px]" style={{ boxShadow: `0 0 0 1px ${divider}` }}>
          {mockup.results.map((r) => (
            <div key={r.title} className="flex h-[25px] items-center text-[12px] leading-4">
              {r.logo ? <ImagePlaceholder label="source icon" className="size-[14px] rounded-[4px]" /> : <KeyRound className="size-[14px]" style={{ color: theme.grey }} />}
              <span className="ml-[6px] font-medium whitespace-pre" style={{ color: 'rgba(10,10,10,0.85)' }}>{r.title}</span>
              <span className="ml-[6px]" style={{ color: theme.grey }}>{r.detail}</span>
              <span className="ml-auto font-medium" style={{ color: theme.grey }}>{r.meta}</span>
            </div>
          ))}
        </div>
        <div className="absolute left-[14px] right-[32px] top-[571px] flex h-[70px] items-start rounded-[16px] bg-white px-[6px] pt-[6px]" style={{ boxShadow: `0 0 0 1px ${divider}` }}>
          <span className="flex size-[24px] items-center justify-center rounded-full bg-[#f5f5f5]"><Plus className="size-[14px]" style={{ color: theme.grey }} /></span>
          <span className="ml-[7px] mt-[2px]" style={{ color: theme.grey }}>{mockup.input}</span>
          <span className="ml-auto size-[26px] rounded-full bg-[#0a0a0a]" />
        </div>
      </div>
    </div>
  )
}
