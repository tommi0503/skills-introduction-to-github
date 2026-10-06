import { Cloud, Code2, Infinity as Inf, Layers, Share2, Wrench, type LucideIcon } from 'lucide-react'
export const impacts: { icon: LucideIcon; pre: string; bold: string; post: string; y: number }[] = [
  { icon: Cloud, pre: '', bold: 'Cloud', post: ' Become Everything', y: 39 },
  { icon: Inf, pre: 'The ', bold: 'DevOps', post: ' Revolution', y: 79 },
  { icon: Code2, pre: 'More ', bold: 'Code', post: ' than Ever', y: 112 },
]
export const compare = {
  rows: [{ label: ['Posture', 'Management'], y: 62 }, { label: ['Native', 'Scanners'], y: 114 }],
}
export const market = {
  quote: ['"By 2026, over 40%', 'of organizations developing', 'proprietary applications', 'will adopt ASPM*'],
  circles: [
    { v: '$7.6B', l: ['AppSec Market Size'], cx: 252, cy: 67, r: 60, c: '#2f64e8', t: 11 },
    { v: '$3.4B', l: ['Security Testing', '(AST)'], cx: 182, cy: 140, r: 33, c: '#6f93f4', t: 8.5 },
    { v: '$2.8B', l: ['Vulnerability', 'Management'], cx: 273, cy: 138, r: 21, c: '#8aa8f6', t: 6.5 },
  ],
}
export const layers = ['Platform', 'Risk Intelligence Graph', 'Posture Management', 'Core Solutions', 'Integrations']
export const connector = {
  left: [{ t: 'Wide-Spectrum of Integrated Tools', y: 16, h: 72 }, { t: 'Risk Intelligence Graph: Code-to-Cloud Discovery', y: 91, h: 65 }],
  right: [{ t: 'Alert Deduplication', icon: Layers, y: 16, h: 52 }, { t: 'Data Correlation', icon: Share2, y: 72, h: 48 }, { t: 'Automated Remediation', icon: Wrench, y: 125, h: 31 }],
  copy: 'Integrate security tools across infrastructure, apps, and clouds for asset inventory and security insights.',
}
export const value = [
  { t: 'Seamless Scalability & Speed', d: 'Scale and standardize AppSec without compromising speed.', y: 54 },
  { t: 'Efficient Tool Consolidation', d: 'Streamline and centralize security tools for optimal effectiveness.', y: 94 },
  { t: 'Eliminating AppSec Blind Spots', d: 'Gain enhanced visibility to solve security blind spots effectively.', y: 134 },
]
export const pains = [
  { t: 'Expectations to innovate fast', x: 136, y: 67 }, { t: 'Sec & Dev working in silos', x: 114, y: 86 },
  { t: 'Too many security tools', x: 83, y: 108 }, { t: 'Unmanageable attack surface', x: 33, y: 129 },
]
