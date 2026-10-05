import { RefreshCcw, Star, X } from 'lucide-react'
import { AppScreen, Button, HomeIndicator, ImagePlaceholder, StatusBar, cn } from '../../../ui'
import { review } from '../data'
import { Divider } from '../components/Divider'
import { RadioDot } from '../components/RadioDot'
import { ReviewSectionRow } from '../components/ReviewSectionRow'
import { StepProgress } from '../components/StepProgress'
import { FONT, palette as c } from '../theme'

export function ReviewScreen() {
  return (
    <AppScreen className={cn(FONT)}>
      <StatusBar paddingX={34} paddingTop={18} fontSize={16} />
      <X size={20} strokeWidth={2} color={c.text} className="absolute top-[78px] left-[343px]" />
      <h1 className="mt-[72px] px-[23px] text-[23.5px] font-semibold tracking-[-0.4px]" style={{ color: c.text }}>
        {review.title}
      </h1>
      <div className="mt-[22px] mr-[25px] ml-[22px] rounded-[14px] border border-[#e4e4e4] px-[16px] pt-[21px] pb-[16px]">
        <div className="flex gap-[15px]">
          <ImagePlaceholder className="rounded-[8px]" style={{ width: 80, height: 80 }} label="room photo" />
          <div style={{ color: c.text }}>
            <div className="-mt-[4px] w-[190px] text-[17px] leading-[24px] font-medium tracking-[-0.2px]">{review.stay.title}</div>
            <div className="mt-[1px] flex items-center gap-[4px] text-[11.5px] font-medium">
              <Star size={10} fill={c.text} strokeWidth={0} />
              {review.stay.rating}
              <RefreshCcw size={10} strokeWidth={2.4} className="ml-[6px]" />
              {review.stay.badge}
            </div>
          </div>
        </div>
        {review.sections.map((s) => (
          <div key={s.title}>
            <Divider className="my-[14.5px]" />
            <ReviewSectionRow section={s} />
          </div>
        ))}
      </div>
      <h2 className="mt-[21px] px-[23px] text-[15.5px] font-semibold" style={{ color: c.text }}>
        {review.payTitle}
      </h2>
      <div className="mt-[11px] mr-[25px] ml-[22px] h-[200px] rounded-[14px] border border-[#e4e4e4] px-[16px]">
        {review.payOptions.map((o, i) => (
          <div key={o.key}>
            {i > 0 && <Divider />}
            <div className={cn('flex justify-between py-[16px]', o.sub ? 'items-start' : 'items-center')}>
              <div style={{ color: c.text }}>
                <div className="text-[13px] leading-[20px] font-medium">{o.title}</div>
                {o.sub && (
                  <div className="mt-[2px] w-[280px] text-[13.5px] leading-[18px]" style={{ color: c.muted }}>
                    {o.sub} <span className="font-medium underline underline-offset-2">{o.link}</span>
                  </div>
                )}
              </div>
              <RadioDot checked={o.key === review.payChoice} color="#222" />
            </div>
          </div>
        ))}
      </div>
      <div className="absolute inset-x-0 top-[730px] bottom-0 bg-white">
        <StepProgress steps={review.steps} done={review.step} />
        <Button className="absolute top-[20px] left-[22px] h-[47px] w-[343px] rounded-[10px] bg-[#222] text-[15px] font-semibold text-white">
          {review.cta}
        </Button>
      </div>
      <HomeIndicator width={138} bottom={6} />
    </AppScreen>
  )
}
