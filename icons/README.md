# Damus icons

The Damus mark is a red hexagon ring around a cyan eye. Wherever a platform allows it, the icon is the badge alone on a transparent background. The navy tile is kept only where an opaque, full-bleed icon is required.

| File | Size | Background | Used for |
| --- | --- | --- | --- |
| `icon.svg` | vector | none | Master artwork: the badge, full detail. |
| `icon-tile.svg` | vector | navy tile | Master for the icons that must be opaque. |
| `favicon.svg` | vector | none | Master for small sizes: heavier ring and a filled eye so it reads at 16 px. Its colours adjust to light and dark browser themes. Embedded in `index.html` by the build. |
| `favicon.ico` | 16, 32, 48 | none | Browser tab icon for browsers that do not use SVG icons. |
| `favicon-16.png`, `favicon-32.png`, `favicon-48.png` | 16, 32, 48 | none | Tab, bookmark and shortcut icons. |
| `icon-192.png`, `icon-512.png` | 192, 512 | none | Installed desktop app icon, listed in `manifest.webmanifest`. |
| `apple-touch-icon.png` | 180 | navy tile | Apple bookmarks and home screens. Apple fills transparent areas with black, so this one stays opaque. |
| `icon-maskable-192.png`, `icon-maskable-512.png` | 192, 512 | navy tile | For systems that crop icons to their own shape. These must fill the whole square, with the mark inside the safe zone. |

Colours: ring `#e0383c` and eye `#12b4d8` on transparent icons, chosen to hold up on both light and dark surfaces; ring `#ef4b50` and eye `#18d4f8` on the navy tile.

To change the mark, edit the SVG masters, re-render the PNG and ICO files at the sizes above, and rebuild `index.html`.
