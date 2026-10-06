import { Abs, Slide, type DeckDefinition } from '../../ui'
import { FindingColumn, HLine, PageMark } from './components'
import { findings, footer, header, title } from './data'
import { theme } from './theme'

function Conclusion() {
  const xs = [58, 460, 865]
  return (
    <Slide background={theme.bg}>
      <Abs x={50} y={36} className={`${theme.serif} text-[14px] font-bold`}>{header.left}</Abs>
      <Abs x={1230} y={36} className={`${theme.serif} text-[14px] font-bold whitespace-nowrap`} style={{ transform: 'translateX(-100%)' }}>{header.right}</Abs>
      <HLine y={25} />
      <Abs x={50} y={96} className={`${theme.serif} text-[62px] font-bold leading-none`}>{title}</Abs>
      <HLine y={62} />
      {[420, 825].map((x) => <Abs key={x} x={x} y={185} w={2} h={455} style={{ background: '#d4d4d2' }} />)}
      {findings.map((f, i) => <FindingColumn key={i} f={f} x={xs[i]} />)}
      <HLine y={205} /><HLine y={220} />
      <Abs x={50} y={618} className="font-inter text-[12px]">{footer.left}</Abs>
      <PageMark text={footer.page} />
    </Slide>
  )
}
const deck: DeckDefinition = { id: '01', title: 'Conclusion', slides: [Conclusion] }
export default deck
