import { AppScreen } from '../../../ui'
import { BrandWheel } from '../components/BrandWheel'
import { StatusRow } from '../components/StatusRow'
import { onboarding as d } from '../data'
import { fonts, zip } from '../theme'

export function Onboarding() {
  return (
    <AppScreen className={fonts.body} style={{ color: zip.ink }}>
      <StatusRow />
      <h1 className="absolute inset-x-0 top-[111px] text-center text-[26px] leading-[30px] font-medium">
        {d.title.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </h1>
      <div className="absolute inset-x-0 top-[229px] text-center text-[16.5px] leading-[24px] text-[#6d6d72]">
        <div>{d.merchant}</div>
        <div>{d.price}</div>
      </div>
      <BrandWheel tiles={d.wheel} cx={196} cy={335} radius={490} stepDeg={15.5} size={104} />
      <div className="absolute inset-x-0 top-[408px] text-center text-[14.5px] font-medium">{d.installmentsLabel}</div>
      <div className="absolute inset-x-0 top-[438px] text-center text-[28px] font-semibold">{d.installment}</div>

      <button
        className="absolute top-[605px] left-[24px] h-[48px] w-[341px] rounded-[7px] text-[17px] font-medium text-white"
        style={{ background: zip.purple }}
      >
        {d.primary}
      </button>
      <button
        className="absolute top-[663px] left-[24px] h-[49px] w-[341px] rounded-[7px] border text-[17px] font-medium"
        style={{ borderColor: zip.border, color: zip.purple }}
      >
        {d.secondary}
      </button>
      <div className="absolute inset-x-0 top-[728px] text-center text-[14px] leading-[18.3px] text-[#707070]">
        {d.legal.map((l) => (
          <div key={l}>{l}</div>
        ))}
        <div className="underline" style={{ color: zip.purple }}>
          {d.legalLink}
        </div>
      </div>
    </AppScreen>
  )
}
