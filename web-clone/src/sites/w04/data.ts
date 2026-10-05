import type { LucideIcon } from 'lucide-react'
import { ArrowRightLeft, Earth, Lock, MapPin, ScanSquare, ShieldPlus, Zap, MonitorCog, Globe } from 'lucide-react'

export interface Feature {
  icon: LucideIcon
  title: string
  body: string
}

export interface CustomerTab {
  name: string
  x: number
  active?: boolean
}

export interface LogoSlot {
  x: number
  y: number
  w: number
  h: number
}

export interface Plan {
  name: string
  tagline: string
  price: string
  unit?: string
  note?: string
  features: string[][]
  cta: string
}

export const nav = {
  links: [
    { label: 'Products', menu: true },
    { label: 'Solutions', menu: true },
    { label: 'Resources', menu: true },
    { label: 'Pricing', menu: false },
  ],
  alert: 'Under attack?',
  login: 'Login',
  contact: 'Contact sales',
}

export const hero = {
  eyebrow: 'Connect 2026 · The Agentic Conference of the Year · Oct 19-21',
  title: ['Everything we learned from powering', '20% of the Internet—yours by default'],
  body: ['One platform for your apps, agents, and workforce.', 'Build, secure, and scale without managing infrastructure.'],
  cta: 'Start building for free',
}

export const region = {
  title: 'Region: Earth',
  body: 'One smart network for workloads + security — close to users, close to data.',
  features: [
    {
      icon: Earth,
      title: 'Run everywhere',
      body: "Security, connectivity, and code run in 335+ cities around the world, within 50ms of 95% of the world's population.",
    },
    {
      icon: MapPin,
      title: 'Run anywhere',
      body: 'Our network is close to your users, applications, and sites. It optimizes all your traffic from source to destination for low latency.',
    },
    { icon: ScanSquare, title: 'Run at massive scale', body: 'No more capacity planning. Ever.' },
  ] satisfies Feature[],
}

export const customers = {
  title: 'Cloudflare powers 45% of the Fortune 500',
  body: 'Trusted by the teams you trust.',
  tabs: [
    { name: 'Shopify', x: 278, active: true },
    { name: 'Character.AI', x: 406 },
    { name: 'Intercom', x: 564 },
    { name: 'DoorDash', x: 700 },
    { name: 'Discord', x: 843 },
    { name: 'Zendesk', x: 971 },
    { name: 'Lovable', x: 1105 },
    { name: 'npm', x: 1235 },
  ] satisfies CustomerTab[],
  quote: [
    'For Shopify, the real challenge is not about how',
    'many different pieces of complex technology',
    'we can use but the opposite. Cloudflare helps',
    'us find a simple way to achieve something',
    'very complex that we can scale and maintain.',
  ],
  author: 'Duncan Davidson',
  role: 'VP of Developer Productivity',
  company: 'Shopify',
  more: 'And thousands more...',
  logos: [
    { x: 120, y: 2546, w: 68, h: 40 },
    { x: 316, y: 2550, w: 36, h: 24 },
    { x: 464, y: 2550, w: 132, h: 24 },
    { x: 660, y: 2543, w: 131, h: 38 },
    { x: 856, y: 2548, w: 133, h: 28 },
    { x: 1070, y: 2538, w: 95, h: 48 },
    { x: 1247, y: 2551, w: 73, h: 20 },
  ] satisfies LogoSlot[],
}

export const why = {
  title: 'Why choose Cloudflare',
  body: 'Everything needed to build secure, performant applications',
  chaos: {
    status: 'STATUS: UNRESOLVED',
    title: ['Fighting infra with', '“cloud”'],
    incidents: '2931 Open incidents',
    circuit: 'MPLS circuit down',
    leak: ['Sensitive d', '12 custome', 'in the last h'],
    whisper: ['"Egress costs just doubled this week — caching', 'not working at edge. Can we fix this by EOD?"'],
  },
  ship: { title: ['Shipping with', 'Cloudflare'], status: ['Pushed', '106', 'new updates today'] },
}

export const pricing = {
  title: 'Pay only when your code runs',
  body: '(Not to keep servers warm.)',
  tabs: [
    { label: 'Network & CDN', icon: Earth, active: true },
    { label: 'SASE / Zero Trust', icon: MonitorCog },
    { label: 'Compute & Storage', icon: Zap },
  ],
  intro: {
    title: 'Pay for clean traffic',
    body: 'One stack of security and performance for every site — same DDoS mitigation, same global CDN, same network at every tier. You only pay for the depth your site needs.',
  },
  flow: {
    from: 'Visitor traffic',
    to: 'Your site',
    caption: 'Same protection at every tier — paid plans add depth',
    layers: [
      { label: 'CDN', icon: Globe },
      { label: 'DDoS', icon: ShieldPlus },
      { label: 'SSL', icon: Lock },
      { label: 'WAF', icon: Zap },
      { label: 'Bot', icon: ArrowRightLeft },
    ],
  },
  plans: [
    {
      name: 'Free',
      tagline: 'for hobby projects',
      price: '$0',
      unit: '/month',
      features: [['Unmetered DDoS'], ['Universal SSL', 'Global CDN']],
      cta: 'See Free plan',
    },
    {
      name: 'Pro',
      tagline: 'for pro websites',
      price: '$20',
      unit: '/mo billed annually',
      note: 'or $25/mo billed monthly',
      features: [['Image optimization'], ['Bot protection', 'Ticket support']],
      cta: 'See Pro plan',
    },
    {
      name: 'Business',
      tagline: 'for small business',
      price: '$200',
      unit: '/mo billed annually',
      note: 'or $250/mo billed monthly',
      features: [['PCI DSS 4.0', '100% uptime SLA'], ['Chat support']],
      cta: 'See Business plan',
    },
    {
      name: 'Contract',
      tagline: 'for mission-critical',
      price: 'Custom',
      note: 'Billed annually',
      features: [['Network priority', '24/7 support'], ['Custom contracts']],
      cta: 'See Contract plan',
    },
  ] satisfies Plan[],
}
