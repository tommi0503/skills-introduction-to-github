import type { DeckDefinition } from '../../ui'
import { Contents, Cover, FourKeys, LongText, Process, Summary, Thanks, ThreeKeys, TwoImages } from './slides'

const deck: DeckDefinition = {
  id: '11',
  title: '베이지색의 심플한 비즈니스 기획서',
  slides: [() => <Cover />, () => <Contents />, () => <LongText />, () => <TwoImages />, () => <FourKeys />, () => <ThreeKeys />, () => <Process />, () => <Summary />, () => <Thanks />],
}
export default deck
