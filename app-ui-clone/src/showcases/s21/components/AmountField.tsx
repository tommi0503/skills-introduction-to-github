import { CircleX } from 'lucide-react'

export interface AmountFieldProps {
  label: string
  placeholder: string
  value?: string
}

/** Question label + large underlined amount input with a clear button when filled. */
export function AmountField({ label, placeholder, value }: AmountFieldProps) {
  return (
    <div style={{ padding: '0 20px' }}>
      <div style={{ fontSize: 16, lineHeight: '20px', color: '#1d1d1f', letterSpacing: -0.4, fontWeight: 500 }}>{label}</div>
      <div className="relative flex items-center" style={{ height: 44, marginTop: 7, borderBottom: '1px solid #efeff1' }}>
        {value ? (
          <span style={{ fontSize: 27.8, fontWeight: 700, color: '#000', letterSpacing: -0.6, marginTop: 3 }}>{value}</span>
        ) : (
          <span style={{ fontSize: 22, color: '#b7b7b9', letterSpacing: -0.6 }}>{placeholder}</span>
        )}
        {value && (
          <CircleX size={23} strokeWidth={2} color="#fff" fill="#8c8c8c" className="absolute" style={{ right: -1.5, top: 13 }} />
        )}
      </div>
    </div>
  )
}
