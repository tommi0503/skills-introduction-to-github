import { CalendarCheck2, Smile } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { AppHeader } from '../components/AppHeader'
import { AppointmentCard } from '../components/AppointmentCard'
import { BarberPhone } from '../components/BarberPhone'
import { Headline } from '../components/Headline'
import { NavDock } from '../components/NavDock'
import { copy, navItems, nextAppointment } from '../data'
import { theme } from '../theme'

/** Home: greeting, salon carousel, next appointment and floating dock. */
export function HomeScreen() {
  return (
    <BarberPhone background={theme.screenHome}>
      <AppHeader left={<ImagePlaceholder label="User avatar" className="h-[43px] w-[43px] rounded-full" />} />
      <div className="absolute left-[21px] top-[111px] flex items-center gap-[7px] text-[13.8px] font-medium">
        {copy.greeting}
        <Smile size={16} strokeWidth={1.5} />
      </div>
      <Headline lines={copy.homeTitle} className="absolute left-[21px] top-[139px] text-[28.8px] font-[460] leading-[36px] tracking-[-0.2px]" />

      {/* salon carousel: neighbours peek at the edges */}
      <ImagePlaceholder label="Previous salon photo" className="absolute left-[-6px] top-[238px] h-[255px] w-[19px] rounded-[10px]" />
      <ImagePlaceholder label="Barber salon interior photo" className="absolute left-[21px] top-[226px] h-[278px] w-[333px] rounded-[19px]" />
      <ImagePlaceholder label="Next salon photo" className="absolute left-[365px] top-[238px] h-[255px] w-[19px] rounded-[10px]" />

      <div className="absolute left-[21px] top-[514px] w-[336px]">
        <AppointmentCard appointment={nextAppointment} />
      </div>

      <button
        type="button"
        className="absolute left-[21px] top-[681px] flex h-[46px] w-[336px] items-center justify-center gap-[8px] rounded-full bg-black text-[14px] font-medium text-white"
      >
        {copy.bookCta}
        <CalendarCheck2 size={16} strokeWidth={1.8} />
      </button>

      <div className="absolute left-[21px] top-[737px] text-[17px] font-medium text-[#a9a8a4]">{copy.sectionPeek}</div>
      <div className="absolute left-[21px] top-[766px] h-[80px] w-[336px] rounded-[20px] bg-white/30" />
      <div className="absolute left-[64px] top-[741px]">
        <NavDock items={navItems} activeKey="home" />
      </div>
    </BarberPhone>
  )
}
