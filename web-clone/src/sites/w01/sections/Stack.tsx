import { ImagePlaceholder } from '../../../ui'
import { Button } from '../components/Button'
import { Column } from '../components/Column'
import { ProductLabel } from '../components/ProductLabel'
import { TwoTone } from '../components/TwoTone'
import { stack } from '../data'
import { theme } from '../theme'

export function Stack() {
  return (
    <Column height={1212} className="px-[48px]">
      <div className="flex items-start justify-between pt-[55px]">
        <div className="w-[576px]">
          <TwoTone muted={stack.muted} strong={stack.strong} />
          <p className="mt-[12px] text-[16px] leading-6" style={{ color: theme.muted }}>{stack.body}</p>
        </div>
        <Button variant="outline" className="mt-[27px]">{stack.cta}</Button>
      </div>
      <div className="mt-[56px] grid grid-cols-2 gap-[40px]">
        {stack.models.map((m) => (
          <div key={m.name}>
            <ImagePlaceholder label={`${m.name} demo video`} className="h-[300px] w-full" />
            <div className="mt-[24px]">
              <ProductLabel {...m} />
            </div>
          </div>
        ))}
      </div>
      <div className="mt-[62px] h-px w-full" style={{ background: theme.rule }} />
      <h3 className="mt-[56px] text-[20px] leading-[26px] font-medium" style={{ color: theme.ink }}>{stack.agentsTitle}</h3>
      <ImagePlaceholder label="managed agents illustration" className="mt-[24px] h-[317px] w-full" />
      <div className="mt-[23px]">
        <ProductLabel {...stack.agents} />
      </div>
    </Column>
  )
}
