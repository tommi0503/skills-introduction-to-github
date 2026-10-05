import { hero } from '../data'
import { theme } from '../theme'
import { PixelText } from '../components/PixelText'

const d = hero.demo
const label = 'text-[11px] uppercase leading-[13px]'

function Screw({ left, top }: { left: number; top: number }) {
  return <span className="absolute h-[14px] w-[14px] rounded-full border border-[#9c9893]" style={{ left, top }} />
}

/** Speaker dots in two staggered rows. */
function Grille() {
  return (
    <div className="absolute left-[1146px] top-[404px] w-[84px]">
      {[0, 1].map((row) => (
        <div key={row} className="flex gap-[8.5px]" style={{ marginLeft: row ? 6 : 0, marginTop: row ? 7 : 0 }}>
          {Array.from({ length: row ? 6 : 7 }, (_, i) => (
            <span key={i} className="h-[3px] w-[3px] rounded-full bg-[#55524e]" />
          ))}
        </div>
      ))}
    </div>
  )
}

/** Left: email unlock form on black. Right: hardware-style control panel with the Talk dial. */
export function DemoWidget() {
  return (
    <div className="absolute left-[170px] top-[375px] h-[470px] w-[1100px] rounded-[12px] shadow-[0_20px_60px_rgba(0,0,0,0.45)]">
      <div className="absolute left-0 top-0 h-full w-[550px] rounded-l-[12px]" style={{ background: theme.color.panelDark }}>
        <PixelText as="p" lines={[d.greeting]} size={26} lineHeight={34} className="absolute left-[26px] top-[18px]" style={{ color: 'rgba(242,241,236,0.82)' }} />
        <p className="absolute left-[26px] top-[312px] text-[18px] leading-[26px]" style={{ color: 'rgba(242,241,236,0.86)' }}>
          {d.prompt}
        </p>
        <div className="absolute left-[26px] top-[378px] flex h-[48px] w-[498px] items-center rounded-[6px] border border-[#2a2b2d] pl-[16px] pr-[4px]" style={{ background: '#0b0c0d' }}>
          <span className="text-[15px] text-white/35">{d.placeholder}</span>
          <span className="ml-auto flex h-[38px] w-[90px] items-center justify-center rounded-[5px] text-[14px]" style={{ background: theme.color.cream, color: theme.color.ink }}>
            {d.submit}
          </span>
        </div>
        <p className={`absolute left-[26px] top-[436px] text-[10.5px] leading-[14px] ${theme.font.mono}`} style={{ color: 'rgba(242,241,236,0.66)' }}>
          {d.note}
        </p>
      </div>
      <div className={`absolute left-[550px] top-0 h-full w-[550px] overflow-hidden rounded-r-[12px] ${theme.font.mono}`} style={{ background: theme.color.panelLight }}>
        <span className="absolute left-0 top-[234px] h-[2px] w-full" style={{ background: theme.color.panelLine }} />
        <span className="absolute left-[274px] top-[236px] h-[234px] w-[2px]" style={{ background: theme.color.panelLine }} />
        <span className="absolute left-[24px] top-[212px] text-[9px] leading-[9px]" style={{ color: 'rgba(75,75,72,0.42)' }}>
          {d.brand}
        </span>
        {d.channels.map((c, i) => (
          <span key={c} className={`absolute top-[433px] flex items-center gap-[7px] ${label}`} style={{ left: 25 + i * 275, color: 'rgba(59,58,56,0.9)' }}>
            <span className="h-[7px] w-[7px] rounded-full border border-[#6a6762]" />
            {c}
          </span>
        ))}
      </div>
      <Screw left={562} top={12} />
      <Screw left={1074} top={11} />
      <div className="absolute" style={{ left: 717, top: 127 }}>
        <div className="h-[216px] w-[216px] rounded-full bg-[#bdb8b3] shadow-[inset_0_2px_6px_rgba(0,0,0,0.25)]" />
        <div className="absolute left-[10px] top-[10px] flex h-[196px] w-[196px] flex-col items-center justify-center rounded-full bg-[#ece9e5] shadow-[0_6px_14px_rgba(0,0,0,0.25)]">
          <span className="h-[3px] w-[26px] rounded-full" style={{ background: '#6b3418' }} />
          <span className={`mt-[14px] ${label} ${theme.font.mono}`} style={{ color: 'rgba(59,58,56,0.9)' }}>
            {d.talk}
          </span>
        </div>
      </div>
      <div className="absolute" style={{ left: -170, top: -375 }}>
        <Grille />
      </div>
    </div>
  )
}
