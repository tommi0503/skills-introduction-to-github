import type { Product } from '../data'
import { ProductCard } from './ProductCard'

/** Two independent columns of product tiles. */
export function MasonryGrid({ columns, gap, showSave }: { columns: Product[][]; gap: number; showSave?: boolean }) {
  return (
    <div className="flex" style={{ gap }}>
      {columns.map((col, i) => (
        <div key={i} className="flex flex-1 flex-col" style={{ gap }}>
          {col.map((p) => (
            <ProductCard key={p.id} product={p} showSave={showSave} />
          ))}
        </div>
      ))}
    </div>
  )
}
