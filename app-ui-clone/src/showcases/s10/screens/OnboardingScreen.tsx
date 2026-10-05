import { Heart, ShoppingCart } from 'lucide-react'
import { Placed } from '../../../ui'
import { AppStatusBar } from '../components/AppStatusBar'
import { CurvedArrow } from '../components/CurvedArrow'
import { FloatingIcon } from '../components/FloatingIcon'
import { ProductCard } from '../components/ProductCard'
import { cheetos, onboarding, potatoChips } from '../data'
import { onboardingCard, onboardingCardOrange } from '../metrics'
import { theme } from '../theme'

/** Phone 1 — "Your Favorite Treats, Anytime" onboarding. */
export function OnboardingScreen() {
  return (
    <div
      className="absolute inset-0"
      style={{ background: `linear-gradient(180deg, ${theme.yellow} 0px, ${theme.yellow} 12px, ${theme.screen} 280px)` }}
    >
      <AppStatusBar />

      {/* translucent back panels */}
      <Placed x={74} y={107} width={230} height={210} style={{ background: 'rgba(255,204,0,0.4)', borderRadius: 16 }} />
      <Placed x={74} y={312} width={206} height={266} style={{ background: 'rgba(255,150,40,0.25)', borderRadius: 16 }} />

      <Placed x={116} y={306} rotate={11}>
        <ProductCard product={cheetos} metrics={onboardingCardOrange} />
      </Placed>
      <Placed x={54} y={137} rotate={-13}>
        <ProductCard product={potatoChips} metrics={onboardingCard} />
      </Placed>

      <Placed x={250} y={140}>
        <CurvedArrow
          width={80}
          height={80}
          color={theme.yellow}
          d="M2 12 C 40 4, 66 20, 70 66"
          head={{ x: 71, y: 76, angle: 92 }}
        />
      </Placed>
      <Placed x={296} y={222}>
        <FloatingIcon icon={ShoppingCart} size={49} color={theme.yellow} iconSize={20} filled={false} />
      </Placed>

      <Placed x={36} y={470}>
        <CurvedArrow
          width={130}
          height={60}
          color={theme.orange}
          d="M126 56 C 70 66, 14 58, 8 12"
          head={{ x: 7, y: 2, angle: -92 }}
        />
      </Placed>
      <Placed x={19} y={423}>
        <FloatingIcon icon={Heart} size={44} color={theme.orange} iconSize={20} />
      </Placed>

      <Placed x={20} y={603}>
        <h1 className="text-[37px] leading-[48px] [word-spacing:3px] text-black">
          <span className="font-bold">{onboarding.titleBold[0]}</span>
          <br />
          <span className="font-bold">{onboarding.titleBold[1]}</span> <span className="font-normal">{onboarding.titleLight}</span>
        </h1>
        <p className="mt-[5px] text-[14px] text-[#555]">{onboarding.subtitle}</p>
      </Placed>

      <Placed x={20} y={748} width={350}>
        <button type="button" className="h-[56px] w-full rounded-full bg-black text-[16px] font-semibold text-white">
          {onboarding.cta}
        </button>
      </Placed>
    </div>
  )
}
