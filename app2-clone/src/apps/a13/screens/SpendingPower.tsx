import { ArrowLeft, ArrowRight, Zap } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { ArrowLink } from '../components/ArrowLink'
import { Card } from '../components/Card'
import { StatusRow } from '../components/StatusRow'
import { spending as d, type CardRow } from '../data'
import { fonts, zip } from '../theme'

function EstimateCard() {
  return (
    <Card className="absolute top-[110px] left-[23px] h-[132px] w-[342px] px-[15px] pt-[12px]">
      <div className="text-[14.5px] leading-[18px]">{d.estimateLabel}</div>
      <div className={cn(fonts.display, 'mt-[5px] flex items-baseline font-bold')}>
        <span className="mr-[3px] text-[27px] leading-none">{d.currency}</span>
        <span className="text-[39px] leading-[38px] tracking-[4.5px]">{d.amount}</span>
      </div>
      <div className="mt-[16px] border-t border-[#e6e6e6]" />
      <div className="mt-[9px] flex justify-between text-[14px]">
        <span>{d.payLabel}</span>
        <span className="font-semibold">{d.payValue}</span>
      </div>
    </Card>
  )
}

function CardRowItem({ row, first }: { row: CardRow; first: boolean }) {
  return (
    <div className={cn('flex h-[63px] items-center pr-[18px] pl-[13px]', first && 'border-b border-[#eeeeee]')}>
      <ImagePlaceholder label={row.title} className="h-[26px] w-[34px] rounded-[4px]" />
      <div className={cn('flex-1 text-[14.5px] leading-[19px]', first ? 'ml-[19px]' : 'ml-[22px]')}>
        <div>
          {row.title}
          {row.sup && <sup className="text-[8px]">{row.sup}</sup>}
        </div>
        <div className="text-[#55555a]">{row.amount}</div>
      </div>
      {row.chevron && <ArrowRight size={22} strokeWidth={1.5} />}
    </div>
  )
}

function UpsellBanner() {
  const u = d.upsell
  return (
    <div
      className="absolute top-[400px] left-[23px] flex h-[77px] w-[342px] items-center gap-[12px] rounded-[12px] pr-[20px] pl-[16px]"
      style={{ background: zip.lavenderSoft }}
    >
      <Zap size={30} strokeWidth={1.3} fill="#f5c932" className="shrink-0 text-[#2a2140]" />
      <p className="max-w-[252px] text-[14.5px] leading-[17.5px]">
        {u.lead} <b className="font-semibold">{u.amount}</b>
        <sup className="text-[7px]">{u.sup}</sup>
        {u.mid}
        <span className="underline" style={{ color: zip.purpleText }}>
          {u.link}
        </span>
        .
      </p>
    </div>
  )
}

function LevelUpCard() {
  const l = d.levelUp
  return (
    <Card className="absolute top-[495px] left-[23px] h-[218px] w-[342px] px-[15px] pt-[15px]">
      <div className={cn(fonts.display, 'text-[13px] leading-[16px] font-extrabold tracking-[-0.2px]')}>{l.title}</div>
      <p className="mt-[6px] pr-[16px] text-[17.5px] leading-[22px] text-[#2a2235]">
        {l.body}{' '}
        <span className="underline" style={{ color: zip.purpleText }}>
          {l.link}
        </span>
      </p>
      <div className="mt-[14px] flex gap-[11px]">
        {l.steps.map((s) => (
          <span
            key={s}
            className={cn(
              fonts.display,
              'flex h-[54px] w-[54px] items-center justify-center rounded-full border-[1.5px] border-dashed border-[#c8c8cc] text-[20px] font-bold text-[#c2c2c6]',
            )}
          >
            {s}
          </span>
        ))}
      </div>
      <ArrowLink label={l.cta} className="mt-[12px] text-[15px]" iconSize={14} />
    </Card>
  )
}

export function SpendingPower() {
  return (
    <AppScreen className={fonts.body} background={zip.page} style={{ color: zip.ink }}>
      <StatusRow />
      <ArrowLeft size={24} strokeWidth={1.8} className="absolute top-[65px] left-[10px]" />
      <EstimateCard />
      <Card className="absolute top-[258px] left-[23px] w-[342px]">
        {d.cards.map((r, i) => (
          <CardRowItem key={r.key} row={r} first={i === 0} />
        ))}
      </Card>
      <UpsellBanner />
      <LevelUpCard />
      <Card className="absolute top-[733px] left-[23px] h-[140px] w-[342px] px-[15px] pt-[16px]">
        <div className={cn(fonts.display, 'text-[13px] leading-[16px] font-extrabold')}>{d.about.title}</div>
        <p className="mt-[7px] pr-[26px] text-[13px] leading-[16.5px] text-[#2a2235]">{d.about.body}</p>
      </Card>
    </AppScreen>
  )
}
