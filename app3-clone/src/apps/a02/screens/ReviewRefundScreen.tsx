import { ChevronLeft, FileText, PenLine } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { Card } from '../components/Card'
import { DeviceChrome } from '../components/DeviceChrome'
import { MetricRow } from '../components/MetricRow'
import { RiskPill } from '../components/RiskPill'
import { SquareButton } from '../components/SquareButton'
import { actions, metrics, refund } from '../data'
import { rf } from '../theme'

function ReasonCard() {
  const { attachment, source } = refund
  return (
    <Card className="absolute top-[357px] right-[18px] left-[18px]">
      <div className="px-[15px] pt-[16px] pb-[14px]">
        <p className="text-[15px] font-medium tracking-[-0.5px]">{refund.reason}</p>
        <p className="mt-[6px] pr-[20px] text-[14.5px] leading-[22px] tracking-[0.1px]" style={{ color: rf.muted }}>
          {refund.policy}
        </p>
        <div className="mt-[14px] flex items-center">
          <ImagePlaceholder className="h-[42px] w-[42px] rounded-[8px]" label="evidence thumbnail" />
          <div className="ml-[12px] flex-1">
            <p className="text-[14.5px] tracking-[-0.4px]">{attachment.name}</p>
            <p className="mt-[1px] text-[10.5px] tracking-[-0.3px]" style={{ color: rf.muted }}>
              {attachment.caption}
            </p>
          </div>
          <span className="flex h-[36px] w-[71px] items-center justify-center rounded-[10px] bg-[#f1f1f0] text-[12px] text-[#666]">
            {attachment.action}
          </span>
        </div>
      </div>
      <div className="flex h-[48px] items-center px-[16px] text-[12.5px] tracking-[-0.4px]">
        <FileText size={16} strokeWidth={1.5} className="text-[#555]" />
        <span className="ml-[5px] flex-1 font-medium">{source.label}</span>
        <span style={{ color: rf.muted }}>{source.value}</span>
      </div>
    </Card>
  )
}

function ActionBar() {
  return (
    <div className="absolute inset-x-0 top-[732px] bottom-0 border-t border-[#efeeeb] bg-white px-[18px] pt-[18px]">
      <div className="flex h-[57px] gap-[8px]">
        <SquareButton size={57} radius={16}>
          <PenLine size={19} strokeWidth={1.5} />
        </SquareButton>
        <span
          className="flex w-[110px] items-center justify-center rounded-[16px] border border-[#ecebe8] text-[14.5px] font-semibold"
          style={{ color: rf.deny }}
        >
          {actions.deny}
        </span>
        <span className="flex flex-1 items-center justify-center rounded-[16px] bg-[#111] text-[14px] tracking-[-0.2px] text-white shadow-[0_6px_14px_rgba(0,0,0,0.18)]">
          {actions.approve}
        </span>
      </div>
    </div>
  )
}

/** Agent-proposed refund awaiting human approval. */
export function ReviewRefundScreen() {
  return (
    <AppScreen background={rf.bg} className="font-jakarta" style={{ color: rf.text }}>
      <DeviceChrome />
      <SquareButton className="absolute top-[63px] left-[18px]">
        <ChevronLeft size={20} strokeWidth={1.6} />
      </SquareButton>
      <h1 className="absolute top-[134px] left-[18px] text-[26px] font-bold tracking-[-0.8px]">{refund.title}</h1>
      <p className="absolute top-[178px] left-[18px] text-[16px] tracking-[0.3px]" style={{ color: '#7a7a77' }}>
        {refund.ticket}
      </p>
      <p className="absolute top-[218px] left-[17px] text-[44px] leading-none font-bold tracking-[0.4px]">{refund.amount}</p>
      <div className="absolute top-[230px] right-[19px]">
        <RiskPill label={refund.risk} />
      </div>
      <p className="absolute top-[279px] left-[18px] text-[14.5px] tracking-[-0.6px]" style={{ color: rf.muted }}>
        {refund.recipient}
      </p>
      <p className="absolute top-[325px] left-[18px] text-[12.5px] tracking-[-0.2px] uppercase" style={{ color: rf.muted }}>
        {refund.reasonHeading}
      </p>
      <ReasonCard />
      <Card className="absolute top-[580px] right-[18px] left-[18px]">
        {metrics.map((m) => (
          <MetricRow key={m.key} metric={m} />
        ))}
      </Card>
      <ActionBar />
    </AppScreen>
  )
}
