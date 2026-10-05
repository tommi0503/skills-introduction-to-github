import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BrandMark } from '../components/BrandMark'
import { Chrome } from '../components/Chrome'
import { PillButton } from '../components/PillButton'
import { welcome } from '../data'
import { theme } from '../theme'

export function WelcomeScreen() {
  return (
    <AppScreen>
      <ImagePlaceholder tone={theme.heroDark} label="app preview illustration" className="absolute inset-x-0 top-0 h-[382px]" />
      <Chrome color="#fff" chipClassName="bg-[#6b6670]/95!" />
      <div className="absolute inset-x-0 top-[382px] px-[18px]">
        <div className="mt-[34px] flex items-center gap-[8px]">
          <BrandMark size={28} />
          <span className="text-[25px] leading-none font-semibold tracking-[-0.3px] text-[#111]">{welcome.brand}</span>
        </div>
        <p className="mt-[21px] text-[15.3px] leading-[20px] font-medium text-[#111]">{welcome.headline}</p>
        <p className="mt-[4px] text-[13.7px] leading-[19.5px] text-[#222]">{welcome.body}</p>
        <div className="mt-[48px] mr-[5px] flex flex-col gap-[13px]">
          {welcome.options.map((o) => (
            <PillButton
              key={o.key}
              variant={o.variant}
              className="h-[47px] text-[15.5px] font-normal"
              leading={o.brand && <BrandMark size={18} tone={o.brand === 'apple' ? '#d9d9de' : undefined} label={`${o.brand} logo`} />}
            >
              {o.label}
            </PillButton>
          ))}
        </div>
      </div>
    </AppScreen>
  )
}
