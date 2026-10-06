import { useEffect, useState } from 'react'
import { decks, findDeck } from './decks/registry'
import { Board, boardSize, type DeckDefinition } from './ui'

function useHash() {
  const read = () => window.location.hash.replace(/^#\/?/, '')
  const [h, setH] = useState(read)
  useEffect(() => {
    const on = () => setH(read())
    window.addEventListener('hashchange', on)
    return () => window.removeEventListener('hashchange', on)
  }, [])
  return h
}

function Thumb({ deck }: { deck: DeckDefinition }) {
  const { width, height } = boardSize(deck.slides.length)
  const s = 640 / width
  return (
    <div style={{ width: 640, height: height * s }} className="overflow-hidden">
      <div style={{ transform: `scale(${s})`, transformOrigin: 'top left' }}>
        <Board deck={deck} />
      </div>
    </div>
  )
}

export default function App() {
  const deck = findDeck(useHash())
  if (deck) return <Board deck={deck} />
  return (
    <main className="grid grid-cols-2 gap-8 p-8 font-inter">
      {decks.map((d) => (
        <a key={d.id} href={`#/${d.id}`}>
          <div className="mb-2 text-sm font-semibold">{d.id} · {d.title} · {d.slides.length} slides</div>
          <Thumb deck={d} />
        </a>
      ))}
    </main>
  )
}
