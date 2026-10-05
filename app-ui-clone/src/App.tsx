import { useEffect, useState } from 'react'
import { findShowcase, showcases } from './showcases/registry'
import type { ShowcaseDefinition } from './ui'

function useHashRoute(): string {
  const [hash, setHash] = useState(() => window.location.hash.replace(/^#\/?/, ''))
  useEffect(() => {
    const onChange = () => setHash(window.location.hash.replace(/^#\/?/, ''))
    window.addEventListener('hashchange', onChange)
    return () => window.removeEventListener('hashchange', onChange)
  }, [])
  return hash
}

function Thumb({ def, maxWidth }: { def: ShowcaseDefinition; maxWidth: number }) {
  const scale = Math.min(1, maxWidth / def.width)
  return (
    <div style={{ width: def.width * scale, height: def.height * scale }} className="overflow-hidden">
      <div style={{ transform: `scale(${scale})`, transformOrigin: 'top left', width: def.width }}>
        <def.Component />
      </div>
    </div>
  )
}

function Gallery() {
  return (
    <main className="mx-auto max-w-[1400px] p-8 font-inter">
      <h1 className="mb-6 text-2xl font-bold">App UI Clone — {showcases.length} showcases</h1>
      <div className="grid grid-cols-1 gap-8 lg:grid-cols-2">
        {showcases.map((def) => (
          <a key={def.id} href={`#/compare/${def.id}`} className="block rounded-xl bg-white p-4 shadow-sm">
            <div className="mb-3 text-sm font-semibold">
              {def.id} · {def.title}
            </div>
            <Thumb def={def} maxWidth={640} />
          </a>
        ))}
      </div>
    </main>
  )
}

function Compare({ def }: { def: ShowcaseDefinition }) {
  return (
    <main className="p-6 font-inter">
      <a href="#/" className="text-sm text-blue-600">
        ← gallery
      </a>
      <h1 className="my-3 text-lg font-bold">
        {def.id} · {def.title}
      </h1>
      <div className="flex flex-wrap gap-6">
        <figure>
          <figcaption className="mb-1 text-xs text-neutral-500">reference</figcaption>
          <img src={`/reference/${def.id}.jpg`} width={def.width} height={def.height} alt="reference" />
        </figure>
        <figure>
          <figcaption className="mb-1 text-xs text-neutral-500">implementation</figcaption>
          <def.Component />
        </figure>
      </div>
    </main>
  )
}

export default function App() {
  const route = useHashRoute()
  const [mode, id] = route.includes('/') ? route.split('/') : ['stage', route]
  const def = id ? findShowcase(id) : undefined
  if (!def) return <Gallery />
  if (mode === 'compare') return <Compare def={def} />
  return <def.Component />
}
