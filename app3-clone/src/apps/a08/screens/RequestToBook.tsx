import { ChevronLeft } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { ListingSummary } from '../components/ListingSummary'
import { PayOptionRow } from '../components/PayOptionRow'
import { SectionBand } from '../components/SectionBand'
import { TripFieldRow } from '../components/TripFieldRow'
import { booking } from '../data'
import { airbnb } from '../theme'

export function RequestToBook() {
  return (
    <AppScreen className="font-figtree" background="#fff">
      <StatusBar color={airbnb.ink} paddingTop={15} timeClassName="font-bold" />
      <header className="relative flex h-[46px] items-center justify-center" style={{ color: airbnb.ink }}>
        <ChevronLeft size={22} strokeWidth={1.8} className="absolute left-[22px]" />
        <h1 className="text-[15.5px] font-bold">{booking.title}</h1>
      </header>
      <div className="h-px" style={{ background: airbnb.hairline }} />
      <ListingSummary listing={booking.listing} />
      <SectionBand color={airbnb.band} />
      <section className="px-[26px] pt-[27px] pb-[27px]">
        <h2 className="text-[19.5px] leading-[24px] font-medium" style={{ color: airbnb.ink }}>
          {booking.tripTitle}
        </h2>
        <div className="mt-[26px] flex flex-col gap-[26px]">
          {booking.trip.map((f) => (
            <TripFieldRow key={f.label} field={f} />
          ))}
        </div>
      </section>
      <SectionBand color={airbnb.band} />
      <section className="px-[26px] pt-[26px] pb-[26px]">
        <h2 className="text-[19.5px] leading-[24px] font-medium" style={{ color: airbnb.ink }}>
          {booking.payTitle}
        </h2>
        <div className="mt-[27px] flex flex-col">
          {booking.payOptions.map((o, i) => (
            <div key={o.key}>
              {i > 0 && <div className="my-[26px] h-px" style={{ background: airbnb.hairline }} />}
              <PayOptionRow option={o} selected={o.key === booking.selectedPay} />
            </div>
          ))}
        </div>
      </section>
      <SectionBand color={airbnb.band} />
      <div className="mt-[20px] h-px" style={{ background: airbnb.hairline }} />
      <HomeIndicator />
    </AppScreen>
  )
}
