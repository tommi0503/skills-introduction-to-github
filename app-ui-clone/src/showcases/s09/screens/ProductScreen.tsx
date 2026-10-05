import { HomeIndicator, ImagePlaceholder } from '../../../ui'
import { DarkButton } from '../components/DarkButton'
import { DarkHeader } from '../components/DarkHeader'
import { NutritionRow } from '../components/NutritionRow'
import { Stepper } from '../components/Stepper'
import { TagChip } from '../components/TagChip'
import { TextBlock } from '../components/TextBlock'
import type { ProductVariant } from '../data'
import { theme } from '../theme'

export interface ProductScreenProps {
  product: ProductVariant
  /** Top of the light sheet below the header (pt). */
  sheetTop?: number
  /** How far the sheet content is scrolled (pt). */
  scroll?: number
  /** Distance of the sticky footer controls from the bottom edge (pt). */
  footerBottom?: number
}

const section = 'border-t px-[21px]'

/** Product detail sheet with sticky footer. Reused scrolled for the cropped right-hand phone. */
export function ProductScreen({ product, sheetTop = 118.7, scroll = 0, footerBottom = 31.5 }: ProductScreenProps) {
  return (
    <div className="absolute inset-0 bg-white">
      <DarkHeader height={150} cartCount={product.cartCount} rounded={false} />
      <div className="absolute inset-x-0 bottom-0 z-20 overflow-hidden rounded-t-[22px]" style={{ top: sheetTop, background: theme.canvas }}>
        <div style={{ transform: `translateY(${-scroll}px)` }}>
          <div className="relative" style={{ height: 372 }}>
            <span className="absolute top-[11px] left-1/2 h-[3px] w-[60px] -translate-x-1/2 rounded-full bg-[#a9a9a9]" />
            <ImagePlaceholder label="quinoa bowl" className="absolute top-[35.3px] left-[21px] h-[318px] w-[318px] rounded-full" />
          </div>
          <div className="bg-white pb-[200px]" style={{ color: theme.ink }}>
            <div className="px-[21px] pt-[25.6px] pb-[19px]">
              <div className="font-poppins text-[27px] leading-[32px] font-medium tracking-[0.025em]">{product.name}</div>
              <div className="mt-[2.4px] font-poppins text-[16.5px] leading-[22px]" style={{ color: theme.muted }}>
                {product.weight}
              </div>
              <div className="mt-[14px] flex gap-[14px]">
                {product.tags.map((t) => (
                  <TagChip key={t.key} tag={t} className="bg-[#f3f3f5]" />
                ))}
              </div>
            </div>
            <div className={`${section} pt-[16px] pb-[15.5px]`} style={{ borderColor: theme.hairline }}>
              <div className="font-poppins text-[14px] leading-[20px]" style={{ color: theme.muted }}>
                {product.nutritionTitle}
              </div>
              <div className="mt-[10px]">
                <NutritionRow items={product.nutrients} />
              </div>
            </div>
            <div className={`${section} pt-[17.5px] pb-[16.5px]`} style={{ borderColor: theme.hairline }}>
              <TextBlock title="Ingredients" lines={product.ingredients} />
            </div>
            <div className={`${section} pt-[17px]`} style={{ borderColor: theme.hairline }}>
              <TextBlock title="Terms and conditions of storage" lines={product.storage} />
            </div>
          </div>
        </div>
      </div>

      <div className="absolute inset-x-[21px] z-30 flex h-[44px] gap-[16px]" style={{ bottom: footerBottom }}>
        <div className="w-[117px]">
          <Stepper value={product.quantity} />
        </div>
        <DarkButton className="flex-1 justify-between px-[18px]">
          <span>Add to Cart</span>
          <span className="text-[16px]">{product.price}</span>
        </DarkButton>
      </div>
      <HomeIndicator width={116} bottom={8} className="z-40" />
    </div>
  )
}
