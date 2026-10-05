# ASSET-PROMPTS — the two prompts (visual + sound), separate, at full depth

This is the deep spec behind **Stage 4 (THE TWO-PROMPT LAW)** in `SKILL.md`.

> ### THE LAW
> From `ANALYSIS.md`, produce **exactly two** asset prompts, as **two separate
> files**:
> 1. `ASSETS-VISUAL.md` — **images + transparent images + logos** (for an image
>    generator).
> 2. `ASSETS-SOUND.md` — **music + sound effects** (for an audio generator).
>
> Nothing else. No video clips. No voiceover. Two files, never merged.

---

## 1. Each file IS a prompt — not a spec sheet

This is the single most important thing, and the one most easily got wrong.

The file is **not** a table for a human to read and then rewrite. It is a
**self-contained instruction you hand directly to an AI agent** with the right
generator. Write it so the agent can execute every item and return files — with
**no further questions**.

So each file:
1. **Opens with the role and the task** — *"You are an AI agent with image
   generation. Produce every asset below and return ONE zip file."* State that
   voiceover and video clips are excluded.
2. **Gives the deliverable tree** — **one zip containing multiple zips inside**,
   one per category, with `MANIFEST.md` as the only loose file.
3. **Numbers every asset with its own executable brief** and its output path.
4. **Closes with acceptance checks.**

> **Depth is the point.** A thin list of names is wrong. Every item carries its
> **exact** values — hex colours, pixel dimensions, durations, BPM, cue times,
> filenames. The complete worked examples are:
> - `examples/EXAMPLE-ASSETS-VISUAL.md`
> - `examples/EXAMPLE-ASSETS-SOUND.md`
>
> **Match that depth.** If your file is much shorter than the examples, it is
> under-specified.

---

## 2. `ASSETS-VISUAL.md` — the visual-asset prompt

Covers **three** sections:

| Section | What | The rule |
|---|---|---|
| **1. Images** | backgrounds, plates, hero objects, textures, charts | one executable brief each: subject · composition · style · palette (hex) · lighting · aspect + background · negatives |
| **2. Transparent images** | cut-outs, icons, overlays, badges, caption PNGs | every brief ends **"transparent background, PNG with alpha"** |
| **3. Logos** | wordmark, mark, badges | if the client supplies an SVG, say so — never reproduce a real brand's mark; otherwise a brief or a `NOTE.md` |

**Deliverable tree:**
```
visual-assets.zip
├── MANIFEST.md
├── images.zip
├── transparent.zip
└── logos.zip
```

**Rules:** no text baked into any image (generated type is garbled — type is
rendered in the edit); every transparent item is a true alpha PNG; the palette is
the **measured hex** from `ANALYSIS.md`.

---

## 3. `ASSETS-SOUND.md` — the sound prompt

Covers **two** sections:

| Section | What | The rule |
|---|---|---|
| **1. Music** | bed tracks, stings, risers | one executable brief each: mood · genre · BPM · length · instrumentation · energy arc; master to the reference's LUFS; WAV + MP3 |
| **2. Sound effects** | whooshes, hits, ticks, risers, pops, UI sounds | one brief per cue, each **timed to a beat** from the analysis; type · character · duration |

**Deliverable tree:**
```
sound-assets.zip
├── MANIFEST.md
├── music.zip
└── sfx.zip
```

**Rules:** every cue time comes from the **beat map** in `ANALYSIS.md`; no
dialogue; deliver clean stems where possible.

---

## 4. What must NOT be in either file

- **No video clips.** (The build makes motion in the edit.)
- **No voiceover / A-roll.** (That comes from the user — Stage 5.)
- **No code components.** (The two prompts are images/logos and sound only —
  "that's it, and nothing". Any animated UI the reference needs is built at
  Stage 6.)
- **No merging.** Two files, two media, two generators.

---

## 5. Provenance & honesty

- Palette = **measured hex** from `ANALYSIS.md`, not invented.
- Never name the reference's brand/product/logo text — request the **form** ("a
  wordmark in this palette"), never the source's actual mark.
- Label any inferred cue as **inferred**.

---

## 6. Checklist before you send them

- [ ] Exactly two files exist: `ASSETS-VISUAL.md`, `ASSETS-SOUND.md`.
- [ ] Each **opens with the role + the task** and **ends with acceptance checks**.
- [ ] Each carries its **deliverable tree** (one zip, multiple zips inside).
- [ ] Every asset has an **executable brief** with **exact values**.
- [ ] Visual covers **images + transparent + logos**; sound covers **music + SFX**.
- [ ] No video clips, no voiceover, no code.
- [ ] Depth matches `examples/EXAMPLE-ASSETS-VISUAL.md` / `-SOUND.md`.
