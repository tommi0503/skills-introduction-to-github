import {
  Camera,
  Crop,
  Files,
  RotateCcw,
  Search,
  Trash2,
  User,
  WandSparkles,
  type LucideIcon,
} from 'lucide-react'

export type CaptureMode = 'AUTO' | 'MANUAL' | 'BATCH'
export const captureModes: CaptureMode[] = ['AUTO', 'MANUAL', 'BATCH']
export const activeMode: CaptureMode = 'MANUAL'

export const libraryFilters = ['All Scans', 'Receipts', 'Contracts', 'Tax 2024']

export interface ScanDoc {
  id: string
  title?: string
  meta?: string
  date?: string
}

export const scanDocs: ScanDoc[] = [
  { id: 'lease', title: 'Lease Agreement', meta: '4 PAGES · 2.1 MB', date: 'OCT 12, 2023' },
  { id: 'receipt', title: 'Dinner Receipt', meta: '1 PAGE · 420 KB', date: 'NOV 04, 2023' },
  { id: 'w2' },
  { id: 'notes' },
]

export interface NavItem {
  key: string
  label: string
  icon: LucideIcon
}

export const libraryTabs: NavItem[] = [
  { key: 'library', label: 'LIBRARY', icon: Files },
  { key: 'capture', label: 'CAPTURE', icon: Camera },
  { key: 'search', label: 'SEARCH', icon: Search },
  { key: 'profile', label: 'PROFILE', icon: User },
]

export interface FilterPreset {
  key: string
  label: string
}

export const filterPresets: FilterPreset[] = [
  { key: 'original', label: 'ORIGINAL' },
  { key: 'bw', label: 'B&W' },
  { key: 'enhance', label: 'ENHANCE' },
  { key: 'invert', label: 'INVERT' },
]

export interface EditAction extends NavItem {
  destructive?: boolean
}

export const editActions: EditAction[] = [
  { key: 'rotate', label: 'ROTATE', icon: RotateCcw },
  { key: 'crop', label: 'CROP', icon: Crop },
  { key: 'auto', label: 'AUTO', icon: WandSparkles },
  { key: 'retake', label: 'RETAKE', icon: Trash2, destructive: true },
]
