import { AppScreen, ImagePlaceholder } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { theme } from '../theme'

export function WelcomeScreen() {
  return (
    <AppScreen background={theme.welcomeBg}>
      <PhoneStatus color="#fff" />
      {/* blurred blue arc glow */}
      <ImagePlaceholder
        tone={theme.arcTone}
        label="glow arc"
        className="absolute rounded-full"
        style={{
          left: -65,
          top: 150,
          width: 520,
          height: 500,
          WebkitMaskImage: 'radial-gradient(ellipse 230px 130px at 260px 270px, transparent 99%, #000 100%)',
          maskImage: 'radial-gradient(ellipse 230px 130px at 260px 270px, transparent 99%, #000 100%)',
          clipPath: 'inset(0 0 290px 0)',
        }}
      />
      <ImagePlaceholder tone="#e9e9e9" label="Beside logo" className="absolute top-[420px] left-[168px] h-[48px] w-[54px] rounded-[6px]" />
      <div className="absolute inset-x-0 top-[511px] flex flex-col items-center text-center text-white">
        <h1 className="text-[23px] leading-[30px] font-bold">Welcome to Beside</h1>
        <p className="mt-[14px] text-[15.5px] leading-[22px] text-[#d9d9d9]">
          Starting today, your AI phone assistant
          <br />
          saves you 2 hours daily.
        </p>
      </div>
      <button className="absolute top-[637px] left-[44px] flex h-[47px] w-[302px] items-center justify-center rounded-full bg-white text-[15px] font-semibold text-[#111]">
        Get Started
      </button>
      <p className="absolute inset-x-0 top-[711px] text-center text-[15px] text-white">
        Already have an account? <span className="font-semibold">Log in</span>
      </p>
      <p className="absolute inset-x-0 top-[760px] text-center text-[12.5px] leading-[17px] text-[#c4c4c4]">
        By tapping Get Started, I agree with the <span className="font-medium text-white">Terms of</span>
        <br />
        <span className="font-medium text-white">Service</span> and <span className="font-medium text-white">Privacy Policy</span>.
      </p>
    </AppScreen>
  )
}
