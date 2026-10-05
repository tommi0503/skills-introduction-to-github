import { AppHeader } from '../components/AppHeader'
import { BottomNav } from '../components/BottomNav'
import { SectionIntro } from '../components/SectionIntro'
import { ServiceList } from '../components/ServiceList'
import { monthlyIntro, services } from '../data'

/** Monthly service list, scrolled to the top. */
export function ServiceListScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white">
      <AppHeader time="12:39" />
      <SectionIntro title={monthlyIntro.title} subtitle={monthlyIntro.subtitle} className="absolute top-[128px]" />
      <ServiceList
        className="absolute top-[210.6px]"
        items={[services.allInOne, services.shirtsDry, services.dryOnly, services.laundryDry]}
      />
      <BottomNav />
    </div>
  )
}
