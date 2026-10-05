import { ImagePlaceholder, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { BigWord, CryptoCard, Lines } from './components/StageDecor'
import { ethereum, stageCopy } from './data'
import { PortfolioScreen } from './screens/PortfolioScreen'
import { TopUpScreen } from './screens/TopUpScreen'
import { theme } from './theme'

function InvestmentShowcase() {
  return (
    <Stage width={752} height={564} background={theme.stage} className="font-inter text-[#141414]">
      <Placed x={-4} y={350}>
        <BigWord word={stageCopy.bigWord} />
      </Placed>

      <Placed x={23} y={25} className="text-[15px] leading-[18px]">
        {stageCopy.kicker}
      </Placed>
      <Placed x={23} y={53}>
        <Lines lines={stageCopy.product} className="text-[13.5px] leading-[15.5px]" />
      </Placed>
      <Placed x={402} y={26}>
        <Lines lines={stageCopy.headline} className="text-[19px] font-bold leading-[22.5px] tracking-[-0.3px] text-[#141a3a]" />
      </Placed>
      <Placed x={402} y={79}>
        <Lines lines={stageCopy.body} className="text-[7.5px] leading-[11.5px]" />
      </Placed>
      <Placed x={694} y={22}>
        <ImagePlaceholder label="Bull logo" className="h-[24px] w-[32px] rounded-[4px]" />
      </Placed>

      <Placed x={130.5} y={61}>
        <PortfolioScreen />
      </Placed>
      <Placed x={389.5} y={117.5}>
        <TopUpScreen />
      </Placed>
      <Placed x={35} y={280}>
        <CryptoCard coin={ethereum} />
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '15',
  title: 'Investment app',
  width: 752,
  height: 564,
  Component: InvestmentShowcase,
}
export default showcase
