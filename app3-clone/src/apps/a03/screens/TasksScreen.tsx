import { AppScreen } from '../../../ui'
import { BottomFade } from '../components/BottomFade'
import { DeviceChrome } from '../components/DeviceChrome'
import { FilterChips } from '../components/FilterChips'
import { FloatingNav } from '../components/FloatingNav'
import { PageHeader } from '../components/PageHeader'
import { TaskCard } from '../components/TaskCard'
import { navItems, taskFilters, tasks, tasksHeader } from '../data'
import { nd } from '../theme'

/** Tasks & To-Dos: priority filters and stacked task cards. */
export function TasksScreen() {
  return (
    <AppScreen background={nd.bg} className="font-poppins" style={{ color: nd.text }}>
      <DeviceChrome />
      <PageHeader {...tasksHeader} />
      <FilterChips labels={taskFilters} active={taskFilters[0]} top={126} />
      <div className="absolute top-[182px] right-[19px] left-[19px] flex flex-col gap-[11px]">
        {tasks.map((t) => (
          <TaskCard key={t.key} task={t} />
        ))}
      </div>
      <BottomFade />
      <FloatingNav items={navItems} activeKey="task" activeLabel="Task" />
    </AppScreen>
  )
}
