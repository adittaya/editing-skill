# ASSETS-VISUAL — <project>

> This file **is a prompt.** Hand it straight to an image generator. Fill every
> `<...>` from `ANALYSIS.md` (palette = measured hex; sizes = the reference's
> aspect). See `examples/EXAMPLE-ASSETS-VISUAL.md` for a complete worked example —
> **match that depth**: exact px, exact hex, one executable brief per asset.

You are an AI agent with **image generation**. Produce every asset below and
return **ONE zip file** (`visual-assets.zip`) containing all outputs, organised
exactly as the deliverable tree shows. Use every value given exactly as written.
Do not ask questions. Do not generate video or voiceover — the user supplies the
A-roll separately.

---

## Deliverable — return ONE zip, containing MULTIPLE zips inside

```
visual-assets.zip
├── MANIFEST.md            ← the only loose file
├── images.zip             ← section 1 outputs
├── transparent.zip        ← section 2 outputs (PNG with alpha)
└── logos.zip              ← section 3 (or a NOTE.md inside)
```

`MANIFEST.md` lists every file inside every zip, with its size and the beat it
serves.

---

## 1. Images — generate (<N>) → `images/`

One **executable brief** per asset: subject · composition · style · palette (hex)
· lighting · aspect + background · negatives.

1. **<name>** — <W×H> (<aspect>) → `images/<file>.png`
   <brief: what it is, the palette hex, the lighting, "no text, no objects">.
2. **<name>** — <W×H> → `images/<file>.png`
   <brief>.

## 2. Transparent images — generate (<N>) → `transparent/`

Each must be a **PNG with a transparent background (alpha)**. Every brief ends
with "transparent background, PNG with alpha". No text.

1. **<name>** — <W×H> → `transparent/<file>.png`. <brief>. Transparent
   background, PNG with alpha.
2. **<name>** — <W×H> → `transparent/<file>.png`. <brief>. Transparent
   background, PNG with alpha.

## 3. Logos — `logos/`

<The mark(s) needed. If the client supplies an SVG, say so — do not reproduce a
real brand's mark. Otherwise write a brief, or `logos/NOTE.md` stating the
wordmark is set as plain text in the reel's typeface.>

---

## Acceptance checks before you return the zip

- Sections 1, 2 and 3 are present; section 3 is a `NOTE.md` if nothing is supplied.
- Every value given was used exactly (hex, px, dimensions).
- **No text appears inside any generated image.**
- Every transparent item is a true PNG with alpha.
- The zip contains **multiple zips** — no loose asset files except `MANIFEST.md`.
- `MANIFEST.md` lists every zip, and inside them every file, with its size and the
  beat it serves.
- The zip contains **no** voiceover and **no** video clips.
