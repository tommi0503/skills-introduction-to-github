import { ArrowUp, ChevronDown, ChevronRight } from 'lucide-react'
import { PixelText } from '../components/PixelText'
import { agents as s, type ChatItem } from '../data'
import { theme } from '../theme'

const PANEL = { left: 802, top: 2625, w: 469, h: 774 }
const STEPS_TOP = 3152
const ROW = 46.2

function Steps() {
  return (
    <div className="absolute left-[169px] w-[469px]" style={{ top: STEPS_TOP }}>
      {s.steps.map((label, i) => {
        const active = i === s.activeStep
        return (
          <div key={label} className="relative flex items-center border-t" style={{ height: ROW, borderColor: theme.color.rule }}>
            {active && <span className="absolute -top-px left-0 h-px w-[21px] bg-white/50" />}
            <span className={`w-[34px] text-[9px] ${theme.font.mono}`} style={{ color: active ? '#fff' : 'rgba(232,237,239,0.45)' }}>
              {String(i + 1).padStart(2, '0')}
            </span>
            <span className="text-[14.5px]" style={{ color: active ? '#fff' : 'rgba(232,237,239,0.6)' }}>
              {label}
            </span>
          </div>
        )
      })}
      <div className="border-t" style={{ borderColor: theme.color.rule }} />
    </div>
  )
}

function Message({ item }: { item: ChatItem }) {
  const top = item.top - PANEL.top
  if (item.from === 'user') {
    return (
      <div
        className="absolute right-[25px] rounded-[9px] px-[13px] py-[8px] text-[14px] leading-[22px] shadow-[0_2px_8px_rgba(0,0,0,0.4)]"
        style={{ top, width: item.width, background: theme.color.cream, color: theme.color.ink }}
      >
        {item.text.map((t) => (
          <span key={t} className="block whitespace-nowrap">
            {t}
          </span>
        ))}
      </div>
    )
  }
  const Chevron = item.open ? ChevronDown : ChevronRight
  return (
    <div className="absolute left-[26px] w-[400px]" style={{ top }}>
      <div className={`border-l border-white/20 pl-[9px] text-[10.5px] leading-[18px] ${theme.font.mono}`}>
        <span className="flex items-center gap-[4px] text-white/55">
          {item.tool}
          <Chevron size={10} />
        </span>
        {item.detail && <span className="block text-white/85">{item.detail}</span>}
      </div>
      <p className="mt-[9px] text-[14px] leading-[22.5px]" style={{ color: 'rgba(242,241,236,0.92)' }}>
        {item.text.map((t) => (
          <span key={t} className="block whitespace-nowrap">
            {t}
          </span>
        ))}
      </p>
    </div>
  )
}

function ChatPanel() {
  const c = s.chat
  return (
    <div
      className="absolute overflow-hidden rounded-[12px] border border-white/10"
      style={{ left: PANEL.left, top: PANEL.top, width: PANEL.w, height: PANEL.h, background: `linear-gradient(180deg, #19191b 0%, ${theme.color.chatBg} 30%, #08090a 100%)` }}
    >
      <PixelText as="p" lines={[c.status]} size={26} lineHeight={34} className="absolute left-[26px] top-[18px]" style={{ color: 'rgba(242,241,236,0.82)' }} />
      <span className={`absolute right-[25px] top-[34px] text-[10.5px] uppercase ${theme.font.mono}`}>
        <span className="text-white/50">{c.moodLabel}</span> <span className="text-white/85">{c.mood}</span>
      </span>
      <span className="absolute left-[26px] top-[61px] h-px w-[417px] bg-white/10" />
      {c.items.map((it) => (
        <Message key={it.text[0]} item={it} />
      ))}
      <div className="absolute left-[26px] top-[646px] flex h-[44px] w-[417px] items-center rounded-[8px] border border-white/15 px-[19px] text-[14px] text-white/45" style={{ background: '#0b0c0d' }}>
        {c.input}
        <ArrowUp size={14} className="ml-auto text-white/60" />
      </div>
      <div className={`absolute bottom-0 left-0 h-[64px] w-full ${theme.font.mono}`} style={{ background: theme.color.chatFoot }}>
        <span className="absolute left-[17px] top-[26px] h-[12px] w-[12px] rounded-full bg-[#3c3c3e]" />
        <span className="absolute left-[44px] top-[25px] text-[9px] text-white/35">{c.brand}</span>
        <span className="absolute left-[268px] top-[28px] h-[7px] w-[7px] rounded-full" style={{ background: theme.color.orange }} />
        <span className="absolute left-[284px] top-[23px] text-[10.5px] uppercase text-white/85">{c.channel}</span>
        <span className="absolute left-[437px] top-[24px] h-[15px] w-[15px] rounded-full bg-[#505052]" />
      </div>
    </div>
  )
}

/** "Agents that keep getting better." — copy + numbered steps beside a live chat transcript. */
export function Agents() {
  return (
    <section className={theme.font.sans}>
      <PixelText lines={s.title} size={52.63} lineHeight={57} className="absolute left-[169px] top-[2624px]" style={{ color: theme.color.textHeading }} />
      <p className="absolute left-[169px] top-[2768px] text-[17px] leading-[25px]" style={{ color: theme.color.textDim }}>
        {s.body.map((t) => (
          <span key={t} className="block">
            {t}
          </span>
        ))}
      </p>
      <Steps />
      <ChatPanel />
    </section>
  )
}
