import { useEffect, useState } from 'react'
import { apps, findApp } from './apps/registry'
import { boardHeight, boardWidth, type AppDefinition } from './ui'

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

function Scaled({ def, width }: { def: AppDefinition; width: number }) {
  const w = boardWidth(def.screens)
  const s = Math.min(1, width / w)
  return (
    <div style={{ width: w * s, height: boardHeight * s }} className="overflow-hidden">
      <div style={{ transform: `scale(${s})`, transformOrigin: 'top left', width: w }}>
        <def.Component />
      </div>
    </div>
  )
}

function Gallery() {
  return (
    <main className="mx-auto max-w-[1500px] p-8 font-inter">
      <h1 className="mb-6 text-2xl font-bold">App2 Clone — {apps.length} apps</h1>
      <div className="flex flex-col gap-10">
        {apps.map((def) => (
          <a key={def.id} href={`#/compare/${def.id}`} className="block">
            <div className="mb-2 text-sm font-semibold">
              {def.id} · {def.title} · {def.screens} screens
            </div>
            <Scaled def={def} width={1400} />
          </a>
        ))}
      </div>
    </main>
  )
}

function Compare({ def }: { def: AppDefinition }) {
  return (
    <main className="p-6 font-inter">
      <a href="#/" className="text-sm text-blue-600">← gallery</a>
      <h1 className="my-3 text-lg font-bold">{def.id} · {def.title}</h1>
      <div className="flex flex-col gap-6">
        <img src={`/flat/${def.id}.png`} alt="reference" style={{ maxWidth: 1400 }} />
        <Scaled def={def} width={1400} />
      </div>
    </main>
  )
}

export default function App() {
  const route = useHashRoute()
  const [mode, id] = route.includes('/') ? route.split('/') : ['board', route]
  const def = id ? findApp(id) : undefined
  if (!def) return <Gallery />
  if (mode === 'compare') return <Compare def={def} />
  return <def.Component />
}
