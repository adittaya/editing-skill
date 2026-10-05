# ASSETS-VISUAL — "Blue Glass" portfolio reel

> A **complete, ready-to-paste example** of `ASSETS-VISUAL.md`. Copy this shape
> for any build: replace the values with the ones measured in `ANALYSIS.md`.
> This file is **itself a prompt** — hand it straight to the image generator.

You are an AI agent with **image generation**. Produce every asset below and
return **ONE zip file** (`visual-assets.zip`) containing all outputs, organised
exactly as the deliverable tree shows. Use every value given exactly as written.
Do not ask questions. Do not generate video or voiceover — the user supplies the
A-roll separately.

---

## Deliverable — return ONE zip, containing MULTIPLE zips inside

```
visual-assets.zip                    ← the ONE zip you return
├── MANIFEST.md                      ← the only loose file
├── images.zip                       ← section 1 outputs
├── transparent.zip                  ← section 2 outputs (PNG with alpha)
└── logos.zip                        ← section 3 (or a NOTE.md inside)
```

No loose asset files — `MANIFEST.md` is the only loose file. The manifest lists
every file inside every zip, with its size and the beat it serves.

---

## 1. Images — generate (3) → `images/`

1. **Background plate** — 2560×1440 (16:9) → `images/background_plate.png`
   Generate a soft, blurred abstract gradient: deep navy `#182B74` at the bottom
   blending up through royal blue `#144EDF` and periwinkle `#5876E9` into a pale
   `#C7CFDF` highlight at the top. Smooth organic blobs, very soft focus, subtle
   film grain. No text, no objects, no people. High resolution, wallpaper quality.

2. **Workspace plate** — 1920×1080 → `images/workspace_plate.png`
   Generate a top-down soft-3D desk scene: matte rounded objects (a pencil cup,
   folded paper, a small cube) on a flat surface, lit in cool purple-blue light,
   shallow depth of field, gentle shadows. Muted and minimal. No text, no logos.

3. **Grain overlay** — 1920×1080 → `images/grain_overlay.png`
   Generate a very light film-grain texture, neutral grey, even, seamless and
   tileable. No objects, no text.

## 2. Transparent images — generate (3) → `transparent/`

Each must be a **PNG with a transparent background (alpha)**. No text.

1. **App tiles** — 512×512 each → `transparent/app_tiles.png` (three tiles in one
   file, or three files). Three rounded-square tiles in one consistent style:
   glossy soft-3D, subtle inner highlight, soft shadow, one accent hue each.
2. **Glass disc** — 800×800 → `transparent/glass_disc.png`. A glossy translucent
   blue disc, refractive glass material, soft specular rim, subtle blue glow,
   centred. Transparent background, PNG with alpha.
3. **Hand cursor** — 256×256 → `transparent/hand_cursor.png`. A clean white
   hand-pointer cursor icon, minimal, slight soft shadow, crisp edges.
   Transparent background, PNG with alpha.

## 3. Logos — `logos/`

The editor's wordmark and handle badge are **supplied by the user as an SVG**.
Do not generate or reproduce a logo. If nothing is supplied, write
`logos/NOTE.md` saying the wordmark is set in the reel's typeface as plain text —
no generated mark.

---

## Acceptance checks before you return the zip

- Sections 1, 2 and 3 are all present; section 3 is a `NOTE.md` if nothing is
  supplied.
- Every value given was used exactly (hex, px, dimensions).
- **No text appears inside any generated image.**
- Every transparent item is a true PNG with alpha.
- The zip contains **multiple zips** (one per category) — no loose asset files
  except `MANIFEST.md`.
- `MANIFEST.md` lists every zip, and inside them every file, with its size and the
  beat it serves.
- The zip contains **no** voiceover and **no** video clips.
