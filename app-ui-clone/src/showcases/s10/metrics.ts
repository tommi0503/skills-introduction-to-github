import type { ProductCardMetrics } from './components/ProductCard'

/** Large featured card on the home screen. */
export const featuredCard: ProductCardMetrics = {
  width: 350,
  height: 382,
  pad: 16,
  radius: 30,
  innerRadius: 26,
  imageHeight: 278,
  titleSize: 37.5,
  titleLeading: 46,
  titleInset: { x: 17, y: 14 },
  heartSize: 42,
  heartInset: 16,
  priceLabelSize: 15,
  priceSize: 19,
  priceBottom: 16,
  button: { width: 185, height: 51, fontSize: 15.5, right: 14, bottom: 16 },
  photo: { left: 28, top: 118, width: 292, height: 160 },
}

/** Small tilted cards on the onboarding screen. */
export const onboardingCard: ProductCardMetrics = {
  width: 213,
  height: 235,
  pad: 12,
  radius: 18,
  innerRadius: 16,
  imageHeight: 160,
  titleSize: 23,
  titleLeading: 27,
  titleInset: { x: 12, y: 12 },
  heartSize: 26,
  heartInset: 10,
  priceLabelSize: 10,
  priceSize: 12,
  priceBottom: 12,
  button: { width: 112, height: 42, fontSize: 11.5, right: 10, bottom: 8 },
  photo: { left: 62, top: 24, width: 127, height: 136 },
}

export const onboardingCardOrange: ProductCardMetrics = {
  ...onboardingCard,
  width: 234,
  height: 230,
  imageHeight: 166,
  photo: { left: 6, top: 40, width: 204, height: 116 },
}
