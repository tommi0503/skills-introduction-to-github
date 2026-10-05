import { Leaflet, Panel, type LeafletDefinition } from '../../ui'
const fonts = ['font-dela', 'font-song-myung', 'font-hahmlet font-extrabold', 'font-blackhan', 'font-myeongjo font-extrabold', 'font-noto-serif font-black', 'font-gowun-batang font-bold', 'font-dohyeon', 'font-yeon-sung', 'font-sunflower font-bold', 'font-hahmlet font-bold']
function C() {
  return (
    <Leaflet panels={3}>
      <Panel background="#ebe1c2">
        {fonts.map((f) => (
          <div key={f} className={f} style={{ fontSize: 34, color: '#5b2a2e' }}>한아름 서도윤 {f.split(' ')[0].slice(5)}</div>
        ))}
      </Panel>
      <Panel background="#552628">
        {fonts.map((f) => (
          <div key={f} className={f} style={{ fontSize: 60, color: '#e8dcc0', lineHeight: 1.1 }}>특별한</div>
        ))}
      </Panel>
      <Panel>
        {fonts.map((f) => (
          <div key={f} className={f} style={{ fontSize: 24, color: '#333' }}>2015년 창단 이후 매년 두 차례,</div>
        ))}
      </Panel>
    </Leaflet>
  )
}
const def: LeafletDefinition = { id: '15', title: 't', panels: 3, Component: C }
export default def
