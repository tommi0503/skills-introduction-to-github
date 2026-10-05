import { Image, Settings, X, ZapOff } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { CornerBrackets } from '../components/CornerBrackets'
import { GlassButton } from '../components/GlassButton'
import { ModeSelector } from '../components/ModeSelector'
import { ShutterButton } from '../components/ShutterButton'
import { activeMode, captureModes } from '../data'
import { theme } from '../theme'

/** Live camera capture with document detection brackets. */
export function CameraScreen() {
  return (
    <div className="absolute inset-0">
      <ImagePlaceholder label="wooden desk camera feed" className="absolute inset-0" />
      <Box rect={{ x: 23, y: 22, w: 36, h: 36 }}>
        <GlassButton icon={X} iconSize={23} />
      </Box>
      <Box rect={{ x: 265, y: 22, w: 88, h: 36 }} className="flex justify-between">
        <GlassButton icon={ZapOff} iconSize={19} />
        <GlassButton icon={Settings} iconSize={19} />
      </Box>

      <Box rect={{ x: 32, y: 197, w: 308, h: 426 }}>
        <ImagePlaceholder label="document in viewfinder" tone="#f3f4f6" className="h-full w-full" />
      </Box>
      <Box rect={{ x: 55, y: 231, w: 267, h: 354 }}>
        <CornerBrackets length={29} thickness={3.5} color={theme.accent} />
      </Box>

      <Box rect={{ x: 66, y: 623, w: 245, h: 36 }}>
        <ModeSelector modes={captureModes} active={activeMode} />
      </Box>

      <Box rect={{ x: 23, y: 712, w: 44, h: 45 }}>
        <ImagePlaceholder label="last scan" tone="#cfd1d4" className="h-full w-full rounded-[6px]" />
      </Box>
      <Box rect={{ x: 150.5, y: 698, w: 74, h: 74 }}>
        <ShutterButton />
      </Box>
      <Box rect={{ x: 308, y: 712, w: 46, h: 45 }}>
        <div className="flex h-full w-full items-center justify-center rounded-[8px] text-white" style={{ background: theme.glass }}>
          <Image size={19} strokeWidth={2} />
        </div>
      </Box>
    </div>
  )
}
