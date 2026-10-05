import { ChevronDown, Lock, RefreshCcw, Share, Undo2, X } from 'lucide-react'
import { cn, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { PieProgress } from '../components/PieProgress'
import { RangeSlider } from '../components/RangeSlider'
import { SheetScreen } from '../components/SheetScreen'
import { payment as d } from '../data'

function BrowserChrome() {
  return (
    <div className="absolute inset-x-0 top-[50px] flex items-center px-[17px] text-[#111]">
      <ChevronDown size={20} strokeWidth={2.2} />
      <div className="ml-[23px] flex h-[34px] w-[310px] items-center rounded-full bg-[#ececee] pr-[8px] pl-[50px] text-[16px]">
        <Lock size={12} strokeWidth={2.6} className="mr-[4px]" />
        <span className="flex-1">{d.url}</span>
        <Share size={19} strokeWidth={1.8} />
        <RefreshCcw size={18} strokeWidth={1.8} className="ml-[13px]" />
      </div>
    </div>
  )
}

function Card({ className, children }: { className?: string; children: React.ReactNode }) {
  return <div className={cn('absolute right-[21px] left-[21px] rounded-[16px] bg-white', className)}>{children}</div>
}

export function PaymentCalculatorScreen() {
  return (
    <SheetScreen
      className="font-inter"
      background="#ffffff"
      dim={0.6}
      sheetTop={93}
      sheetClassName="rounded-t-[22px] bg-[#f3f2f7]"
      backdrop={<BrowserChrome />}
      status={{ color: '#111' }}
    >
      <CircleButton icon={Undo2} className="absolute top-[10px] left-[11px] bg-white text-[#111]" />
      <CircleButton icon={X} className="absolute top-[10px] right-[11px] bg-white text-[#111]" />
      <h1 className="absolute inset-x-0 top-[75px] text-center text-[31.5px] leading-[38px] font-bold tracking-[-0.3px] text-[#111]">
        {d.title}
      </h1>
      <p className="absolute inset-x-0 top-[124px] text-center text-[16px] leading-[24px] text-[#222]">
        {d.subtitle.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </p>

      <Card className="top-[207px] h-[380px]">
        <p className="absolute top-[13px] left-[17px] text-[15.5px] font-semibold text-[#111]">{d.question}</p>
        <p className="absolute top-[45px] left-[17px] text-[21px] text-[#111]">{d.amount}</p>
        <RangeSlider value={d.sliderValue} width={306} className="absolute top-[112px] left-[17px]" />
        <p className="absolute top-[168px] left-[17px] text-[15.5px] font-semibold text-[#111]">{d.planTitle}</p>
        <span className="absolute top-[174px] right-[17px] rounded-[4px] bg-[#bdeef7] px-[8px] py-[3px] text-[12.5px] text-[#14363c]">
          {d.planBadge}
        </span>
        <div className="absolute top-[212px] right-[17px] left-[17px] grid grid-cols-4 gap-[1px]">
          {d.steps.map((s, i) => (
            <div
              key={s.when}
              className={cn('flex h-[84px] flex-col items-center rounded-[10px] pt-[8px]', i === d.activeStep && 'bg-[#f1f1f4]')}
            >
              <PieProgress progress={s.progress} />
              <span className="mt-[7px] text-[12.5px] leading-[15px] text-[#222]">{s.amount}</span>
              <span className={cn('text-[10px] leading-[16px]', i === d.activeStep ? 'text-[#222]' : 'text-[#888]')}>
                {s.when}
              </span>
            </div>
          ))}
        </div>
        <div className="absolute top-[322px] left-[15px] flex items-center gap-[13px]">
          <span className="flex h-[42px] w-[42px] items-center justify-center rounded-full bg-[#f2f2f5]">
            <ImagePlaceholder className="h-[20px] w-[20px] rounded-[4px]" label="no interest icon" />
          </span>
          <span className="text-[15.5px] text-[#111]">{d.note}</span>
        </div>
      </Card>

      <Card className="top-[604px] h-[104px]">
        <p className="absolute top-[13px] left-[17px] text-[15.5px] leading-[26px] text-[#222]">
          {d.feedback.map((l) => (
            <span key={l} className="block">
              {l}
            </span>
          ))}
        </p>
        {[234, 292].map((x, i) => (
          <span
            key={x}
            className="absolute top-[33px] flex h-[40px] w-[40px] items-center justify-center rounded-full bg-[#f2f2f2]"
            style={{ left: x }}
          >
            <ImagePlaceholder className="h-[22px] w-[22px] rounded-full" label={i === 0 ? 'thumbs up' : 'thumbs down'} />
          </span>
        ))}
      </Card>
    </SheetScreen>
  )
}
