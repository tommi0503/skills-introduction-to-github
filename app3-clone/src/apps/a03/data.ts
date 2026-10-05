import { ClipboardCheck, House, Layers, Search, type LucideIcon } from 'lucide-react'

export interface NavItem {
  key: string
  icon: LucideIcon
  label: string
}

export const navItems: NavItem[] = [
  { key: 'home', icon: House, label: 'Home' },
  { key: 'search', icon: Search, label: 'Search' },
  { key: 'task', icon: ClipboardCheck, label: 'Task' },
  { key: 'stack', icon: Layers, label: 'Library' },
]

export const notesHeader = { title: 'Notes & Docs', subtitle: '21 documents in personal workspace' }
export const tasksHeader = { title: 'Tasks & To-Dos', subtitle: '3 of 10 completed' }

export const noteFilters = ['All Notes', 'Growth', 'Personal', 'Work']
export const taskFilters = ['All', 'High', 'Medium', 'Low', 'Critical']

export const searchPlaceholder = 'Search notes, tags, content...'

export interface Note {
  key: string
  tag: string
  date: string
  title: string
  excerpt: string
}

const excerpt = 'Central knowledge hub for growth, personal tracking and weekly reviews.'

export const notes: Note[] = [
  { key: 'la', tag: 'Travel', date: '1 Yesterday', title: 'Los Angeles City Guide', excerpt },
  { key: 'james', tag: 'Journal', date: '1 Yesterday', title: "James' wiki", excerpt },
  { key: 'workout', tag: 'Fitness', date: '1 Yesterday', title: 'Workout Tracker Plan', excerpt },
  { key: 'journal', tag: 'Nutrition', date: '1 Yesterday', title: 'Journal & Daily Notes', excerpt },
  { key: 'skyline', tag: 'Travel', date: '1 Yesterday', title: 'City Trips', excerpt },
  { key: 'finance', tag: 'Finance', date: '1 Yesterday', title: 'Budget Review', excerpt },
]

export interface Task {
  key: string
  priority: string
  title: string
  time: string
  tag: string
}

export const tasks: Task[] = [
  { key: 'reply', priority: 'High', title: 'Reply to\nimportant emails', time: '11:30 AM - 12:00 PM', tag: 'Product' },
  { key: 'contacts', priority: 'Low', title: 'Update phone\ncontacts', time: '11:30 AM - 12:00 PM', tag: 'Team' },
  { key: 'meditate', priority: 'Medium', title: 'Meditate for 10\nminutes.', time: '11:30 AM - 12:00 PM', tag: 'Finance' },
  { key: 'run', priority: 'Medium', title: 'Go for a morning run\nbefore work', time: '11:30 AM - 12:00 PM', tag: 'Health' },
]
