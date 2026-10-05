import { StatusBar, type StatusBarProps } from '../../../ui'

/** Status bar tuned to the reference recording's metrics. */
export function PhoneStatusBar(props: StatusBarProps) {
  return <StatusBar paddingTop={15} fontSize={15.5} className="!pr-[19px]" {...props} />
}
