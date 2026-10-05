import { Search, X } from 'lucide-react'
import { AppScreen, Button, HomeIndicator, IconButton, StatusBar, cn } from '../../../ui'
import { activeVertical, verticals, where } from '../data'
import { FieldCard } from '../components/FieldCard'
import { SuggestionRow } from '../components/SuggestionRow'
import { VerticalTabs } from '../components/VerticalTabs'
import { FONT, palette as c } from '../theme'

export function WhereScreen() {
  return (
    <AppScreen className={cn(FONT)} background={c.sheetBg}>
      <StatusBar paddingX={34} paddingTop={18} fontSize={16} />
      <VerticalTabs
        items={verticals}
        active={activeVertical}
        centers={[106, 193, 281]}
        iconSize={32}
        showNew={false}
        labelGap={3}
        underlineWidth={40}
        className="mt-[13px]"
      />
      <IconButton
        icon={X}
        size={38}
        iconSize={15}
        strokeWidth={2.6}
        className="absolute top-[70px] left-[341px] bg-white text-[#222] shadow-[0_2px_8px_rgba(0,0,0,0.08)]"
      />
      <div
        className="absolute top-[143px] left-[12px] h-[423px] w-[365px] overflow-hidden rounded-[24px] bg-white px-[23px] pt-[19px]"
        style={{ boxShadow: '0 6px 24px rgba(0,0,0,0.1)' }}
      >
        <h1 className="text-[22.5px] font-bold" style={{ color: c.text }}>
          {where.title}
        </h1>
        <div className="mt-[14px] flex h-[54px] items-center gap-[14px] rounded-[12px] border border-[#b0b0b0] px-[19px]">
          <Search size={15} strokeWidth={2.6} color={c.text} />
          <span className="text-[13.5px]" style={{ color: c.muted }}>
            {where.placeholder}
          </span>
        </div>
        <div className="mt-[17px] text-[11px] font-medium" style={{ color: c.text }}>
          {where.suggestedLabel}
        </div>
        <div className="mt-[11px] flex flex-col gap-[15px]">
          {where.suggestions.map((s) => (
            <SuggestionRow key={s.id} item={s} />
          ))}
        </div>
        <div className="absolute inset-x-0 bottom-0 h-[30px] bg-gradient-to-b from-white/0 to-white" />
      </div>
      <div className="absolute top-[583px] left-[15px] flex w-[357px] flex-col gap-[18px]">
        {where.fields.map((f) => (
          <FieldCard key={f.label} label={f.label} value={f.value} />
        ))}
      </div>
      <span className="absolute top-[763px] left-[23px] text-[14px] font-semibold underline underline-offset-2" style={{ color: c.text }}>
        {where.clear}
      </span>
      <Button
        leadingIcon={Search}
        iconSize={17}
        iconStrokeWidth={2.6}
        className="absolute top-[750px] left-[236px] h-[47px] w-[129px] gap-[8px] rounded-[12px] text-[14.5px] font-semibold text-white"
        style={{ background: c.brand }}
      >
        {where.search}
      </Button>
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
