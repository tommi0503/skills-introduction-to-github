import type { CSSProperties } from 'react'
import { Leaflet, type LeafletDefinition } from '../../ui'
import { growth } from '../shared-3031/theme'
import { ServiceGrid } from './components/ServiceGrid'
import { IntroPanel } from './panels/IntroPanel'
import { ProcedurePanel } from './panels/ProcedurePanel'
import { ServicesPanel } from './panels/ServicesPanel'

const vars = { '--ink': growth.ink, color: growth.text } as CSSProperties

function Leaflet31() {
  return (
    <Leaflet panels={3} background={growth.sheetBg} overlay={<ServiceGrid />} style={vars}>
      <IntroPanel />
      <ServicesPanel />
      <ProcedurePanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '31', title: '지역 성장 지원사업 (내면)', panels: 3, Component: Leaflet31 }
export default definition
