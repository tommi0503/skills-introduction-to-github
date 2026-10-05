import { ArrowRight, CircleX, Search } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { Card } from '../components/Card'
import { ResultRow } from '../components/ResultRow'
import { StatusRow } from '../components/StatusRow'
import { results as d } from '../data'
import { fonts, zip } from '../theme'

function SearchHeader() {
  return (
    <div className="absolute inset-x-0 top-0 h-[104px] border-b border-[#e3e3e3] bg-white">
      <div
        className="absolute top-[62px] left-[13px] flex h-[35px] w-[302px] items-center rounded-[10px] pr-[10px] pl-[12px]"
        style={{ background: zip.field }}
      >
        <Search size={17} strokeWidth={2} />
        <span className="ml-[11px] flex-1 text-[16px]">{d.query}</span>
        <CircleX size={17} strokeWidth={2} fill="#8d8d92" className="text-[#ebeae8]" />
      </div>
      <span className="absolute top-[69px] left-[327px] text-[16px] font-medium" style={{ color: zip.purpleText }}>
        {d.cancel}
      </span>
    </div>
  )
}

export function SearchResults() {
  return (
    <AppScreen className={fonts.body} background={zip.page} style={{ color: zip.ink }}>
      <SearchHeader />
      <StatusRow />
      <Card className="absolute top-[118px] left-[16px] w-[356px] overflow-hidden">
        {d.items.map((it) => (
          <ResultRow key={it.key} item={it} />
        ))}
        <div className="h-[41px] pt-[10px] pl-[15px] text-[13px]" style={{ color: zip.purpleText }}>
          {d.showFewer}
        </div>
      </Card>

      <Card className="absolute top-[500px] left-[16px] h-[121px] w-[356px]">
        <div className="absolute top-[17px] left-[15px] flex items-center gap-[10px]">
          <span className="rounded-[5px] px-[8px] text-[14px] leading-[23px]" style={{ background: zip.adTag }}>
            Ad
          </span>
          <span className="text-[15px] font-semibold">{d.featuredTitle}</span>
        </div>
        <div className="absolute top-[52px] left-[16px] flex gap-[18px]">
          {d.featured.map((k) => (
            <ImagePlaceholder key={k} label={k} className="h-[51px] w-[51px] rounded-full" />
          ))}
        </div>
      </Card>

      <Card className="absolute top-[637px] left-[16px] flex h-[71px] w-[356px] items-center pr-[17px] pl-[23px]">
        <ImagePlaceholder label="Google" className="h-[25px] w-[25px] rounded-full" />
        <div className="ml-[24px] flex-1 text-[15px] leading-[20px]">
          <div className="font-semibold">{d.google.title}</div>
          <div>{d.google.subtitle}</div>
        </div>
        <Search size={21} strokeWidth={1.6} />
      </Card>

      <Card className="absolute top-[724px] left-[16px] flex h-[83px] w-[356px] items-center pr-[17px] pl-[16px]">
        <ImagePlaceholder label="virtual card" className="h-[40px] w-[60px] rounded-[3px]" />
        <div className="ml-[15px] flex-1">
          <div className="text-[15px] leading-[19px] font-semibold">{d.virtualCard.title}</div>
          <div className="mt-[2px] text-[13px] leading-[16px] text-[#7a7a7f]">
            {d.virtualCard.body.map((l) => (
              <div key={l}>{l}</div>
            ))}
          </div>
        </div>
        <ArrowRight size={21} strokeWidth={1.6} />
      </Card>
    </AppScreen>
  )
}
