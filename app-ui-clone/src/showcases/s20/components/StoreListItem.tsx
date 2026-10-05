import { ImagePlaceholder } from '../../../ui'
import type { StoreRow } from '../data'

export interface StoreListItemProps {
  store: StoreRow
  divider?: boolean
}

/** One store: logo (placeholder), green name, method and optional note. */
export function StoreListItem({ store, divider = true }: StoreListItemProps) {
  return (
    <div className="relative flex" style={{ paddingLeft: 124, paddingTop: 17.5, paddingBottom: 18 }}>
      <div className="absolute inset-y-0 flex items-center justify-center" style={{ left: 18, width: 98 }}>
        <ImagePlaceholder label={`${store.name} logo`} style={{ width: store.logo.width, height: store.logo.height }} />
      </div>
      <div className="flex flex-col" style={{ paddingLeft: 6 }}>
        <span style={{ fontSize: 15, lineHeight: '22px', fontWeight: 600, color: '#00a854', letterSpacing: -0.2 }}>
          {store.name}
        </span>
        <span style={{ fontSize: 15, lineHeight: '23px', fontWeight: 700, color: '#1b1b1b', letterSpacing: -0.45 }}>
          {store.method}
        </span>
        {store.description && (
          <span
            className="whitespace-pre-line" style={{ fontSize: 14, lineHeight: '20px', color: '#747474', letterSpacing: -0.5, marginTop: 0 }}
          >
            {store.description}
          </span>
        )}
      </div>
      {divider && (
        <span className="absolute bottom-0" style={{ left: 124, right: 21, height: 1.5, background: '#f0f0f0' }} />
      )}
    </div>
  )
}
