# EXTRACTION-PROTOCOL — read a reference at maximum accuracy

This is the deep checklist behind **Stage 2 (THE EXTRACTION LAW)** in `SKILL.md`.
Its whole purpose is **accuracy**. A reference that is 95% read produces a build
that is 60% right; a reference that is 100% read produces a build that is right.

> **The one rule:** extract **everything**, at **maximum resolution**, and
> **zoom** until nothing is unread. Never analyse from a handful of thumbnails.

---

## 1. Read the input type first

| Input | Passes to run |
|---|---|
| **Video file** | A (frames) → B (audio) → C (cuts) → D (text) → E (elements) → F (colour) → G (motion) |
| **Contact sheet (image/PDF)** | A' (panels) → D (text) → E (elements) → F (colour) |
| **Link** | Fetch; then whichever of the above fits the fetched media. |

---

## 2. PASS A — Frames (video)

1. **Baseline pass at 2 FPS** — a first look at the whole thing.
2. **Dense pass around every cut and every text change** — 10-30 FPS in those
   windows. Text that appears for 8 frames is invisible at 2 FPS.
3. **Key-frame pass** — the single frame where each element is *most complete*
   (a chart fully drawn, a logo fully on).
4. Save frames with **time in the filename** (`f_0012.40s.png`) so every later
   note is traceable.

Tool: `tools/extract.py --video REF.mp4 --fps 2 --dense`.

## 3. PASS A' — Panels (contact sheet)

1. Read **every panel**, left-to-right, top-to-bottom, in order.
2. Number them (`00s`, `01s`, …) exactly as the sheet does.
3. **Zoom each panel** — a panel is often 4-6 elements; read them one at a time.
4. Note the **header** (title, frame count, aspect) and the **style line**
   (e.g. "CINEMATIC • MODERN • CLEAN • PREMIUM").

## 4. PASS B — Audio (video)

1. **Loudness curve** — measure integrated LUFS and the peaks.
2. **Music cues** — where music starts/stops/changes.
3. **SFX hits** — every whoosh, hit, riser, click; note the frame it lands on.
4. **Transcript** — full text, **word-level timings** if possible.

Tool: `tools/analyze.py --video REF.mp4`.

## 5. PASS C — Cuts

List every scene change as a frame + time. Classify the transition (hard cut,
dissolve, whip, glitch, match-cut). This becomes the **cut spine** of the beat
map.

## 6. PASS D — Text (verbatim, always)

- OCR **every** on-screen word. **Verbatim** — do not paraphrase, do not fix
  spelling, do not translate.
- Record **in/out time** for each text element.
- Record **position** (safe-area zone), **weight**, **case**, **colour**, and
  **animation** (word-by-word, typewriter, pop, slide).
- Note **recurring** strings vs **changing** strings (e.g. a title that stays,
  a number that counts up).

## 7. PASS E — Elements

Inventory every non-text element:
- **logos** (and where they sit),
- **UI** (buttons, cards, cursors, menus),
- **charts / data** (bars, rings, sparklines — and the **numbers**, verbatim),
- **characters / people** (and their framing),
- **icons, props, textures, backgrounds**.

For each: what it is, where it is, how it enters/exits, and its source (native,
stock, generated).

## 8. PASS F — Colour

- Sample **hex** per element, per shot (not one average for the whole video).
- Identify the **dominant**, **accent** and **background** colours and their role.
- Note gradients and their direction.

Tool: `tools/analyze.py --palette`.

## 9. PASS G — Motion

For every move: what moves, **how** (pan/zoom/parallax/rack/dolly), **how fast**,
**why** (motivation), and whether it is a camera move or an element move. Follow
the **Camera Law** vocabulary in `SKILL.md`.

---

## 10. The verify pass (do not skip)

1. **Sample re-check** — pick 8-10 frames/tiles at random, re-open them, and
   compare against your extraction. Fix every miss.
2. **Time-axis check** — every text element has a plausible in/out; every cut
   aligns with an audio cue.
3. **Completeness check** — the element inventory has an entry for everything
   visible; nothing is "misc".
4. **Honesty check** — everything inferred is labelled **inferred**.

## 11. Output of this protocol

A single filled-in `ANALYSIS.md` (see `templates/ANALYSIS.template.md`) plus the
V1/V2/V3 contact sheets. Nothing else. This file is the source of truth for every
later stage.
