import type { LucideIcon } from 'lucide-react'
import { Cloud, Server, Cpu } from 'lucide-react'

export interface NavLink { label: string; dropdown?: boolean }
export interface CtaLink { label: string; variant: 'primary' | 'outline' | 'ghost' }

export const nav = {
  links: [
    { label: 'Products', dropdown: true },
    { label: 'Resources', dropdown: true },
    { label: 'Voices' },
    { label: 'Languages' },
    { label: 'Customers' },
    { label: 'Pricing' },
  ] satisfies NavLink[],
  actions: [
    { label: 'Sign in', variant: 'ghost' },
    { label: 'Contact Sales', variant: 'outline' },
    { label: 'Try Cartesia', variant: 'primary' },
  ] satisfies CtaLink[],
}

export const hero = {
  titleMuted: '#1-ranked realtime interaction models.',
  title: 'Built on frontier AI research.',
  body: 'One API for speech generation, transcription, and production voice agents — fast enough for live conversation.',
  ctas: [
    { label: 'Try Cartesia', variant: 'primary' },
    { label: 'Contact Sales', variant: 'outline' },
  ] satisfies CtaLink[],
  /** Voice orbs: [x, y, size] in page coordinates. */
  orbs: [
    [341, 491, 66], [453, 470, 108], [621, 425, 199], [881, 470, 108], [1035, 491, 66],
  ] as const,
  voice: { name: 'Talk to Skylar', tone: 'Warm and unhurried' },
}

export const industries = {
  muted: 'Voice agents for',
  strong: 'every industry',
  tabs: ['Finance', 'Healthcare', 'Government'],
  active: 0,
  panel: {
    title: 'Financial services',
    body: 'Voice agents that improve customer experience, enhance security, and streamline operations across the financial ecosystem.',
  },
}

export const customers = {
  lead: 'Join the teams making the',
  leadStrong: 'switch to Cartesia',
  stat: { title: 'Ranked #1', body: 'in Speech Arena leaderboard & Speech to Text leaderboard by Artificial Analysis' },
  /** Logo bounding boxes inside each grid cell (w, h). */
  logos: [
    [163, 24], [207, 22], [102, 28], [159, 27],
    [111, 31], [167, 34], [124, 27], [157, 25],
  ] as const,
}

export interface Product { name: string; tag: string; body: string }

export const stack = {
  muted: 'The full stack for',
  strong: 'interactive intelligence',
  body: 'Built on State Space Models (SSMs), a new primitive for low latency, long-context reasoning, and greater efficiency at scale.',
  cta: 'Try Cartesia',
  models: [
    { name: 'Ink.', tag: 'Speech-to-text', body: 'The fastest, most accurate streaming transcription model.' },
    { name: 'Sonic.', tag: 'Text-to-speech', body: 'The fastest, ultra-realistic voice synthesis model.' },
  ] satisfies Product[],
  agentsTitle: 'Voice agents as fast and accurate as the models powering them',
  agents: {
    name: 'Managed Agents.',
    tag: 'Build voice agents',
    body: 'The fastest, most customizable platform for building and shipping enterprise voice agents, powered by our models.',
  } satisfies Product,
}

export const research = {
  title: 'Pioneering AI research:',
  subtitle: 'Architectures that learn through real-world interaction',
  body: 'Our team has pioneered breakthrough AI architectures, including state space models (SSMs), Mamba & H-Nets. Our research manifests our mission — we architect AI that learns from and interacts with the world like humans do.',
  cta: 'Our research',
}

export interface DeployOption { icon: LucideIcon; label: string; body?: string; open?: boolean }

export const deploy = {
  muted: 'Deploy AI anywhere.',
  strong: 'Own it everywhere.',
  body: 'The same models and agents across cloud, on-premise, and on-device. Inference runs in-region — keeping you within your latency envelope, data residency obligations, and compliance frameworks.',
  options: [
    {
      icon: Cloud,
      label: 'Cloud',
      open: true,
      body: 'Deploy via regional API endpoints across the globe — ensuring in-region processing, high availability, and the uptime your production systems demand.',
    },
    { icon: Server, label: 'On-premise' },
    { icon: Cpu, label: 'On-device' },
  ] satisfies DeployOption[],
}

export const getStarted = {
  title: 'Get started today',
  columns: [
    {
      title: 'Talk to an expert.',
      body: 'Connect with a member of our team and learn how Cartesia can help you build world-class voice experiences.',
      cta: { label: 'Contact Sales', variant: 'outline' },
    },
    {
      title: 'Start building.',
      body: 'Access our models via API and bring a voice agent into production in minutes.',
      cta: { label: 'Try Cartesia', variant: 'primary' },
    },
  ] satisfies { title: string; body: string; cta: CtaLink }[],
  hiring: { title: 'We’re hiring!', body: 'Build the future of interactive intelligence', cta: 'Careers page' },
}

export const cookie = {
  title: 'We use cookies',
  body: 'Accept all, or pick what you’re comfortable with.',
  link: 'Privacy Policy',
  actions: [
    { label: 'Customize', variant: 'outline' },
    { label: 'Accept', variant: 'primary' },
  ] satisfies CtaLink[],
}
