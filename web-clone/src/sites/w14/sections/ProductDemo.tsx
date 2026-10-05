import { ChevronDown, CircleHelp, Search, Sparkles, Trash2, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { assistant, demoTabs, docsApp } from '../data'
import { colors, fonts, shadows } from '../theme'
import { PillButton } from '../components/primitives'

/** Page-space geometry of the demo (section starts at `top`). */
const geo = {
  art: { x: -60, y: 577, w: 1560, h: 690 },
  tabs: { y: 606 },
  frame: { x: 160, y: 626, w: 1120, h: 647 },
  cta: { y: 1212 },
}

function DemoTabs() {
  return (
    <div
      className={`flex h-[38px] items-center gap-[4px] rounded-full border px-[5px] ${fonts.sans}`}
      style={{ background: colors.subtle, borderColor: colors.border }}
    >
      {demoTabs.map((t, i) => (
        <span
          key={t}
          className="flex h-[30px] items-center rounded-full px-[10px] text-[14px] leading-[22.4px] font-medium"
          style={i === 0 ? { background: colors.orange, color: '#fff' } : { background: '#fff', color: colors.body }}
        >
          {t}
        </span>
      ))}
    </div>
  )
}

function DocsTopBar() {
  return (
    <div className="flex h-[50px] shrink-0 items-center pl-[20px] pr-[20px] pt-[1px]">
      <ImagePlaceholder label="Acme logo" style={{ width: 55, height: 18 }} />
      <div className="ml-[185px] flex h-[25px] w-[198px] items-center rounded-[6px] border px-[6px]" style={{ borderColor: '#e8dcd9' }}>
        <Search size={11} strokeWidth={2} color={colors.mockMuted} />
        <span className="ml-[6px] flex-1 text-[10px] leading-[12px]" style={{ color: colors.mockMuted }}>
          {docsApp.search}
        </span>
        {docsApp.keys.map((k) => (
          <span
            key={k}
            className="ml-[2px] rounded-[3px] border px-[2px] font-spacemono text-[8px] leading-[10px]"
            style={{ borderColor: colors.border, color: colors.mockMuted }}
          >
            {k}
          </span>
        ))}
      </div>
      <Sparkles className="ml-[15px]" size={14} strokeWidth={1.6} color={colors.body} />
      <span className="ml-[6px] text-[12px]" style={{ color: colors.mockMuted }}>
        {docsApp.ask}
      </span>
      <span className="ml-auto flex h-[24px] items-center rounded-[5px] border px-[8px] text-[12px]" style={{ borderColor: colors.border, color: colors.ink }}>
        {docsApp.signIn}
      </span>
    </div>
  )
}

function DocsTabs() {
  return (
    <div className="flex h-[25px] shrink-0 items-stretch gap-[24px] border-b pl-[20px] whitespace-nowrap" style={{ borderColor: colors.border }}>
      {docsApp.tabs.map(({ label, icon: Icon, active }) => (
        <span
          key={label}
          className="flex shrink-0 items-start gap-[6px] text-[12px] leading-[13px] font-medium"
          style={{ color: active ? colors.orange : colors.mockMuted, borderBottom: active ? `1px solid ${colors.orange}` : undefined }}
        >
          <Icon size={14} strokeWidth={1.5} className="-mt-[1px]" />
          <span className="pt-[1px]">{label}</span>
        </span>
      ))}
    </div>
  )
}

function DocsSidebar() {
  return (
    <aside className="ml-[20px] w-[190px] border-l pt-[20px]" style={{ borderColor: colors.border }}>
      {docsApp.sidebar.map((group, gi) => (
        <div key={group.title} className={gi ? 'mt-[13px]' : ''}>
          <p className={`pl-[10px] text-[10px] leading-[10px] font-semibold uppercase ${fonts.mono}`} style={{ color: colors.ink }}>
            {group.title}
          </p>
          <ul>
            {group.items.map(({ label, icon: Icon, active }) => (
              <li
                key={label}
                className={`relative -ml-px flex h-[31.6px] items-center gap-[6px] pl-[10px] text-[11px] ${fonts.ui}`}
                style={{ color: colors.mockMuted, borderLeft: active ? '1px solid #ffaa8d' : '1px solid transparent' }}
              >
                <Icon size={14} strokeWidth={1.4} />
                {label}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </aside>
  )
}

function DocsMain() {
  return (
    <main className={`ml-[20px] w-[513px] pt-[16px] ${fonts.ui}`}>
      <div className="flex items-center justify-between">
        <p className={`text-[10px] leading-[10px] font-semibold uppercase ${fonts.mono}`} style={{ color: colors.muted }}>
          {docsApp.eyebrow}
        </p>
        <span className="flex h-[20px] items-center rounded-[4px] border text-[9px]" style={{ borderColor: colors.border, color: colors.mockMuted }}>
          <span className="flex items-center gap-[3px] border-r px-[5px]" style={{ borderColor: colors.border }}>
            <Sparkles size={9} /> {docsApp.ask}
          </span>
          <ChevronDown size={11} className="mx-[2px]" />
        </span>
      </div>
      <h3 className="mt-[11px] text-[20px] leading-[26px] font-semibold tracking-[-0.6px]" style={{ color: colors.ink }}>
        {docsApp.title}
      </h3>
      <p className="mt-[6px] text-[14px] leading-[19.6px] tracking-[-0.14px]" style={{ color: colors.fadedText }}>
        {docsApp.intro}
      </p>
      <div className="mt-[20px] grid grid-cols-[247px_247px] gap-x-[20px] gap-y-[20px]">
        {docsApp.cards.map((c, i) => (
          <div key={i} className="h-[246px] overflow-hidden rounded-[8px] border" style={{ borderColor: colors.border }}>
            <ImagePlaceholder label="card illustration" style={{ width: '100%', height: 170 }} />
            <div className="px-[14px] pt-[14px]">
              <h6 className="text-[15px] leading-[21px] font-semibold tracking-[-0.45px]" style={{ color: colors.ink }}>
                {c.title}
              </h6>
              <p className="mt-[6px] text-[12px] leading-[19.2px]" style={{ color: colors.fadedText }}>
                {c.text}
              </p>
            </div>
          </div>
        ))}
      </div>
    </main>
  )
}

function AssistantPanel() {
  return (
    <div className={`relative flex h-full w-[320px] flex-col border-l ${fonts.ui}`} style={{ borderColor: colors.border, background: '#fff' }}>
      <div className="flex h-[36px] items-center px-[16px] pt-[16px]">
        <Sparkles size={18} strokeWidth={1.6} color={colors.ink} />
        <span className="ml-[10px] text-[14px] leading-[14px] font-medium" style={{ color: colors.ink }}>
          {assistant.title}
        </span>
        <Trash2 className="ml-auto" size={13} strokeWidth={1.5} color="#a8a29e" />
        <X className="ml-[16px]" size={14} strokeWidth={1.6} color={colors.body} />
      </div>
      <div className="mt-[36px] self-end mr-[16px] flex h-[40px] w-[232px] items-center px-[16px] text-[13px]" style={{ background: colors.orangeSoft, color: colors.ink, borderRadius: '16px 4px 16px 16px' }}>
        {assistant.question}
      </div>
      <p className="mt-[28px] w-[240px] pl-[16px] text-[13px] leading-[20.8px] font-medium" style={{ color: colors.ink }}>
        {assistant.answer.map((s) => (
          <span key={s.text} style={s.link ? { color: colors.orange, textDecoration: 'underline', textUnderlineOffset: 4 } : undefined}>
            {s.text}
          </span>
        ))}
      </p>
      <div className="absolute bottom-[16px] left-[16px] right-[16px] h-[88px] rounded-[16px] border-2 px-[14px] pt-[13px]" style={{ borderColor: '#f9cbbb', background: '#fff' }}>
        <p className="text-[13px] font-medium" style={{ color: colors.body }}>
          {assistant.input}
        </p>
        <div className="mt-[18px] flex items-center">
          <span className="flex h-[14px] items-center rounded-full px-[3px] text-[10px] leading-[10px] font-semibold text-white" style={{ background: colors.aiChip }}>
            AI
          </span>
          <span className="ml-[4px] text-[11px] font-medium" style={{ color: colors.body }}>
            {assistant.context}
          </span>
          <CircleHelp className="ml-[4px]" size={11} color={colors.body} />
          <span className="ml-auto -mr-[2px] flex h-[28px] items-center rounded-full px-[13px] text-[12px]" style={{ background: colors.orangeSoft, color: colors.orange }}>
            {assistant.send}
          </span>
        </div>
      </div>
    </div>
  )
}

/** "Ask your docs" interactive product mockup, rendered as UI over a placeholder art band. */
export function ProductDemo({ top, height }: { top: number; height: number }) {
  const f = geo.frame
  return (
    <section className="relative" style={{ height }}>
      <ImagePlaceholder label="orange brush-stroke art" className="absolute" style={{ left: geo.art.x, top: geo.art.y - top, width: geo.art.w, height: geo.art.h }} />
      <div
        className="absolute overflow-hidden rounded-[16px] border"
        style={{ left: f.x, top: f.y - top, width: f.w, height: f.h, background: colors.frame, borderColor: colors.border, boxShadow: shadows.frame }}
      >
        <div className="flex h-[44px] items-center gap-[8px] pl-[24px]">
          {colors.dots.map((d) => (
            <span key={d} className="h-[12px] w-[12px] rounded-full" style={{ background: d }} />
          ))}
        </div>
        <div className="absolute left-[7px] top-[43px] flex h-[595px] w-[1104px] overflow-hidden rounded-[12px] border bg-white" style={{ borderColor: colors.border }}>
          <div className="flex w-[784px] flex-col">
            <DocsTopBar />
            <DocsTabs />
            <div className="flex">
              <DocsSidebar />
              <DocsMain />
            </div>
          </div>
          <AssistantPanel />
        </div>
      </div>
      <div className="absolute left-0 right-0 flex justify-center" style={{ top: geo.tabs.y - top }}>
        <DemoTabs />
      </div>
      <div className="absolute left-0 right-0 flex justify-center" style={{ top: geo.cta.y - top }}>
        <PillButton className="h-[37px]" arrow>
          {assistant.cta}
        </PillButton>
      </div>
    </section>
  )
}
