import { ImagePlaceholder, KeyValueList, Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { Heading } from '../components/Heading'
import { admission, greeting, trees } from '../data'
import { theme } from '../theme'

const X = 62
const PARAGRAPH_TOPS = [483, 596, 680]

/** Inside-left: 입장료 list, 인사말 and the forest illustration. */
export function InfoPanel() {
  return (
    <Panel background={theme.paper}>
      <Heading x={X} y={76} color={theme.accent}>
        {admission.heading}
      </Heading>
      <Placed x={X} y={163} width={330} style={{ color: theme.muted }}>
        <KeyValueList
          items={admission.fees.map((f) => ({ key: f.label, label: f.label, value: f.price }))}
          className="font-pretendard text-[19px]"
          rowClassName="h-[32px] items-center"
          valueClassName="text-right"
        />
      </Placed>
      <Placed x={X} y={290} className="whitespace-nowrap font-pretendard text-[19px] leading-[30px] tracking-[0.03em]" style={{ color: theme.muted }}>
        {admission.note}
      </Placed>
      <Heading x={X} y={399} color={theme.accent}>
        {greeting.heading}
      </Heading>
      {greeting.paragraphs.map((p, i) => (
        <TextLines
          key={i}
          className="absolute font-pretendard text-[19px] font-extrabold tracking-[0.07em]"
          style={{ left: X, top: PARAGRAPH_TOPS[i], color: theme.body }}
          lines={p}
          lineClassName="leading-[28px]"
        />
      ))}
      <ImagePlaceholder label={trees.label} className="absolute" style={trees.style} />
    </Panel>
  )
}
