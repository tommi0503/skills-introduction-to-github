export { cn } from './core/cn'
export type { ShowcaseDefinition, AppDefinition } from './core/showcase'
export { Stage, type StageProps } from './core/Stage'
export { Placed, type PlacedProps } from './core/Placed'
export { Scaled, type ScaledProps } from './core/Scaled'

export { PhoneFrame, type PhoneFrameProps, type BezelSpec } from './device/PhoneFrame'
export { StatusBar, type StatusBarProps } from './device/StatusBar'
export { SignalBars, Battery, type BatteryProps } from './device/StatusGlyphs'
export { DynamicIsland, type DynamicIslandProps } from './device/DynamicIsland'
export { HomeIndicator, type HomeIndicatorProps } from './device/HomeIndicator'

export { ImagePlaceholder, type ImagePlaceholderProps } from './media/ImagePlaceholder'
export { Avatar, type AvatarProps } from './media/Avatar'

export { IconButton, type IconButtonProps } from './controls/IconButton'
export { Button, type ButtonProps } from './controls/Button'
export { ChipGroup, type ChipGroupProps, type ChipItem } from './controls/ChipGroup'
export { SearchField, type SearchFieldProps } from './controls/SearchField'
export { SegmentedControl, type SegmentedControlProps } from './controls/SegmentedControl'
export { Toggle, type ToggleProps } from './controls/Toggle'

export { TabBar, IconLabelTab, type TabBarProps, type TabItem, type DefaultTabProps } from './navigation/TabBar'

export { SCREEN, BOARD, boardWidth, boardHeight } from './board/geometry'
export { AppScreen, type AppScreenProps } from './board/AppScreen'
export { ScreenBoard, type ScreenBoardProps } from './board/ScreenBoard'
export { HighlightChip, type HighlightChipProps } from './device/HighlightChip'
