import { Leaflet, Panel, type LeafletDefinition } from '../../ui'
const lines = ['2056','도서관','책축제']
function T() {
  return (
    <Leaflet panels={3}>
      <Panel>
        {lines.map((f) => (
          <p key={f} className="font-blackhan m-0 text-[100px] leading-[200px]">{f}</p>
        ))}
      </Panel>
      <Panel />
      <Panel />
    </Leaflet>
  )
}
const d: LeafletDefinition = { id: '19', title: 't', panels: 3, Component: T }
export default d
