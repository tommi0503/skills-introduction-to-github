import { Leaflet, Panel, type LeafletDefinition } from '../../ui'
const fonts = ['font-pretendard','font-noto-sans','font-gothic-a1','font-nanum-gothic','font-plex-kr','font-sunflower','font-dohyeon','font-gowun-dodum','font-blackhan','font-jua']
function T() {
  return (
    <Leaflet panels={3}>
      <Panel>
        {fonts.map((f) => (
          <p key={f} className={`${f} m-0 text-[20px] leading-[40px] font-medium`}><span data-f={f}>개막식 및 북마켓 오픈</span></p>
        ))}
      </Panel>
      <Panel />
      <Panel />
    </Leaflet>
  )
}
const d: LeafletDefinition = { id: '19', title: 't', panels: 3, Component: T }
export default d
