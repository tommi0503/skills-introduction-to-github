import type { DeckDefinition } from '../../ui'
import { Device, Frame, Headline, Small, T, Year } from './components'
import { activity, categories, future, record, tagline } from './data'
import { theme } from './theme'

function Activity() {
  return (
    <Frame k={theme.k1}>
      <Headline x={25} y={20} lines={['TRACK YOUR', '*FINANCIAL*', 'ACTIVITY']} />
      <Small x={350} y={22} lines={tagline} size={5.5} />
      <Small x={629} y={28} lines={activity.right} size={10.5} lh={14} right />
      {categories.map((c) => {
        const I = c.icon
        return (
          <div key={c.label}>
            <div className="absolute" style={{ left: 25, top: c.y, width: c.w, height: 44, background: c.active ? theme.lime : theme.card, borderRight: c.active ? 'none' : '3px solid #eee' }} />
            <div className="absolute flex items-center justify-center rounded-full" style={{ left: 38, top: c.y + 14, width: 16, height: 16, background: c.active ? '#222' : '#2e2e2e', color: '#fff' }}><I size={8} /></div>
            <T x={62} y={c.y + 16} className="text-[8px] font-bold" style={{ color: c.active ? '#000' : '#fff' }}>{c.label}</T>
          </div>
        )
      })}
      <Device x={353} y={99} w={207} h={290} />
      <Year x={617} y={325} />
    </Frame>
  )
}
function Trust() {
  return (
    <Frame k={theme.k1}>
      <Small x={24} y={22} lines={tagline} size={5.5} />
      <Headline x={100} y={20} lines={['YOUR', '*TRUST* IS', 'PARAMO', 'UNT TO US.']} />
      <Year x={24} y={183} />
      <Device x={101} y={192} w={222} h={250} />
    </Frame>
  )
}
function Future() {
  return (
    <Frame k={theme.k1}>
      <Headline x={395} y={22} lines={future.heading.map((l) => (l === 'FINANCIAL' ? '*FINANCIAL*' : l))} size={38} lh={40} />
      <Small x={520} y={270} lines={future.body} size={12} lh={15} />
    </Frame>
  )
}
function Record() {
  return (
    <Frame k={theme.k2}>
      <Device x={262} y={-40} w={221} h={190} />
      <Small x={25} y={25} lines={record.saving} size={12} lh={15} />
      <T x={535} y={0} className="h-[200px] w-[159px] bg-[#1a1a1a]" />
      <T x={655} y={16} className="text-[11px] font-bold" style={{ color: theme.lime }}>01</T>
      <Small x={549} y={147} lines={record.uncertainty} size={11} lh={14} />
      <div className="absolute" style={{ left: 459, top: 201, width: 75, height: 77, background: theme.lime }} />
      <Headline x={25} y={164} lines={['OUR *TRACK*', '*RECORD* SPEAKS', 'FOR ITSELF']} size={38} lh={40} />
      {record.stats.map((s, i) => (
        <T key={s} x={25 + i * 165} y={298} className="whitespace-nowrap text-[52px] leading-none" style={{ fontStretch: '110%', fontWeight: 600, color: 'transparent', WebkitTextStroke: '1.2px #6b6b6b' }}>{s}</T>
      ))}
      {record.cols.map((c, i) => <T key={i} x={358 + i * 168} y={309} w={160} className="text-[7px] font-bold leading-[9px]">{c}</T>)}
    </Frame>
  )
}
const deck: DeckDefinition = { id: '10', title: 'Finance', slides: [Activity, Trust, Future, Record] }
export default deck
