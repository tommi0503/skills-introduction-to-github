import { ImagePlaceholder } from '../../../ui'

/** Calendar app logo (brand mark → placeholder), centred at its splash position. */
export function GoogleLogo({ tone }: { tone?: string }) {
  return (
    <ImagePlaceholder
      label="Google Calendar logo"
      tone={tone}
      className="absolute rounded-[9px]"
      style={{ left: 129, top: 278, width: 131, height: 132 }}
    />
  )
}
