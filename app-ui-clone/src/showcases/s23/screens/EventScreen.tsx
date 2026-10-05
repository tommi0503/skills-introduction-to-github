import { AppHeader } from '../components/AppHeader'
import { BottomNav } from '../components/BottomNav'
import { EventBanner } from '../components/EventBanner'
import { ScrollTopButton } from '../components/ScrollTopButton'
import { ServiceList } from '../components/ServiceList'
import { event, services } from '../data'

/** Service list scrolled down to the friend-invite event banner. */
export function EventScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white">
      <AppHeader time="12:39" />
      <ServiceList
        className="absolute top-[108.9px]"
        items={[services.laundryDry, services.laundryOnly, services.beddingOnly]}
      />
      <EventBanner {...event} className="absolute top-[647.2px]" />
      <ScrollTopButton className="top-[649px] left-[312px]" />
      <BottomNav />
    </div>
  )
}
