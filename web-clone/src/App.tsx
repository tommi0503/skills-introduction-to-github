import { useEffect, useState } from 'react'
import { findSite, sites } from './sites/registry'
import { FRAME, type SiteDefinition } from './ui'

function useHashRoute() {
  const read = () => window.location.hash.replace(/^#\/?/, '')
  const [hash, setHash] = useState(read)
  useEffect(() => {
    const on = () => setHash(read())
    window.addEventListener('hashchange', on)
    return () => window.removeEventListener('hashchange', on)
  }, [])
  return hash
}

function Scaled({ def, width }: { def: SiteDefinition; width: number }) {
  const s = width / FRAME.width
  return (
    <div style={{ width, height: FRAME.height * s }} className="overflow-hidden">
      <div style={{ transform: `scale(${s})`, transformOrigin: 'top left', width: FRAME.width }}>
        <def.Component />
      </div>
    </div>
  )
}

function Gallery() {
  return (
    <main className="mx-auto max-w-[1500px] p-8 font-inter">
      <h1 className="mb-6 text-2xl font-bold">Web Clone — {sites.length} sites</h1>
      <div className="grid grid-cols-4 gap-8">
        {sites.map((def) => (
          <a key={def.id} href={`#/compare/${def.id}`} className="block">
            <div className="mb-2 text-sm font-semibold">{def.id} · {def.title}</div>
            <Scaled def={def} width={320} />
          </a>
        ))}
      </div>
    </main>
  )
}

function Compare({ def }: { def: SiteDefinition }) {
  return (
    <main className="p-6 font-inter">
      <a href="#/" className="text-sm text-blue-600">← gallery</a>
      <h1 className="my-3 text-lg font-bold">{def.id} · {def.title} — {def.url}</h1>
      <div className="flex gap-6">
        <img src={`/flat/${def.id}.png`} alt="reference" style={{ width: 700 }} />
        <Scaled def={def} width={700} />
      </div>
    </main>
  )
}

export default function App() {
  const route = useHashRoute()
  const [mode, id] = route.includes('/') ? route.split('/') : ['frame', route]
  const def = id ? findSite(id) : undefined
  if (!def) return <Gallery />
  if (mode === 'compare') return <Compare def={def} />
  return <def.Component />
}
