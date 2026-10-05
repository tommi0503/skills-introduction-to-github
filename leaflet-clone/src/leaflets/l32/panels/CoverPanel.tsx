import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { BrandMark } from '../../shared-3233/components/BrandMark'
import { hutech } from '../../shared-3233/theme'
import { brand, cover } from '../data'

/** Left outside panel: brand row, big statement, sub copy and the concentric-arch artwork. */
export function CoverPanel() {
  return (
    <Panel background={hutech.navySoft} className="font-noto-sans">
      <Placed x={46} y={47} className="flex items-center gap-[10px]">
        <BrandMark size={34} />
        <span className="text-[23px] font-medium" style={{ color: hutech.onNavySoft }}>
          {brand.name}
        </span>
      </Placed>
      <Placed x={46} y={106}>
        <h1 className="m-0 text-[59px] font-bold leading-[77px] tracking-[-0.02em]" style={{ color: hutech.onNavy }}>
          {cover.headline.map((line) => (
            <span key={line} className="block whitespace-nowrap">
              {line}
            </span>
          ))}
        </h1>
      </Placed>
      <Placed x={46} y={437}>
        <p className="m-0 text-[26.4px] leading-[38px]" style={{ color: hutech.onNavySoft }}>
          {cover.sub.map((line) => (
            <span key={line} className="block">
              {line}
            </span>
          ))}
        </p>
      </Placed>
      <Placed x={45} y={560}>
        <ImagePlaceholder label="concentric arch artwork" style={{ width: 396, height: 458, borderRadius: '198px 198px 0 0' }} />
      </Placed>
    </Panel>
  )
}
