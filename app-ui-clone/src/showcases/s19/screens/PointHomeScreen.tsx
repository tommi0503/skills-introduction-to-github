import { NaverStatusBar } from '../../shared-naver'
import { BottomNav } from '../components/BottomNav'
import { NpayHeader } from '../components/NpayHeader'
import { PayTabs } from '../components/PayTabs'
import { PointPromoCard } from '../components/PointPromoCard'
import { WalletCardStack } from '../components/WalletCardStack'
import { ACTIVE_PAY_TAB, navItems, payTabs, walletCards } from '../data'

/** Wallet view: point/money card on top of the registered payment cards. */
export function PointHomeScreen() {
  return (
    <div className="absolute inset-0" style={{ background: '#0d141a' }}>
      <NaverStatusBar time="1:31" color="#fff" charging />
      <NpayHeader />
      <PayTabs tabs={payTabs} active={ACTIVE_PAY_TAB} height={42.3} className="absolute" style={{ left: 23.7, right: 24.8, top: 116.6 }} />
      <PointPromoCard style={{ left: 23.7, right: 24.8, top: 174.4 }} />
      <WalletCardStack cards={walletCards} />
      <BottomNav items={navItems} />
    </div>
  )
}
