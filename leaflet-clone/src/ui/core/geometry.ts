/**
 * Single source of truth for page geometry.
 * Every panel of every leaflet has exactly this size (A4 tri-fold panel ratio 99:210),
 * and leaflets are always rendered unfolded and flat.
 */
export const PANEL = { width: 480, height: 1018 } as const

export type PanelCount = 3 | 4

export function sheetWidth(panels: PanelCount): number {
  return PANEL.width * panels
}
